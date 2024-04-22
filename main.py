from fastapi import FastAPI

from routers.patient import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(router=patient_router, prefix="/patients", tags=["Patients"])
app.include_router(router=doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(router=appointment_router, prefix="/Appointments", tags=['Appointments'])



@app.get('/')
def index():
    return "welcome, please book your appointment"
