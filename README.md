# Simple authentication in Django
## Overview
Little side-project written for learning django authentication.

## Some things used in project
- Custom db user model
- Login, logout redirect pages
- Login method decorator
- Redirects to and from login page to previously blocked content
- Form Models

## Screenshots
1. Main page viewed as anonymous user
![index page](gh/index-anonymous.png)
2. Register and login views
![register page](gh/register.png)
![login page](gh/login.png)
3. Test view (available only for authenticated users)
![page for authorized users](gh/test-authenticated.png)


## How to run project
0. Make sure you have python and django installed. 
1. Download or clone repository 
2. Open cmd in simple_authentication/ 
3. Type following code to create database and run migrations: 

```cmd
python manage.py migrate
```

4. Type following code to run django server: 

```shell
python manage.py runserver
```

5. Paste url given by django server in your browser and... It's done 😉

## Urls
- [Customizing authentication in Django](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)
- [Using the Django authentication system](https://docs.djangoproject.com/en/3.0/topics/auth/default/)