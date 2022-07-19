# django-graphql
Learning basics of api developments with django, django-graphene and graphql
# installation steps:
- install virtual environment on your pc with
```
pip install -m virtualenv
```
- clone this project on your pc with
```
git clone https://github.com/aayobam/django-graphql
```
- browse to the cloned project director or open with your favourite text IDE (EG VSCODE)
```
cd django-graphql
```
- create a virtual environment where all the project packages/dependencies will be installed/isolated
```
virtualenv venv
```
- activate your newly created virtualenv (venv) on linux OS with
```
source venv/bin/activate
```
- activate your newly created virtualenv (venv) on windows OS with
```
venv/Scripts/activate
```
- install all dependencies/packages from the requirements.txt file with
```
pip install -r requirements.txt
```
- makemigrations  and migrate your database with
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- load the default data in data.json into your database with the below command. you can decide not to load and create manually from the admin or from your create endpoint.
```
python manage.py loaddata data.json
```
