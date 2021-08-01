# e-clinic-back

E-Clinic Backend (Django REST API) multidisciplinary project

# Deployment

## Development

### Auto Scripts

    python3 setup.py

### OR Setup Manually (In case of errors)

- `pip install -r requirements.txt`
- `python3 manage.py makemigrations authentication medical`
- `python3 manage.py migrate`
- `python3 manage.py loaddata data.json`
- `python3 manage.py runserver`

## Production

- I'll be dockerizing the project soon
