from sqlalchemy import func

from app.dependencies.database import get_db
from app.models.models import FoodLog
from app.schemas.schemas import FoodLogCreate

db = get_db()

def create_log(log: FoodLogCreate):
    db_log = FoodLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_logs(skip: int = 0, limit: int = 10):
    return db.query(FoodLog).offset(skip).limit(limit).all()

def delete_log(log_id: int):
    db_log = db.query(FoodLog).filter(FoodLog.id == log_id).first()
    db.delete(db_log)
    db.commit()
    return db_log

def get_calories_summary_by_date():
    return db.query(FoodLog.date, func.sum(FoodLog.calories).label('total_calories'), func.avg(FoodLog.calories).label('avg_calories')).group_by(FoodLog.date).all()
    
def search_food_by_name(pattern: str):
    return db.query(FoodLog).filter(FoodLog.name.op('~')(pattern)).all()
