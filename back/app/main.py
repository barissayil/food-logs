from fastapi import FastAPI, Query

from app.dependencies import database
from app.crud import crud
from app.schemas import schemas

app = FastAPI()

@app.on_event("startup")
def startup():
    database.connect()

@app.on_event("shutdown")
def shutdown():
    database.disconnect()

@app.post("/logs/", response_model=schemas.FoodLog)
def create_log(log: schemas.FoodLogCreate):
    return crud.create_log(log=log)

@app.get("/logs/", response_model=list[schemas.FoodLog])
def read_logs(skip: int = 0, limit: int = 10):
    return crud.get_logs(skip=skip, limit=limit)

@app.delete("/logs/{log_id}", response_model=schemas.FoodLog)
def delete_log(log_id: int):
    return crud.delete_log(log_id=log_id)

@app.get("/logs/summary", response_model=list[schemas.CaloriesSummary])
def get_calories_summary_by_date():
    return crud.get_calories_summary_by_date()

@app.get("/logs/search", response_model=list[schemas.FoodLog])
def search_food(name_pattern: str = Query(...)):
    return crud.search_food_by_name(pattern=name_pattern)
