<img src='Dummy_data/screenshot.png'>

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 3000 # for runserver
