Requirements:
Python
Git

Setting up virtual environment:
python -m venv env
source env/Scripts/activate

Install:
git clone https://github.com/juniozguedes/cpf_validator.git
cd cpf_validator
cd cpf_validator
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python setup.py
python manage.py loaddata initial_cpf_data.json
python manage.py runserver

Usage:
