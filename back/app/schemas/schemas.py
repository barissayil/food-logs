from pydantic import BaseModel
from datetime import date

class FoodLogCreate(BaseModel):
    date: date
    name: str
    calories: int

class FoodLog(FoodLogCreate):
    id: int

    class Config:
        from_attributes = True

class CaloriesSummary(BaseModel):
    date: date
    total_calories: int
    avg_calories: float