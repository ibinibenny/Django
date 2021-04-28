afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~$ cd Documents
afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ virtualenv afr_env
created virtual environment CPython3.8.5.final.0-64 in 1212ms
  creator CPython3Posix(dest=/home/afreedfayaz/Documents/afr_env, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, pkg_resources=latest, via=copy, app_data_dir=/home/afreedfayaz/.local/share/virtualenv/seed-app-data/v1.0.1.debian.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ source afr_env/bin/activate
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ django-admin startproject eshop

Command 'django-admin' not found, but can be installed with:

sudo apt install python3-django

(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ django-admin start project eshop

Command 'django-admin' not found, but can be installed with:

sudo apt install python3-django

(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ django-admin startproject eshop

Command 'django-admin' not found, but can be installed with:

sudo apt install python3-django

(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ pip install django
Collecting django
  Using cached Django-3.2-py3-none-any.whl (7.9 MB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.3.4-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Installing collected packages: asgiref, sqlparse, pytz, django
Successfully installed asgiref-3.3.4 django-3.2 pytz-2021.1 sqlparse-0.4.1
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ django-admin startproject eshop
CommandError: '/home/afreedfayaz/Documents/eshop' already exists
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ django-admin startproject eshop1
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents$ cd eshop1
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 28, 2021 - 14:43:34
Django version 3.2, using settings 'eshop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[28/Apr/2021 14:44:01] "GET / HTTP/1.1" 200 10697
[28/Apr/2021 14:44:01] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[28/Apr/2021 14:44:01] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[28/Apr/2021 14:44:01] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[28/Apr/2021 14:44:01] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
Not Found: /favicon.ico
^C(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(afr_env) afreedfayaz@afreedfayaz-HP-Laptop-15-da0xxx:~/Documents/eshop1$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 28, 2021 - 14:47:53
Django version 3.2, using settings 'eshop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

