import logging
from typing import List

import requests
from bs4 import BeautifulSoup

from src.posts.dependencies import TrangThaiEnum
from src.posts.service import luu_model
#minhdang

def du_lieu_status(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
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


def du_lieu_name_status(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,name_mix_status: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
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

def du_lieu_name_status_group(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,name_mix_status: str,group: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_mix_status}&gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
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

def du_lieu_status_group(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,group: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Đang%20giải%20quyết&s=Từ%20chối&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?gop=any&g={group}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&p={page}"
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