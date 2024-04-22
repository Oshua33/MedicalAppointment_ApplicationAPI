from typing import Optional
from fastapi import HTTPException,status
from schema.patients import PatientCreate, patients


# class PatientServices:
    
    
#     @staticmethod
#     def validate_patient(payload: PatientCreate):
#         patient_id: int = payload.id
#         for patient in patients:
#             # patient: Patient = patients.get(int(patient_id))
#             if patient.id == patient_id:
#                 raise HTTPException(status_code=400, detail="patient name already exist")
#             return payload
        
    
class PatientServices:
    
    @staticmethod
    def validate_patient(payload: PatientCreate):
        # name:str = payload.name
        for patient_id, patient_info in patients.items():
            if patient_info.name == payload.name:
                raise HTTPException(status_code=400, detail="patient name already exist")
            return payload
        
        
    @staticmethod 
    def get_patient_from_id(patient_id: int) -> Optional[PatientCreate]:
        get_patient = None
        for patient in patients:
            if patient.id == patient_id:
                get_patient = patient
            break

        if get_patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
                )
        return get_patient
                
