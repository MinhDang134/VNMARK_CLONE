from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session
from database import get_db
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten
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

    for nh in nh_dulieu:
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
