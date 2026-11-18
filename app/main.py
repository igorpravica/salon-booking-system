from fastapi import FastAPI
from app.routers import services
from app.database import Base, engine
from app.models.service import Service

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Salon booking system",
    description="Backend API for hair salon appointment booking",
    version="1.0.0"
)
app.include_router(services.router)

@app.get("/")
def pocetna():
    return {"poruka: Dobrodosli u Salon Booking System API!"}

@app.get("/health")
def health():
    return {"status": "ok"}

