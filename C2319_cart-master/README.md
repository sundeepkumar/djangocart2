# C-2319 Django Project

This is our capstone project for CSCE 490 and CSCE 492.

Link to our web - [http://c2319.pythonanywhere.com](http://c2319.pythonanywhere.com)

In order to use the web, you must be login to your account.


## Running Locally

Run the following commands to get started running this app locally (on Linux machine):

```sh
$ git clone https://github.com/SCCapstone/C-2319.git
$ cd c-2319
$ source bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver
```

Run the following commands to get started running this app locally (on Windows Power Shell):

```sh
git clone https://github.com/SCCapstone/C-2319.git
cd c-2319
.\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then visit `http://http://127.0.0.1:8000` to play with the app.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/SCCapstone/C-2319.git
$ cd c-2319
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```

## Deploying to Pythonanywhere

login to the group pythonanywhere account and run the following:

```sh
$ git clone https://github.com/SCCapstone/C-2319.git
$ cd c-2319
$ mkvirtualenv --python=/usr/bin/python3.7 myenv
$ pip3 install -r requirements.txt
$ python manage.py collectstatic
```

## About our project
>Our team has decided to develop an online platform where students, faculty, and staff can freely buy and sell items from each other. This website will be exclusive to students, faculty, and staff. A university email address will be required when signing up for an account. Our goal for this website is that it will provide a safe environment for students (both undergraduate and graduate), faculty, and staff to buy and sell their goods. The Idea is similar to Craigslist but without the risk of not knowing who you are meeting in person. This website should ideally be usable on laptop and desktop computers.

## Features

* Create users
* Edit users
* Add items
* Remove Items
* Edit items
* Send messages to sellers
* Share items
