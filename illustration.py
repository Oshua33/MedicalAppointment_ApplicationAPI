#  medical appointment application.
 
# patient
# doctors
# appointments


# patient - id, name, age, sex, weight, height, phone
# doctors - id, name, specialization, phone, is_available (defaults to True)
# appointments -   id, patient, doctor, date


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