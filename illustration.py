#  medical appointment application.

# patient
# doctors
# appointments


# patient - id, name, age, sex, weight, height, phone
# doctors - id, name, specialization, phone, is_available (defaults to True)
# appointments -   id, patient(name or id), doctor(doc name or id), date


# description
# patient can book appointments, one patient to a docutor at a time
#  status code if doctor is avalible. -- check for avalibilty, with pending or avalible status
#  checkings
# 1. if the doc is avalible, if avalible - TRUE, else if not FALSE
# 2. wen booking appointment, check if patients exixt
# 3. wen booking, check if the patient exist, and if doctor exist. and is avalible

# so it the appointments dat will have service of avaliblity or dependency of avali.

# start with schema of patient class, patientcreate class, dummy db of listof patient object(3)
# 2.Doctor schema of Doctor class, DoctorCreate class, dummy db.(set the tp) -- i can use dict= {chap1: doc 1, chap2: doc2 } - using key and values
# 3. appointment schema, appot class, appointCreate class, dummy db.

# 1. start routers
# starts patients routers-
#   define ur imports, check ur CRUD endpoints(create, list, update, delete.)

# list ==== list var = ['chap 1', 'chap 2'] 
# to access {} - dict ===  print(dict[chap1]), note we use .get('chap1') to throw None wen the value is not found. == dict.get('chap3', 'not found')

# check if a doctor is avalible --- dependecy in doctor service.

# @booking_router.post('/', status_code=201) #
# def create_booking(payload: BookingCreate, check_availability: BookingCreate = Depends(BookingServices.check_availability)):
#     booking_id = len(bookings) + 1
#     new_booking = Booking(
#         id=booking_id,
#         patient_id= payload.patient_id,
#         doctor_id= payload.doctor_id,
#         date=payload.date
#     )
    
#     return {"message": "Booking created succesffuly", 'data': new_booking}


# from fastapi import HTTPException
# from schema.doctors import doctors
# from schema.bookings import BookingCreate

# class BookingServices:
#     #  check_availability: BookingCreate = Depends(BookingServices.check_availability)
#     @staticmethod
#     def check_availability(payload: BookingCreate ):
#         for doctor in doctors.values():
#             if doctor.is_avalible == False:
#                 raise HTTPException(status_code=400, detail="Doctor not avaiable")
#             return payload

# what left 
# update and delete for patient, doctors, bookings,
# wen doctore is created and book does it change to not avalible.

# user model
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    role: str

users = {}


# patient post end point
@patient_router.post('/', status_code=201)
def create_patient(payload: PatientCreate, validated_patient: PatientCreate = Depends(PatientServices.validate_patient)):
    patient_id = len(patients) + 1
    new_patient = Patient(
        id=patient_id,
        name=payload.name,
        age=payload.age,
        sex=payload.sex,
        weight=payload.weight,
        height=payload.height,
        phone_no=payload.phone_no,
    )
    patients[patient_id] = new_patient
    # Create a user for the patient
    users[patient_id] = User(id=patient_id, name=payload.name, role="patient")
    return {"message": "Patient created successfully", 'data': new_patient}

@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate, validated_doctor: DoctorCreate = Depends(DoctorServices.validate_doctor)):
    doctor_id = len(doctors) + 1
    new_doctor = Doctor(
        id=doctor_id,
        name=payload.name,
        specialization=payload.specialization,
        phone_no=payload.phone_no,
        is_avalible=payload.is_avalible,
    )
    doctors[doctor_id] = new_doctor
    # Create a user for the doctor
    users[doctor_id] = User(id=doctor_id, name=payload.name, role="doctor")
    return {"message": "Doctor created successfully", 'data': new_doctor}


# dependency
from fastapi import Depends, HTTPException, status
from .models import User, BookingCreate

class BookingServices:
    @staticmethod
    def check_patient_role(payload: BookingCreate):
        user_id = payload.user_id
        # Assuming 'users' is a dictionary mapping user IDs to User objects
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if user['role'] != 'patient':
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments")
        return user


# @booking_router.post('/', status_code=201)
def create_booking(
    payload: BookingCreate,
    user: dict = Depends(BookingServices.check_patient_role),
    check_availability: BookingCreate = Depends(BookingServices.check_availability)
):
    # Your booking creation logic here
    return {"message": "Booking created successfully", 'data': new_booking}


# so now create users in main.py 
# create user model for them. with roles
# create depency.
# link it to patient post endpoint
