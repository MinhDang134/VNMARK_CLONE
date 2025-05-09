import logging
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup
from typing import List
from src.posts.models import Nhan
from datetime import datetime

logger = logging.getLogger(__name__)


def du_lieu_ten(q: str) -> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?q={q}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except Exception as e:
        logging.info(f"Lỗi khi gọi request: {e}")
        logging.info("Không có dữ liệu")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    nhan_hieu = []

    rows = soup.select("table tbody tr")
    for row in rows:
        cols = row.select("td")
        if len(cols) >= 10:
            try:
                maunhan = cols[2].get_text(strip=True)
                nhanhieu = cols[3].get_text(strip=True)
                nhom = cols[4].get_text(strip=True)
                status = cols[5].get_text(strip=True)
                ngaynopdon_str = cols[6].get_text(strip=True)
                ngaynopdon = datetime.strptime(ngaynopdon_str,
                                               "%d/%m/%Y") if ngaynopdon_str and "/" in ngaynopdon_str else None
                sodon = cols[7].get_text(strip=True)
                chudon = cols[8].get_text(strip=True)
                daidienshcn = cols[9].get_text(strip=True)

                if nhanhieu:
                    nhan_hieu.append(
                        Nhan(
                            maunhan=maunhan,
                            nhanhieu=nhanhieu,
                            nhom=nhom,
                            status=status,
                            ngaynopdon=ngaynopdon,
                            sodon=sodon,
                            chudon=chudon,
                            daidienshcn=daidienshcn
                        )
                    )
            except (ValueError, TypeError) as e:
                logging.error(f"Lỗi khi xử lý dòng dữ liệu: {e}")
                continue

    return nhan_hieu


def du_lieu_theo_ngay(startday: str, endday: str):
    startday_fix = datetime.strptime(startday, "%Y-%m-%d")
    endday_fix = datetime.strptime(endday, "%Y-%m-%d")
    fd_param = quote_plus(f"{startday_fix.strftime('%d/%m/%Y')} - {endday_fix.strftime('%d/%m/%Y')}")
    url = f"https://vietnamtrademark.net/search?fd={fd_param}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except Exception as e:
        logging.info(f"Lỗi khi gọi request: {e}")
        logging.info("Không có dữ liệu")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    nhan_hieu = []

    rows = soup.select("table tbody tr")
    for row in rows:
        cols = row.select("td")
        if len(cols) >= 10:
            nhan_hieu = luu_model(cols,nhan_hieu)

    return nhan_hieu


def luu_model(cols, dulieu: list):
    try:
        maunhan = cols[2].get_text(strip=True)
        nhanhieu = cols[3].get_text(strip=True)
        nhom = cols[4].get_text(strip=True)
        status = cols[5].get_text(strip=True)
        ngaynopdon_str = cols[6].get_text(strip=True)
        ngaynopdon = datetime.strptime(ngaynopdon_str, "%d/%m/%Y") if ngaynopdon_str and "/" in ngaynopdon_str else None
        sodon = cols[7].get_text(strip=True)
        chudon = cols[8].get_text(strip=True)
        daidienshcn = cols[9].get_text(strip=True)

        if nhanhieu:
            dulieu.append(
                Nhan(
                    maunhan=maunhan,
                    nhanhieu=nhanhieu,
                    nhom=nhom,
                    status=status,
                    ngaynopdon=ngaynopdon,
                    sodon=sodon,
                    chudon=chudon,
                    daidienshcn=daidienshcn
                )
            )
    except (ValueError, TypeError) as e:
        logging.error(f"Lỗi khi xử lý dòng dữ liệu: {e}")

    return dulieu
