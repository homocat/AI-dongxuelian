from pydantic import BaseModel

class HealthSchema(BaseModel):
    height: float
    weight: float
    blood_pressure: str
    heart_rate: int