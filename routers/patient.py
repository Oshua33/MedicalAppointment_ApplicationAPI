from fastapi import APIRouter
from schema.patients import Patient, PatientCreate, patients
patient_router = APIRouter()

# CRUD

@patient_router.get("/")
def get_all():
    return patients

