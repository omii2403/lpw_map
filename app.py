import flask
import json
from flask import request
# import pymongo

app = flask.Flask(__name__)


@app.route('/regitserPatient', methods = ['POST'])
def register_patient():
    patient_data = request.json
    with open("patient_data.json", "r+") as file:
        data = json.load(file)
        data.append(patient_data)

@app.route('/getPatientData', methods = ['GET'])
def get_patient_data():
    with open("patient_data.json", "r") as file:
        data = json.load(file)
        return data

@app.route('/registerDoctor', methods = ['POST'])
def register_doctor():
    doctor_data = request.json
    with open("doctor_data.json", "r+") as file:
        data = json.load(file)
        data.append(doctor_data)

@app.route('/getDoctorData', methods = ['GET'])
def get_doctor_data():
    with open("doctor_data.json", "r") as file:
        data = json.load(file)
        return data

@app.route('/loginPatient', methods = ['POST'])
def login_patient():
    patient_data = request.json
    with open("patient_data.json", "r") as file:
        data = json.load(file)
        for patient in data:
            if patient['username'] == patient_data['username'] and patient['password'] == patient_data:
                return patient
            

@app.route('/loginDoctor', methods = ['POST'])
def login_doctor():
    patient_data = request.json
    with open("doctor_data.json", "r") as file:
        data = json.load(file)
        for patient in data:
            if patient['username'] == patient_data['username'] and patient['password'] == patient_data:
                return patient


#Write a function for patient appointment
@app.route('/patientAppointment', methods = ['POST'])
def patient_appointment():
    data = request.json
    with open("appointment_data.json", "r+") as file:
        data = json.load(file)
        data.append(data)

if __name__ == "__main__":
    app.run()
