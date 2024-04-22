from fastapi import APIRouter, HTTPException, Depends
from schema.patients import Patient, PatientCreate, patients
from services.patients import PatientServices


patient_router = APIRouter()

# CRUD
# create patients
# list patients
# update patients
# delete the patients

@patient_router.get("/")
def get_all():
    return patients

# create patients
@patient_router.post('/', status_code=201)
def create_patient(payload: PatientCreate, validated_patient: PatientCreate = Depends(PatientServices.validate_patient)):
    patient_id = len(patients) + 1
# create new-patient object
    new_patient = Patient(
        id= patient_id,
        name = payload.name,
        age= payload.age,
        sex= payload.sex,
        weight= payload.weight,
        height=payload.height,
        phone_no=payload.phone_no,
    )
    
    # store the new data to in memory of patients
    # print(new_patient)
    
    # patients.append(new_patient)
    patients[patient_id] = new_patient 
    
    return {"message": "patient created successfuly", 'data': new_patient}
    
    
            
# get single patient
@patient_router.get("/{patient_id}", status_code=200)
def get_patient(patient_id: int):

        patient = PatientServices.get_doctor_by_id(patient_id)
        
        if patient:
            return patient
        else:
            raise HTTPException(status_code=404, detail="Doctor not found.")



# update
@patient_router.put('/{patient_id}', status_code=200)
def update_patient(patient_id: int, payload: PatientCreate):
    try:
    # Check if the patient exists
        if patient_id not in patients:
            raise HTTPException(status_code=404, detail="Patient not found")
    
        # Update patient information
        curr_patient = patients[patient_id]
        curr_patient.name = payload.name
        curr_patient.age = payload.age
        curr_patient.sex = payload.sex

        return {"message": "Patient edited successfully", 'data': curr_patient}


    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e),)

# delete
@patient_router.delete('/{patient_id}', status_code=200)
def delete_patient(patient_id: int):
    # Check if the patient exists
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del patients[patient_id]
    

    return {"message": "Patient deleted successfully", 'data': patient_id}


