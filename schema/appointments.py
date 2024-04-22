

# class Booking(BaseModel):
#     id: int
#     patient_id: Patient
#     doctor_id: Doctor
#     date: datetime
#     is_completed: bool = False
    

# class BookingComplete(BaseModel):
#     id: int
#     patient: Patient
#     doctor_id: Doctor
#     date: datetime
#     is_completed: bool = False 
    
# class BookingCreate(BaseModel):
#     patient_id: int
    
# bookings: list[Booking] = []
    
    
    

    
# # bookings: list[Booking] = [
# #     Booking(id=1, patient_id=1, doctor_id=1, date="2024-04-18"),
# #     Booking(id=2, patient_id=2, doctor_id=2, date="2024-04-20"),
# #     Booking(id=3, patient_id=3, doctor_id=3, date="2024-04-22"),
# #     Booking(id=4, patient_id=4, doctor_id=4, date="2024-04-25"),    
# # ]



from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

from schema.doctors import Doctor
from schema.patients import PatientCreate, Patient


class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    date: datetime
    is_completed: bool = False 


class AppointmentComplete(BaseModel):
    id: int
    patient: PatientCreate
    doctor: Doctor
    date: datetime
    is_completed: bool = False 


class AppointmentCreate(BaseModel):
    patient_id: int

class CompletedAppointmentResponse(BaseModel):
    id: int
    patient_id: int
    patient_username: str
    patient_name: str
    patient_phone_number: str
    doctor: Dict
    date: datetime
    is_completed: bool
    message: str


appointments: list[Appointment] = []
