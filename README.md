# Healthcare Management System

A full-stack web application for managing patients, doctors, and patient-doctor assignments. Built with Django + Django REST Framework backend, vanilla JavaScript frontend, PostgreSQL database, and JWT authentication.

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Django 5.2, Django REST Framework |
| Auth       | JWT (djangorestframework-simplejwt)|
| Database   | PostgreSQL                        |
| Frontend   | Django Templates, Vanilla JS, CSS |
| Environment| python-decouple (.env)            |

---

## Features

- User registration and login with JWT tokens
- Full CRUD for patients (scoped to the logged-in user)
- Full CRUD for doctors (visible to all authenticated users)
- Assign/unassign doctors to patients (many-to-many mappings)
- Dashboard with live stats (patient/doctor/mapping counts)
- Responsive UI with modals, tables, and navigation
- Token-based API authentication with auto-redirect on session expiry

---

## Setup Instructions

### 1. Clone and create virtual environment

```bash
cd "Health Care"
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up PostgreSQL

Create the database:

```sql
CREATE DATABASE healthcare_db;
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations and start

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## API Endpoints

### Authentication (Public)

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| POST   | `/api/auth/register/` | Register a new user      |
| POST   | `/api/auth/login/`    | Login and get JWT tokens |

### Patients (Requires JWT)

| Method | Endpoint              | Description                             |
|--------|-----------------------|-----------------------------------------|
| GET    | `/api/patients/`      | List all patients (created by user)     |
| POST   | `/api/patients/`      | Add a new patient                       |
| GET    | `/api/patients/<id>/` | Get a specific patient                  |
| PUT    | `/api/patients/<id>/` | Update patient details                  |
| DELETE | `/api/patients/<id>/` | Delete a patient                        |

### Doctors (Requires JWT)

| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| GET    | `/api/doctors/`      | List all doctors        |
| POST   | `/api/doctors/`      | Add a new doctor        |
| GET    | `/api/doctors/<id>/` | Get a specific doctor   |
| PUT    | `/api/doctors/<id>/` | Update doctor details   |
| DELETE | `/api/doctors/<id>/` | Delete a doctor         |

### Mappings (Requires JWT)

| Method | Endpoint                      | Description                  |
|--------|-------------------------------|------------------------------|
| GET    | `/api/mappings/`              | List all assignments         |
| POST   | `/api/mappings/`              | Assign doctor to patient     |
| GET    | `/api/mappings/<patient_id>/` | Get doctors for a patient    |
| DELETE | `/api/mappings/delete/<id>/`  | Remove an assignment         |

Include `Authorization: Bearer <access_token>` header for all protected endpoints.

---

## Frontend Pages

| URL          | Page              | Description                                   |
|--------------|-------------------|-----------------------------------------------|
| `/`          | Home              | Redirects to login                            |
| `/register/` | Register          | Create a new account                          |
| `/login/`    | Login             | Sign in with email & password                 |
| `/dashboard/`| Dashboard         | Stats overview + quick action cards           |
| `/patients/` | Patients          | Add, edit, delete patients (table + modal)    |
| `/doctors/`  | Doctors           | Add, edit, delete doctors (table + modal)     |
| `/mappings/` | Mappings          | Assign/remove doctor-patient relationships    |

---

## Project Structure

```
Health Care/
├── healthcare/          # Project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/            # User registration & JWT login
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── patients/            # Patient CRUD API
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── doctors/             # Doctor CRUD API
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── mappings/            # Patient-Doctor assignment API
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── frontend/            # Web UI (templates + static files)
│   ├── views.py
│   ├── urls.py
│   ├── templates/frontend/
│   │   ├── base.html
│   │   ├── app_base.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── patients.html
│   │   ├── doctors.html
│   │   └── mappings.html
│   └── static/frontend/
│       ├── css/style.css
│       └── js/app.js
├── .env
├── requirements.txt
├── manage.py
└── README.md
```
