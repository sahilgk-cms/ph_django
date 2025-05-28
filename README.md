
# PH-EBS using Django demo testing

Trying to display all the articles from PH_EBS MongoDB database.

## Folder structure
```
ph_django
├── ph
│  ├── migrations
│  │  ├── __pycache__
│  │  │  └── __init__.cpython-312.pyc
│  │  └── __init__.py
│  ├── templates
│  │  └── ph
│  │     ├── article_detail.html
│  │     ├── article_list.html
│  │     └── base.html
│  ├── admin.py
│  ├── apps.py
│  ├── models.py
│  ├── tests.py
│  ├── urls.py
│  ├── views.py
│  └── __init__.py
├── ph_django
│  ├── asgi.py
│  ├── settings.py
│  ├── urls.py
│  ├── wsgi.py
│  └── __init__.py
├── manage.py
├── README.md
└── requirements.txt
```


## Installation

Go to the cloned repository & create the virtual enviroment in python
```bash
  cd ph_django
```

```bash
  python venv myvenv
```

Activate the virtual enviroment.

```bash
  myvenv\Scripts\activate
```

Install the requirements
```bash
  pip install -r "requirements.txt"
```

## Run Locally
- MongoEngine is also ORM which bypasses the Django Models ORM.
- So we don't have to run migrations.
- Hence, instead of using Django models we will use Document from MongoEngine.
- If we had relational database with primary key, foreign key then we would have to run migrations to kiigrate data to Django models.
- Since we are not running migrations in this case, we won't be able to view data in django admin panel.

After install all the dependencies run the manage.py file..

Run the streamlit file in another terminal....

```bash
  python manage.py runserver
```
We can see the articles on http://localhost:8000/ph


## Screenshots
Article list view
![image](https://github.com/user-attachments/assets/d6da8b51-cab1-4b8c-9cc3-6801c75ef5f6)

Article detail view
![image](https://github.com/user-attachments/assets/c6efc11c-5e2f-428d-9d9a-d8cd7eedd624)
