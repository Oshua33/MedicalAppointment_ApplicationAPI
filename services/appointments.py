


# class BookingServices:
    
#     @staticmethod 
#     def check_availability(payload: BookingCreate):
#         #get doctor_id from Doctor class
#         doctor_id = payload.doctor_id

#         # Finding the doctor in the doctors dictionary
#         doctor = doctors.get(doctor_id)

#         # Checking if the doctor exists
#         if not doctor:
#             raise HTTPException(status_code=400, detail="Doctor not found")

#         # Checking if the doctor is available
#         if not doctor.is_avalible:
#             raise HTTPException(status_code=400, detail="Doctor not available")

#         return payload
    
#     # check if a patient exist 1. 
#     # if user role is patient success
#     # # if found go nd make booking
#     # include user to dis and d role.
#     # @staticmethod
#     # def book_appointment(payload: BookingCreate):
#     #     patient_id = patients[id]
#     #     patient_name = patients[patient_id].name
#     #     for patient_id, patient_name in patients.items():
#     #         if  patient_id != payload.patient_id:
#     #             raise HTTPException(status_code=400, detail="Patient not found")
            
#     #         elif patient_id == payload.patient_id:
#     #             return {"message": f"{patient_name} proceed to book your appointment"}
            
        
        
#     # @staticmethod
#     # def check_patient_role(user_id:int):
#     #     # user_id = payload.user_id
#     #     # Assuming 'users' is a dictionary mapping user IDs to User objects
#     #     user = users.get(user_id)
#     #     if not user:
#     #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     #     if user['role'] != 'patient':
#     #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments")
#     #     return user

# # def check_patient(user_id: int = Depends()):
# #     user = users.get(user_id)
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
# #     if user.role != 'patient':
# #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can create bookings")
# #     return user
    
#     # @staticmethod
#     # def check_availability(payload:BookingCreate):
#     #     # doctor_id = client input id
#     #     doctor_ids = payload.doctor_id
#     #     # interate doctor ids
#     #     for doctor_id in doctor_ids:
#     #         doctor: Doctor = doctors[get(int(doctor_id)]
#     #         if doctor[]
    
#     # @staticmethod 
#     # def check_avaliblity(payload: BookingCreate ):
#     #     for doctor in doctors.values():
#     #         if doctor.is_avalible == True:
#     #             raise HTTPException(status_code=400, detail="Doctor not avaiable")
#     #         return payload
    
    
#     #  @staticmethod
#     # def check_availability(payload: OrderCreate):
#     #     product_ids = payload.items
#     #     for product_id in product_ids:
#     #         product: Product = products.get(int(product_id))
#     #         if product.quantity_available < 1:
#     #             logger.warning(Product is no more available")
#     #             raise HTTPException(status_code=400, detail='Product is unavailable')
#     #         product.quantity_available -= 1
#     #     return payload



from datetime import datetime
from typing import Optional
# from logger import logger

from fastapi import HTTPException, status
from schema.appointments import  Appointment, appointments
from schema.patients import Patient
from schema.doctors import Doctor,doctors
from services.doctors import DoctorServices


class AppointmentService:
    
    @staticmethod
    def create_appointment(patient: Patient, doctor: Doctor, date: datetime) -> Appointment:
            
            if not doctor.is_avalible:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="The doctor is not available for appointments.",
                )

            existing_appointment = AppointmentService.get_existing_appointment(patient.id)
            if existing_appointment:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"You already have an appointment with a doctor. "
                        "If you want to make a new appointment, please cancel the existing one first."
                )
            
            appointment_id = len(appointments) + 1
            new_appointment = Appointment(
                id=appointment_id,
                patient=patient,
                doctor=doctor,
                date=date,
                is_completed=False
            )
            
            DoctorServices.set_doctor_availability(doctor.id, False)
            appointments.append(new_appointment)
            return new_appointment
        
    
    @staticmethod
    def get_appointment_by_id(appointment_id: int) -> Optional[Appointment]:
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment
        return None
    


    @staticmethod
    def update_appointment(appointment: Appointment) -> Appointment:
        try:
            appointment_index = next((index for index, app in enumerate(appointments) if app.id == appointment.id), None)
            if appointment_index is not None:
                appointments[appointment_index] = appointment
                return appointment
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Appointment not found.",
                )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while updating the appointment.",
            )
        

    @staticmethod
    def get_existing_appointment(patient_id: int) -> Optional[Appointment]:
        for appointment in appointments:
            if appointment.patient.id == patient_id and not appointment.is_completed:
                return appointment
        return None
    
    

    