from enum import Enum


class TrangThaiEnum(str, Enum):
    dang_giai_quyet = "Đang giải quyết "
    cap_bang = "cấp bằng"
    tu_choi = "từ chối"
    rut_don = "rút đơn"

class LoaiDonEnum(str,Enum):
    don_quoc_te = "Đơn quốc tế "
    don_quoc_gia = "Đơn quốc gia "
