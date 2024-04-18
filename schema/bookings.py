from pydantic import BaseModel
from schema.doctors import Doctor, doctors

class Booking(BaseModel):
    id: int
    patient: str
    doctor: str
    date: int

class BookingCreate(BaseModel):
    patient: str
    doctor: str
    date: int
    
bookings: list[Booking] = [
    Booking(id=1, patient="mama bissi", doctor="Dr Alex", date=18/4/2024),
    Booking(),
    
]
