#!/bin/sh
cd $APP_PATH

# check if the database is ready
echo "Waiting for Postgres DB"
while ! pg_isready -h $PG_HOSTNAME > /dev/null 2>&1;
do
  echo -n "."
  sleep 1
done
echo "Postgres DB is ready"

# in case we used mysql db
# echo "Waiting for Mysql DB"
# while ! mysqladmin ping -h"$MYSQL_HOSTNAME" --silent;
# do
#   echo -n "."
#   sleep 1
# done
# echo "Mysql is ready"

# create tables
echo "Updating Database Tables"
./manage.py makemigrations
./manage.py makemigrations legacy
./manage.py migrate
echo "The Database has been updated"

# load data to tables
echo "Updating Database Tables"
./manage.py loaddata seed_data.json
./manage.py loaddata publictargets_data.json
echo "The Database has been updated"

# create roles
echo "Groups..."
cat /create_groups.py | ./manage.py shell
# create admin user
echo "Superuseres..."
cat /create_superuser.py | ./manage.py shell

# collect static files
./manage.py collectstatic --no-input

# run the server
echo "Starting the server..."
gunicorn backend.wsgi --bind 0.0.0.0:8000