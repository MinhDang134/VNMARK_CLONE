import logging
from datetime import datetime
from typing import List
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

from src.posts.dependencies import TrangThaiEnum, LoaiDonEnum
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


def du_lieu_name_status_shcn(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,name: str,shcn: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&r={shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&r={shcn}&p={page}"
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


def du_lieu_name_status_chudon(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,name: str,chudon: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
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


def du_lieu_status_dd_shcn(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,dd_shcn: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&r={dd_shcn}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&r={dd_shcn}&p={page}"
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


def du_lieu_status_chudon(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,chudon: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&a=Rút%20đơn&r={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&a={chudon}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&a={chudon}&p={page}"
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


def du_lieu_status_date(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,startday : str, endday: str):
    startday_fix = datetime.strptime(startday, "%d-%m-%Y")
    endday_fix = datetime.strptime(endday, "%d-%m-%Y")
    fd_param = quote_plus(f"{startday_fix.strftime('%d/%m/%Y')} - {endday_fix.strftime('%d/%m/%Y')}")
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&a=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
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

def du_lieu_status_loaidon(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str, loaidons: List[LoaiDonEnum]):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        #----------------
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
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



def du_lieu_name_status_loaidon(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str, loaidons: List[LoaiDonEnum], name: str):
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_gia in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=0&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        #----------------
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Đang%20giải%20quyết&s=Từ%20chối&t=1&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if LoaiDonEnum.don_quoc_te in loaidons and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&t=1&p={page}"
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

def du_lieu_name_status_date(TrangThaiEnum: str, trang_thais: List[TrangThaiEnum], page: str,name_st_d : str ,startday : str, endday: str):
    startday_fix = datetime.strptime(startday, "%d-%m-%Y")
    endday_fix = datetime.strptime(endday, "%d-%m-%Y")
    fd_param = quote_plus(f"{startday_fix.strftime('%d/%m/%Y')} - {endday_fix.strftime('%d/%m/%Y')}")
    try:
        url = None
        headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # rut_don
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&a=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # tu_choi
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # dang_giai_quyet
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # cap_bang
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Đang%20giải%20quyết&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        # 3 dau
        if TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.rut_don in trang_thais and TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Đang%20giải%20quyết&s=Từ%20chối&fd={fd_param}&p={page}"
            headers = {"User-Agent": "Mozilla/5.0"}
        if TrangThaiEnum.tu_choi in trang_thais and TrangThaiEnum.cap_bang in trang_thais and TrangThaiEnum.dang_giai_quyet in trang_thais and TrangThaiEnum.rut_don in trang_thais:
            url = f"https://vietnamtrademark.net/search?q={name_st_d}&s=Cấp%20bằng&s=Đang%20giải%20quyết&s=Từ%20chối&s=Rút%20đơn&fd={fd_param}&p={page}"
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