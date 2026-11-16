from fastapi import APIRouter
from app.schemas.services import ServiceCreate

router = APIRouter(
    prefix="/services",
    tags=["services"],
)

@router.get("/")
def prikazi_usluge():
    return []

@router.post("/", status_code=201)
def create_service(service: ServiceCreate):
    return service