from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm.persistence import save_obj
from sqlmodel import Session
from database import get_db
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten,du_lieu_theo_ngay,luu_from_router_don
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
            saved_stn = luu_from_router_don(nh, saved, db, nhan_crud)
    return saved


@router.get("/search_theongay",response_model=List[Nhan])
def nhan_dulieu_search_theongay(start : str , end : str, db: Session = Depends(get_db)):
    stn_dulieu = du_lieu_theo_ngay(start,end)
    saved_stn = []

    for stn in stn_dulieu:
        saved_stn = luu_from_router_don(stn,saved_stn,db,nhan_crud)
    return saved_stn
