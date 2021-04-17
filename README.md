## Requirements:

Python
Git

## Setting up virtual environment:

`python -m venv env`
`source env/Scripts/activate`

## Install:

git clone https://github.com/juniozguedes/cpf_validator.git
cd cpf_validator
cd cpf_validator
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python setup.py
python manage.py loaddata initial_cpf_data.json
python manage.py runserver

## Usage:

    1 . Register user at: http://localhost:8000/account/register
    with body: {
    "username": "user",
    "email": "user@gmail.com",
    "password": "123456"
    }

    2 . Login and get access token at: http://localhost:8000/api/token/
    with body: {
    "username": "user",
    "email": "user@gmail.com",
    "password": "123456"
    }

    3. Paste the access token in the Authorization Header of desired route as:
        Bearer #TOKEN_NAME
        example: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

## Routes:

## Get DENY cpf list

( Retrieve denied list )
GET http://127.0.0.1:8000/cpf/denied;

## Get all cpf's

(List all cpf's in the database)
GET http://127.0.0.1:8000/cpf/list;

## Create CPF

( Create cpf if it's not denied or existing, status can be either ALLOW or DENY )
POST http://127.0.0.1:8000/cpf/create; Body: {
"number":"##.##.##.##",
"status": "ALLOW"
}

## Delete CPF

( Delete cpf )
DELETE http://127.0.0.1:8000/cpf/details; Body: {
"number":"##.##.##.##"
}

## Get single CPF

( Retrieve single document )
GET http://127.0.0.1:8000/cpf/details; Body: {
"number":"##.##.##.##"
}

## Considerations:

Numbers are being sent in the body JSON so it can be validated correctly with cpf.py file
You could send either ##.##.##.## OR ##,##,##/## OR ##-##-##-##
It accepts all regex if the numbers are valid cpf numbers.

Developed by https://github.com/juniozguedes/
