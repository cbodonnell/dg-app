from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from dg_backend import crud, schemas
from dg_backend.database import SessionLocal, engine
from dg_backend.models import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/rounds/", response_model=schemas.RoundInfoResponse)
def create_round_endpoint(round_info: schemas.RoundInfoCreate, db: Session = Depends(get_db)):
    return crud.create_round(db, round_info)

@app.get("/rounds/{round_id}", response_model=schemas.RoundInfoResponse)
def get_round_endpoint(round_id: int, db: Session = Depends(get_db)):
    round_db = crud.get_round(db, round_id)
    return crud.convert_info_response(round_db)

@app.put("/rounds/{round_id}", response_model=schemas.RoundInfoResponse)
def update_round_endpoint(round_id: int, round_info: schemas.RoundInfoUpdate, db: Session = Depends(get_db)):
    return crud.convert_info_response(crud.update_round(db, round_id, round_info))

@app.delete("/rounds/{round_id}", response_model=int)
def delete_round_endpoint(round_id: int, db: Session = Depends(get_db)):
    deleted_round_id = crud.delete_round(db, round_id)
    if deleted_round_id is None:
        raise HTTPException(status_code=404, detail="Round not found")
    return deleted_round_id
