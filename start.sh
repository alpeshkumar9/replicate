python manage.py makemigrations
python manage.py migrate
echo 'Migration completed!'

python manage.py collectstatic --noinput
echo 'Static files generated'

gunicorn --workers 2 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 \
     dhi.wsgi
