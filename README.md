# Rob
Question &amp; Answer

# how to install Virtual env whith multiple python in system
   Creating virtual env if we have 2 python so use specific python to install python3.6 version
    virtualenv -p python3 test
# start project
   After creating virtual env go inside project where we can have requirement.txt file
   run pip install -r requirement.txt command
   this will take time to install package
# setup DB
  run python manage.py makemigations
  then python manage.py migrate
  this will install DB in our application
  run server using python manage.py runserver
  
# create superuser
  python manage.py createsuperuser 
  enter user details which is asked
  
# hit first API
  http://localhost:8000/adnmin
  login to admin system
  create new user at user table
  
# Email config
  to work with email need to setup email id and password which we can see in djangi settings file

# JWT Token
  after setting up access the token api which will give 2 things
  Access, refresh
# first hit to API
  using token hit the api
