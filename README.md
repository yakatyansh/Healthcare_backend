# Healthcare Backend API

A backend healthcare management system built using Django, Django REST Framework (DRF), PostgreSQL, and JWT Authentication.

This project was developed as part of a Backend Engineer Intern assignment.

---

# Features

* User Registration and Login
* JWT Authentication
* Patient Management APIs
* Doctor Management APIs
* Patient-Doctor Mapping APIs
* PostgreSQL Database Integration
* Protected Routes using JWT
* Django ORM-based database modeling
* Modular Django App Structure

---

# Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* PostgreSQL
* Simple JWT Authentication
* pgAdmin 4
* Postman

---

# Project Structure

```txt
healthcare_backend/
│
├── config/
├── authentication/
├── patients/
├── doctors/
├── mappings/
├── manage.py
├── requirements.txt
└── .env
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <repository_url>
cd healthcare_backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

## Create Database

Open PostgreSQL shell:

```bash
psql postgres
```

Create database:

```sql
CREATE DATABASE healthcare_db;
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```env
DB_NAME=healthcare_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

---

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Server

```bash
python manage.py runserver
```

Server will start at:

```txt
http://127.0.0.1:8000/
```

---

# Authentication

JWT Authentication is implemented using `djangorestframework-simplejwt`.

Protected endpoints require:

```txt
Authorization: Bearer <access_token>
```

---

# API Endpoints

# Authentication APIs

## Register User

### POST

```txt
/api/auth/register/
```

Request Body:

```json
{
    "username": "yash",
    "email": "yash@gmail.com",
    "password": "1234"
}
```

---

## Login User

### POST

```txt
/api/auth/login/
```

Request Body:

```json
{
    "username": "yash",
    "password": "1234"
}
```

Response:

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

---

# Patient APIs

## Create Patient

### POST

```txt
/api/patients/
```

Request Body:

```json
{
    "name": "Rahul",
    "age": 25,
    "disease": "Fever"
}
```

---

## Get All Patients

### GET

```txt
/api/patients/
```

---

## Get Single Patient

### GET

```txt
/api/patients/<id>/
```

---

## Update Patient

### PUT

```txt
/api/patients/<id>/
```

---

## Delete Patient

### DELETE

```txt
/api/patients/<id>/
```

---

# Doctor APIs

## Create Doctor

### POST

```txt
/api/doctors/
```

Request Body:

```json
{
    "name": "Dr Sharma",
    "specialization": "Cardiology",
    "experience": 10
}
```

---

## Get All Doctors

### GET

```txt
/api/doctors/
```

---

## Get Single Doctor

### GET

```txt
/api/doctors/<id>/
```

---

## Update Doctor

### PUT

```txt
/api/doctors/<id>/
```

---

## Delete Doctor

### DELETE

```txt
/api/doctors/<id>/
```

---

# Mapping APIs

## Assign Doctor To Patient

### POST

```txt
/api/mappings/
```

Request Body:

```json
{
    "patient": 1,
    "doctor": 1
}
```

---

## Get All Mappings

### GET

```txt
/api/mappings/
```

---

## Get Doctors Assigned To A Patient

### GET

```txt
/api/mappings/patient/<patient_id>/
```

---

## Remove Mapping

### DELETE

```txt
/api/mappings/<id>/
```

---

# Database Models

## Patient

* user
* name
* age
* disease

## Doctor

* name
* specialization
* experience

## PatientDoctorMapping

* patient
* doctor

---

# Security Features

* JWT Authentication
* Protected APIs using `IsAuthenticated`
* User-specific patient access
* Environment variable-based configuration

---

# Testing

All APIs were tested using:

* Postman
* DRF Browsable API
* pgAdmin 4

---

# Future Improvements

* Role-based access control
* Separate doctor/patient authentication
* API documentation using Swagger
* Docker support
* Pagination and filtering
* Deployment support

---

# Author

Yash Katyan
