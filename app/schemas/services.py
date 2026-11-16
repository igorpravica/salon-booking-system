from pydantic import BaseModel, Field

class ServiceCreate(BaseModel):
    name: str=Field(min_length=2, max_length=100)
    price: int=Field(gt=0)
    duration_minutes: int=Field(gt=0)