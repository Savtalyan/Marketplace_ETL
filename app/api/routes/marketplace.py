from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.models.data_models import Marketplace
from app.api.dependencies import get_db


router = APIRouter() 


@router.get("/marketplaces", response_model=Marketplace)
def get_marketplaces(db : Session = Depends(get_db)):
    return db.exec(select(Marketplace)).all() 


@router.get("/marketplace/{marketplace_id}", response_model=List[Marketplace])
def get_markeplace(marketplace_id : int , db : Session = Depends(get_db)):
    marketplace = db.exec(select(Marketplace).where(Marketplace.id == marketplace_id)).first()

    if not marketplace:
        return HTTPException(404, "Marketplace not found")
    
    return marketplace


@router.post("/marketplace", response_model=Marketplace)
def create_marketplace(marketplace : Marketplace, db : Session = Depends(get_db)):
    db.add(marketplace)
    db.commit() 
    db.refresh(marketplace)
    return marketplace


