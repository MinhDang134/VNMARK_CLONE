from fastapi import APIRouter
from typing import List

from fastapi.params import Depends
from sqlmodel import Session, select
from database import get_db
from src.posts.models import Nhan
from src.posts.service import du_lieu_ten

router = APIRouter()




@router.get("/")
def root():
    return {"message": "API đang hoạt động bình thường"}

@router.get("/search/", response_model=List[Nhan])
def nhan_valuu_dulieu_nhanhieu(q: str, db: Session = Depends(get_db)):
    nh_dulieu = du_lieu_ten(q)
    saved = []

    for nh in nh_dulieu:
        try:
            # Kiểm tra xem bản ghi đã tồn tại chưa
            stmt = select(Nhan).where(
                Nhan.maunhan == nh.maunhan,
                Nhan.nhanhieu == nh.nhanhieu,
                Nhan.nhom == nh.nhom,
                Nhan.status == nh.status,
                Nhan.ngaynopdon == nh.ngaynopdon,
                Nhan.sodon == nh.sodon,
                Nhan.chudon == nh.chudon,
                Nhan.daidienshcn == nh.daidienshcn
            )
            result = db.exec(stmt).first()
            
            if not result:
                db.add(nh)
                saved.append(nh)
        except Exception as e:
            print(f"Lỗi khi xử lý bản ghi: {e}")
            continue

    try:
        db.commit()
    except Exception as e:
        print(f"Lỗi khi lưu vào cơ sở dữ liệu: {e}")
        db.rollback()
        return []

    if not saved:
        try:
            # Sửa lại cách truy vấn để lấy tất cả bản ghi
            stmt = select(Nhan)
            results = db.exec(stmt).all()
            return results
        except Exception as e:
            print(f"Lỗi khi lấy tất cả bản ghi: {e}")
            return []

    return saved