from typing import Any, Dict, List, Optional, Type, TypeVar
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.base_model import BaseDBModel

ModelType = TypeVar("ModelType", bound=BaseDBModel)

class DataManager:
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def create(self, db: Session, *, obj_in: Dict[str, Any]) -> ModelType:
        obj_in_data = dict(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all() 