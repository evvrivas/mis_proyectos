Django on OpenShift v3.0
===


![Django on OpenShift 1.10](https://raw.githubusercontent.com/biwin/Django-on-OpenShift/master/static/demo/images/screenshot.v3.png) <br>
Django on OpenShift is a independent fork of [openshift-django17] by [John Flynn Matthew].


### QuickLinks
Previous versions and supported Django versions <br>
<br>


|Version|Django Version|Tag|Browse|
|---|---|---|---|
|3|1.10|`v3`|[v3](https://github.com/biwin/Django-on-OpenShift/)|
|2|1.8 LTS|`v2`|[v2](https://github.com/biwin/Django-on-OpenShift/tree/f7eddd3b709e58d6ff1af44e4ae7ae84e52740f4)|

###Features
* Ready to use for local development
* Easy to push to OpenShift
* Works with  either PostgreSQL or MySQL
* Minimal changes to default django 1.10.x LTS installation
* Support to new template configurations for Django 1.8.x LTS
* Support for multiple template engines
* Uses new folder layout from OpenShift March 2014 release
* Allows for debug mode on OpenShift with the help of an environment variable.
* Use of static files is pre-configured
* Preloads Bootstrap and jQuery cdn versions
* New Demo app to display software information
* Code formatting as per PEP8 recommendations


###How to use this repository
- Create an account at https://www.openshift.com
- Install the RHC client tools if you have not already done so.


    `sudo gem install rhc`
    `rhc setup`


- Create a Python 2.7 application


    `rhc app create django python-2.7`


- Add the database cartridge (choose one)


    `rhc add-cartridge postgresql-9.2 --app django`

OR

    `rhc add-cartridge mysql-5.5 --app django`


- Add this upstream repo

```
    cd django
    git remote add upstream -m master https://github.com/biwin/Django-on-OpenShift.git
    git pull -s recursive -X theirs upstream master
```

- set the WSGI application to django's built in WSGI application (stored in the wsgi folder).


    `rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi/wsgi.py --app django`


- Push the repo upstream


    `git push`

- SSH into the application to create a django superuser.


    `python app-root/repo/manage.py createsuperuser`


- Now use your browser to connect to the Admin site.

### Static files
Static files are already setup and ready to use for either local or OpenShift use.

Place all static files / folders into the project-directory/static.  They will be collected with `collectstatic` when
pushed to OpenShift.

**DO NOT PUT STATIC FILES INTO /wsgi/static/**, this is merely a place holder for the `collectstatic` command.

### Where do I put my HTML Templates?
You are free to place the HTML template files either on the separate template directory or in-app template directory or
 on both.
Your HTML templates can be placed on,

 * `project/templates`
 * `project/app/templates`


### Running locally and the django tutorial
This repository was designed to allow you to quickly develop and deploy a website to OpenShift.  For local development, make sure you have the following setup:

- Virtualenv for this instance of python / django.
- pip (should be installed with virtualenv)

Once you have those installed, install the requirements for this repository:


    pip install -r requirements.txt


Once you have django installed, you can continue the tutorial from here https://docs.djangoproject.com/en/1.7/intro/tutorial01/#database-setup, although the default database and application configuration should be sufficient.

### Configuration details
When a git push is done, the ``.openshift/action_hooks/deploy` is executed.  This script does two things:

1.  Runs python manage.py migrate to update any changes to the Schema
2.  Runs python manage.py `collectstatic` to move all necessary static files into /wsgi/static

#### Debugging mode and OpenShift
By default, debug mode is off when pushed to OpenShift.  However, if you'd like to turn on debugging (settings.DEBUG) while running on OpenShift, you can set the environment variable DEBUG to True and then stop and start your application, and debugging will be turned on.

    rhc env set DEBUG=True

### HTTPS redirection
HTTPS redirection is accomplished by telling the local Apache gear to redirect all traffic to the HTTPS version of your site.  You'll need to add an .htaccess file into the WSGI folder

Add the following .htaccess file into the WSGI folder



    RewriteEngine on
    RewriteCond %{HTTP:X-Forwarded-Proto} !https
    RewriteRule .* https://%{HTTP_HOST}%{REQUEST_URI} [R,L]  



This will redirect **ALL** HTTP traffic to the site to HTTPS.

### Notes on compatibility
This setup works with python 2.7 and 3.3. Issues, pull requests are welcome.


[openshift-django17]:https://github.com/jfmatth/openshift-django17
[John Flynn Matthew]:https://github.com/jfmatth/
