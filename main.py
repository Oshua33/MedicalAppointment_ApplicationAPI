from fastapi import FastAPI

from routers.patient import patient_router

app = FastAPI()

app.include_router(router=patient_router, prefix="/patients", tags=["Patients"])

@app.get('/')
def index():
    return "welcome, please book your appointment"
