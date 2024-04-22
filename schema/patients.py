from pydantic import BaseModel
# import uuid

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone_no: str
    
class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone_no: str
    
    
    
patients = {
    1: Patient(id=1, name= "mrs abdul", age=50, sex="female", weight="80", height="5.9", phone_no= "+2347088676543"),
    2: Patient(id=2, name= "miss favour", age=20, sex="female", weight="52", height="6.0", phone_no= "+2348088676999"),
    3: Patient(id=3, name= "sir bello", age=45, sex="male", weight="73", height="5.3", phone_no= "+2348088676895"),
    4: Patient(id=4, name= "mama bissi", age=79, sex="female", weight="69", height="5.0", phone_no= "+2349016676999"),
}
    
