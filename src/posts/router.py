from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm.persistence import save_obj
from sqlmodel import Session
from database import get_db
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten,du_lieu_theo_ngay
from src.posts.crud_base import CRUDBase

router = APIRouter()
nhan_crud = CRUDBase(Nhan)

@router.get("/")
def root():
    return {"message": "API đang hoạt động bình thường"}

@router.get("/search/", response_model=List[Nhan])
def nhan_valuu_dulieu_nhanhieu(q: str, db: Session = Depends(get_db)):
    nh_dulieu = du_lieu_ten(q)
    saved = []

    for nh in nh_dulieu:#
        try:
            created = nhan_crud.create_if_not_exists(
                db=db,
                obj_data=nh,
                unique_fields=[
                    "maunhan", "nhanhieu", "nhom", "status",
                    "ngaynopdon", "sodon", "chudon", "daidienshcn"
                ]
            )
            if created:
                saved.append(created)
        except Exception as e:
            print(f"Lỗi khi xử lý bản ghi: {e}")
            continue

    try:
        nhan_crud.save_changes(db)
    except Exception as e:
        print(f"Lỗi khi lưu vào CSDL: {e}")
        return []

    if not saved:
        try:
            return nhan_crud.get_all(db)
        except Exception as e:
            print(f"Lỗi khi truy xuất dữ liệu: {e}")
            return []

    return saved


@router.get("/search_theongay",response_model=List[Nhan])
def nhan_dulieu_search_theongay(start : str , end : str, db: Session = Depends(get_db)):
    stn_dulieu = du_lieu_theo_ngay(start,end)
    saved_stn = []

    for stn in stn_dulieu:
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
            continue
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
