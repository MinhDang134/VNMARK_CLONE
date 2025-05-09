from typing import TypeVar, Generic, Type, List, Optional
from sqlmodel import SQLModel, Session, select

ModelType = TypeVar("ModelType", bound=SQLModel)

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session) -> List[ModelType]:
        return db.exec(select(self.model)).all()

    def get_existing(self, db: Session, **kwargs) -> Optional[ModelType]:
        stmt = select(self.model).filter_by(**kwargs)
        return db.exec(stmt).first()

    def create_if_not_exists(self, db: Session, obj_data: ModelType, unique_fields: List[str]) -> Optional[ModelType]:
        filter_kwargs = {field: getattr(obj_data, field) for field in unique_fields}
        existing = self.get_existing(db, **filter_kwargs)
        if not existing:
            db.add(obj_data)
            return obj_data
        return None

    def save_changes(self, db: Session):
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
