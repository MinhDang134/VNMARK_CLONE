from sqlalchemy import Table
from  datetime import datetime
from sqlmodel import SQLModel,Field
from typing import Optional

class Nhan(SQLModel, table = True):
    __tablename__ = 'nhan_hieu'
    id: Optional[int] = Field(default=None,primary_key=True)
    maunhan : str
    nhanhieu : str
    nhom : str
    status : Optional[str] = Field(default=None)
    ngaynopdon : Optional[datetime] = Field(default=None)
    sodon : str
    chudon : str
    daidienshcn : str

