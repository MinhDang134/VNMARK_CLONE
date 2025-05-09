import logging
from typing import Optional
import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter, Depends, Query
from typing import List

from sqlalchemy.orm.persistence import save_obj
from sqlmodel import Session
from database import get_db
from src.posts.dependencies import TrangThaiEnum
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten, du_lieu_theo_ngay, luu_from_router_don, luu_model,du_lieu_status
from src.posts.crud_base import CRUDBase

router = APIRouter()
nhan_crud = CRUDBase(Nhan)

@router.get("/")
def root():
    return {"message": "API đang hoạt động bình thường"}

@router.get("/search/", response_model=List[Nhan])
def nhan_valuu_dulieu_nhanhieu(q: str, page:str ,db: Session = Depends(get_db)):
    nh_dulieu = du_lieu_ten(q,page)
    saved = []
    for nh in nh_dulieu:#
            saved_tt = luu_from_router_don(nh, saved, db, nhan_crud)
    return saved_tt


@router.get("/search_theongay",response_model=List[Nhan])
def nhan_dulieu_search_theongay(start : str , end : str, db: Session = Depends(get_db)):
    stn_dulieu = du_lieu_theo_ngay(start,end)
    saved_stn = []
    for stn in stn_dulieu:
        saved_stn = luu_from_router_don(stn,saved_stn,db,nhan_crud)
    return saved_stn
@router.get("/search_status")
def nhan_dulieu_status(
    page: Optional[str],
    db : Session = Depends(get_db),
    trang_thais: List[TrangThaiEnum] = Query(..., title="Trạng thái cần lọc", description="Chọn một hoặc nhiều trạng thái")):
    st_dulieu = du_lieu_status(TrangThaiEnum,trang_thais,page)
    saved_st = []
    for st in st_dulieu:
        saved_st = luu_from_router_don(st,saved_st,db,nhan_crud)
    return saved_st

# @router.get("/research_shcn")
# def nhan_dulieu_shcn(page: Optional[str],daidien_shcn: str,db: Session = Depends(get_db)):
#     dd_shcn_dulieu = du_lieu_ten(daidien_shcn,page)






