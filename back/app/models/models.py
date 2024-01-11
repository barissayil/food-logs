from sqlalchemy import Column, Integer, String, Date
from app.dependencies.database import Base

class FoodLog(Base):
    __tablename__ = "food_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    name = Column(String)
    calories = Column(Integer)
