from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.services import ServiceCreate, ServiceResponse
from app.models.service import Service

router = APIRouter(
    prefix="/services",
    tags=["services"],
)

@router.get("/", response_model=list[ServiceResponse])
def prikazi_usluge(db: Session = Depends(get_db)):
    usluge=db.query(Service).all()
    return usluge


@router.post("/", status_code=201, response_model=ServiceResponse)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    nova_usluga = Service(
        name=service.name,
        price=service.price,
        duration_minutes=service.duration_minutes
    )

    db.add(nova_usluga)
    db.commit()
    db.refresh(nova_usluga)
    return nova_usluga

@router.put("/{id}", response_model=ServiceResponse)
def update_service(id: int, service: ServiceCreate, db: Session = Depends(get_db)):
    usluga=db.query(Service).filter(Service.id == id).first()
    if usluga is None:
        raise HTTPException(status_code=404, detail="Service not found")

    usluga.name=service.name
    usluga.price=service.price
    usluga.duration_minutes=service.duration_minutes

    db.commit()
    db.refresh(usluga)
    return usluga

@router.delete("/{id}")
def delete_service(id: int, db: Session = Depends(get_db)):
    usluga=db.query(Service).filter(Service.id == id).first()
    if usluga is None:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(usluga)
    db.commit()
    return {"message":"Service deleted successfully"}
