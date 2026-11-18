from pydantic import BaseModel, Field, ConfigDict

class ServiceCreate(BaseModel):
    name: str=Field(min_length=2, max_length=100)
    price: int=Field(gt=0)
    duration_minutes: int=Field(gt=0)

class ServiceResponse(BaseModel):
    id: int=Field(gt=0)
    name: str=Field(min_length=2, max_length=100)
    price: int=Field(gt=0)
    duration_minutes: int=Field(gt=0)

    model_config = ConfigDict(from_attributes=True)