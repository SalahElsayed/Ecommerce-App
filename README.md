# E-commerce App
This is an e-commerce web application built using Django and Django REST Framework.

## Prerequisites
Python 3.10.6+
Django 4.2.1+
Django REST Framework 3.14.0+

## Getting Started

Follow these steps to get the project up and running on your local machine:

1. Clone the repository:
   ```shell
   git clone https://github.com/SalahElsayed/Ecommerce-App.git
   cd Ecommerce-App
   ```

2. Set up a virtual environment (optional but recommended):
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Create a PostgreSQL database for the app.
   - Update the database configuration in `settings.py` file:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. Apply the database migrations:
   ```shell
   python manage.py migrate
   ```

6. Start the development server:
   ```shell
   python manage.py runserver
   ```

7. Access the app in your web browser at `http://localhost:8000`.


Contact with the author 
Salah E.Abuhashim 
salahelsayed995@gmail.com