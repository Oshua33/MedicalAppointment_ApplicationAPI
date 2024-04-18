from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone_no: int
    
class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone_no: int
    
    
    
patients = {
    0: Patient(id=0, name= "mr jerry", age=70, sex="male", weight="5.4cm", height="5.2ft", phone_no= +2348088222999),
    1: Patient(id=1, name= "mrs abdul", age=50, sex="female", weight="5.6cm", height="5.0ft", phone_no= +2347088676543),
    2: Patient(id=2, name= "miss favour", age=20, sex="female", weight="5.2cm", height="5.2ft", phone_no= +2348088676999),
    3: Patient(id=3, name= "sir bello", age=45, sex="male", weight="5.7cm", height="5.8ft", phone_no= +2348088676895),
    4: Patient(id=4, name= "mama bissi", age=20, sex="female", weight="5.2cm", height="5.2ft", phone_no= +2349016676999),
      
}
    
