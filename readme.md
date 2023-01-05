
python -m venv venv

source venv/bin/activate

pip install bs4

pip freeze > requirements.txt

pip install -r requirements.txt