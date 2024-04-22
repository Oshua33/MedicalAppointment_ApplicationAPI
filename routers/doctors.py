from fastapi import APIRouter, HTTPException, Depends
from schema.doctors import Doctor, DoctorCreate, doctors
from services.doctors import DoctorServices


doctor_router = APIRouter()


# CRUD
# create patients
# list patients
# update patients
# delete the patients

@doctor_router.get("/")
def get_all():
    return doctors

# create doctor
@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate, validate_doctor:DoctorCreate = Depends(DoctorServices.validate_doctor) ):
        doctor_id = len(doctors) + 1
        new_doctor = Doctor(
            id=doctor_id,
            name=payload.name,
            specialization=payload.specialization,
            phone_no=payload.phone_no,
            is_avalible=payload.is_avalible,
        )
        # doctors.append(new_doctor) --- list for list db
        # for dict db
        doctors[doctor_id] = new_doctor
        
        return {"message": "doctor created successfully", 'data': new_doctor}

# get single doctor
@doctor_router.get("/{doctor_id}", status_code=200)
def get_doctor(doctor_id: int):

        doctor = DoctorServices.get_doctor_by_id(doctor_id)
        
        if doctor:
            return doctor
        else:
            raise HTTPException(
                status_code=404,
                detail="Doctor not found."
            )

#  update
# @doctor_router.put('/{doctor_id}', status_code=200)
# def update_doctor(doctor_id: int, payload: DoctorCreate):
#     # Check if the doctor exists
#     if doctor_id not in doctors:
#         raise HTTPException(status_code=404, detail="Doctor not found")
    
#     # Update patient information
#     curr_doctor = doctors[doctor_id]
#     curr_doctor.name = payload.name
#     curr_doctor.specialization = payload.specialization
#     curr_doctor.is_avalible = payload.is_avalible

#     return {"message": "Doctor edited successfully", 'data': curr_doctor}


@doctor_router.put("/{doctor_id}/availability", response_model=Doctor)
def update_doctor_availability(doctor_id: int, is_available: bool):

        DoctorServices.set_doctor_availability(doctor_id, is_available)
        
        return DoctorServices.get_doctor_by_id(doctor_id)



# # delete
@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(doctor_id:int):
    
    doctor = DoctorServices.get_doctor_by_id(doctor_id)
    
    # Check if the doctor exists
    # if doctor_id not in doctors:
    #     raise HTTPException(status_code=404, detail="Doctors not found")
    
    if doctor:
        doctors.remove(doctor)
        return {"message": "Doctor deleted successfully"}
        
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")
