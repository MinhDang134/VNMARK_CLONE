import logging
from urllib.parse import quote_plus

from requests import Session

import requests
from bs4 import BeautifulSoup
from typing import List
from src.posts.models import Nhan
from datetime import datetime
from src.posts.dependencies import TrangThaiEnum, LoaiDonEnum

logger = logging.getLogger(__name__)


def du_lieu_loaidon(LoaiDonENum: str, loaidons: List[LoaiDonEnum], page: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonENum.don_quoc_gia in loaidons:
            url = f"https://vietnamtrademark.net/search?t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonENum.don_quoc_te in loaidons:
            url = f"https://vietnamtrademark.net/search?t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if url:
            try:
                resp = requests.get(url, headers=headers)
                resp.raise_for_status()
            except Exception as e:
                logging.info(f"Lỗi khi gọi request: {e}")
                return []

            soup = BeautifulSoup(resp.text, "html.parser")
            nhan_hieu = []

            rows = soup.select("table tbody tr")
            for row in rows:
                cols = row.select("td")
                if len(cols) >= 10:
                    nhan_hieu = luu_model(cols, nhan_hieu)

            return nhan_hieu
        else:
            return {"message": "Không có trạng thái nào được xử lý!"}
    except Exception as e:
        logging.info(f"Lỗi tổng quát: {e}")
        return []
def du_lieu_ten_mix_group(name_mix_group: str , group : str , page:str)-> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?q={name_mix_group}&gop=any&g={group}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu



def du_lieu_ten(q: str, page: str) -> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?q={q}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu


def du_lieu_group(group: str, page: str) -> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?gop=any&g={group}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu

def dulieu_n_mix_loaidon(name_of_loaidon:str,page:str, loaidons: List[LoaiDonEnum]):
        if LoaiDonEnum.don_quoc_gia in loaidons:
            url = f"https://vietnamtrademark.net/search?q={name_of_loaidon}&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons:
            url = f"https://vietnamtrademark.net/search?q={name_of_loaidon}&t=1&p={page}"
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
                nhan_hieu = luu_model(cols, nhan_hieu)

        return nhan_hieu

def du_lieu_ten_dd_shcn(q: str, page: str) -> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?a={q}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu

def du_lieu_ten_mix_shcn(name_mix_shcn: str , dd_shcn : str , page:str)-> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?q={name_mix_shcn}&r={dd_shcn}p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu
def du_lieu_ten_mix_chudon(name_mix_chudon: str , chudon : str , page:str)-> List[Nhan]:
    url = f"https://vietnamtrademark.net/search?q={name_mix_chudon}&a={chudon}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

    return nhan_hieu

def du_lieu_search_name_date(startday: str , endday: str, name_mix_date: str,page:str):
    startday_fix = datetime.strptime(startday, "%d-%m-%Y")
    endday_fix = datetime.strptime(endday, "%d-%m-%Y")
    fd_param = quote_plus(f"{startday_fix.strftime('%d/%m/%Y')} - {endday_fix.strftime('%d/%m/%Y')}")
    url = f"https://vietnamtrademark.net/search?q={name_mix_date}&fd={fd_param}&p={page}"
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
            nhan_hieu = luu_model(cols, nhan_hieu)

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





def luu_from_router_don(stn: str, saved_stn: list, db: Session, nhan_crud: list):
    try:
        created = nhan_crud.create_if_not_exists(
            db=db,
            obj_data=stn,
            unique_fields=[
                "maunhan", "nhanhieu", "nhom", "status",
                "ngaynopdon", "sodon", "chudon", "daidienshcn"
            ]
        )
        if created:
            saved_stn.append(created)
    except Exception as e:
        print(f"Lỗi khi xử lý search_theongay  bản ghi: {e}")

    try:
        nhan_crud.save_changes(db)
    except Exception as e:
        print(f"Lỗi khi lưu search_theongay  vào CSDL: {e}")
        return []

    if not saved_stn:
        try:
            return nhan_crud.get_all(db)
        except Exception as e:
            print(f"Lỗi khi search_theongay dữ liệu: {e}")
            return []

    return saved_stn
