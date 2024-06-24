# file_sharing_web_app

# Secure File Sharing System

This project is a secure file-sharing system built using the Django framework. It provides REST APIs for two types of users: Operation Users (Ops Users) and Client Users. Ops Users can upload files, and Client Users can sign up, verify their email, log in, list, and download files.


# Urls of the project  After runsever of the project

- Singnup : http://127.0.0.1:8000/api/singup/

- Login : http://127.0.0.1:8000/api/login/

- upload : http://127.0.0.1:8000/api/upload/

- files : http://127.0.0.1:8000/api/files/

- download : http://127.0.0.1:8000/api/download/1

## Features

- User registration and login with JWT authentication
- Email verification for client users
- Secure file upload (only for Ops Users)
- Secure file download with encrypted URLs (only for Client Users)
- Listing of uploaded files

## Requirements

- Python 3
- Django
- Django Rest Framework
- SimpleJWT for JWT Authentication
- Cryptography for encryption

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
