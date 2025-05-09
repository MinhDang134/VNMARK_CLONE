import logging
from typing import Optional
import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter, Depends, Query
from typing import List

from sqlalchemy.orm.persistence import save_obj
from sqlmodel import Session
from database import get_db
from src.posts.dependencies import TrangThaiEnum,LoaiDonEnum
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten, du_lieu_theo_ngay, luu_from_router_don, luu_model, du_lieu_status, \
    du_lieu_ten_dd_shcn,du_lieu_group,du_lieu_loaidon,dulieu_n_mix_loaidon,du_lieu_ten_mix_group
from src.posts.crud_base import CRUDBase

router = APIRouter()
nhan_crud = CRUDBase(Nhan)

@router.get("/search_DON----------------------")
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

@router.get("/research_shcn")
def nhan_dulieu_shcn(page: Optional[str],daidien_shcn: str,db: Session = Depends(get_db)):
    dd_shcn_dulieu = du_lieu_ten_dd_shcn(daidien_shcn,page)
    save_dd_shcn = []
    for dd_shcn in dd_shcn_dulieu:
        saved_dd = luu_from_router_don(dd_shcn, save_dd_shcn, db, nhan_crud)
    return saved_dd

@router.get("/search_group")
def nhan_dulieu_group(page: Optional[str],group : str ,db: Session = Depends(get_db)):
    dd_group = du_lieu_group(group,page)
    saved_dd_group = []
    for dd_group_dulieu in dd_group:
        saved_dd_group = luu_from_router_don(dd_group_dulieu,saved_dd_group,db,nhan_crud)
    return  saved_dd_group

@router.get("/search_chuho")
def nhan_dulieu_chuho(page: Optional[str],chuho: str,db: Session = Depends(get_db)):
    chuho_dulieu = du_lieu_ten_dd_shcn(chuho,page)
    save_dd_chuho = []
    for dd_shcn in chuho_dulieu:
        saved_chuho = luu_from_router_don(dd_shcn, save_dd_chuho, db, nhan_crud)
    return saved_chuho

@router.get("/search_loai_don")
def nhan_dulieu_loaidon(
    page: Optional[str],
    db : Session = Depends(get_db),
    loaidons: List[LoaiDonEnum] = Query(..., title="Trạng thái cần lọc", description="Chọn một hoặc nhiều loại đơn xem ")):
    ld_dulieu = du_lieu_loaidon(LoaiDonEnum,loaidons,page)
    saved_ld = []
    for ld in ld_dulieu:
        saved_ld = luu_from_router_don(ld,saved_ld,db,nhan_crud)
    return saved_ld

@router.get("/search_ten-----------------")
def phankethop():
    print("Phần kết hợp")

@router.get("/search_name_mix_loaidon")
def search_name_mix_loaidon(name_of_loaidon : str,
                            page:str,
                            db:Session = Depends(get_db)
                            ,loaidons: List[LoaiDonEnum] = Query(..., title="Trạng thái cần lọc", description="Chọn một hoặc nhiều loại đơn xem ")):
    nh_n_mix_loaidon = dulieu_n_mix_loaidon(name_of_loaidon,page,loaidons)
    saved_n_mix_loaidon = []
    for nh in nh_n_mix_loaidon:#
            saved_n_mix_loaidon = luu_from_router_don(nh, saved_n_mix_loaidon, db, nhan_crud)
    return saved_n_mix_loaidon


@router.get("/search_name_mix_group")
def search_name_mix_group(name_mix_group : str, group : str,page:str , db:Session = Depends(get_db)):
    name_group = du_lieu_ten_mix_group(name_mix_group, group,page)
    saved_name_group = []
    for ng in name_group:  #g
        saved_name_group = luu_from_router_don(ng, saved_name_group, db, nhan_crud)
    return saved_name_group



