from pydantic import BaseModel

class Doctor(BaseModel):
    id:int
    name: str
    specialization: str
    phone_no: int
    is_avalible: bool
    
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone_no: int
    is_avalible: bool
    

doctors =  {
    0: Doctor(id=0, name="Dr Alex", specialization="Cardiologist", phone_no=+2349076543210, is_avalible= True ), 
    1: Doctor(id=1, name="Dr Onome", specialization="Pediatrician", phone_no=+2349076543210, is_avalible= False),
    2: Doctor(id=2, name="Dr Musa", specialization="Dermatologist", phone_no=+2349076543210, is_avalible= True),
    3: Doctor(id=3, name="Dr Ose", specialization="Neurologist", phone_no=+2349076543210, is_avalible= True),
    4: Doctor(id=4, name="Dr Uyi", specialization="Orthopedic Surgeon", phone_no=+2349076543210, is_avalible= False),
    }