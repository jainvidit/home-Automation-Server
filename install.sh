#!/usr/bin/env bash
# Install essential packages from Apt
apt-get update -y
# Python dev packages
apt-get install -y build-essential python python-dev python-setuptools python-pip
apt-get install -y libxml2-dev libxslt1-dev
apt-get install -y nginx uwsgi uwsgi-plugin-python
apt-get install -y postgresql postgresql-contrib libpq-dev
# Edit the following to change the name of the database user that will be created:
APP_DB_USER=my_user
APP_DB_PASS=marullz..
# Edit the following to change the name of the database that is created (defaults to the user name)
APP_DB_NAME=test

cat << EOF | sudo -u postgres psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER
                                  LC_COLLATE='en_US.utf8'
                                  LC_CTYPE='en_US.utf8'
                                  ENCODING='UTF8'
                                  TEMPLATE=template0;
EOF

#export database url for app
export DATABASE_URL=postgresql://$APP_DB_USER:$APP_DB_PASS@localhost:5432/$APP_DB_NAME

pip install -r requirements.txt