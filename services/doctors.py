from typing import Optional
from fastapi import HTTPException, status

from schema.doctors import Doctor, DoctorCreate, doctors

class DoctorServices:
    
    @staticmethod
    def validate_doctor(payload: DoctorCreate):
        # to interate thru a turple in dict, use key nd values 
        for doctor_id, doctor_info in doctors.items():
            if doctor_info.name == payload.name and doctor_info.specialization == payload.specialization:
                raise HTTPException(status_code=400, detail="Doctor name and specialization already exist")
            elif doctor_info.specialization == payload.specialization:
                raise HTTPException(status_code=400, detail="Doctor specialization already exists with a different name")
        return payload
    
    
    @staticmethod
    def available_doctor() -> Optional[Doctor]:
        for doctor_id,doctor_info in doctors.items():
            if doctor_info.is_avalible:
                return doctor_info
        return None
    
    
    @staticmethod
    def set_doctor_availability(doctor_id: int, is_available: bool) -> None:
            
            for doctor_id, doctor_info in doctors.items():
                if doctor_info:              
                    doctor_info.is_avalible = is_available
                else:
                    raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="Doctor not found."
                        )

    
    @staticmethod
    def make_doctor_available(doctor_id: int) -> None:
            
            for doctor_id, doctor_info in doctors.items():
                if doctor_info :              
                    doctor_info.is_avalible = True
                else:
                    raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="Doctor not found."
                        )

    @staticmethod
    def get_doctor_by_id(doctor_id: int) -> Optional[Doctor]:
        for doctor_id, doctor_info in doctors.items():
            if doctor_info.id == doctor_id:
                return doctor_info
        return None
