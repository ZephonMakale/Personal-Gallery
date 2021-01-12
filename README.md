## Personal Gallery Application
This is my personal gallery application that displays my photos for the users to see.
### Getting Started
Here are the things you need to install the software.

#### Prerequisites
* The text Editor. Eg Visual Studio
* Django App.
* Virtual Environment.
#### Installing
Step 1
To get this project up and running you should start by having Python installed on your computer. The first step is to create a virtual environment to store your projects dependencies separately. You can install virtualenv with:
* pip install virtualenv
  
Step 2. 
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project:
* virtualenv env
  
Step 3.
That will create a new folder env in your project directory. Next activate it with this command:
* source env/bin/activate
  

Step 4.
Then install the app dependencies with:
* pip install -r requirements.txt

Step 5.
Now you can run the app with this command:
* python manage.py runserver

Note if you want to get some data out of the system, you will need create your own database.
## Running the tests
Django allows us to test our systems. To test the project system, you have to run the following commands:
* source env/bin/activate 
* python3.8 manage.py test post

## Deployment
To deploy this on a live system like Heroku Server, you have to install the heroku cli.
Sign up to Heroku.
Then install the Heroku Toolbelt. This is a command line tool that manages your Heroku apps
After installing the Heroku Toolbelt, open a terminal and login to your account:

* Add a Procfile in the project root;
* Add requirements.txt file with all the requirements in the project root;
* Add Gunicorn to requirements.txt;
* A runtime.txt to specify the correct Python version in the project root;
* Configure whitenoise to serve static files.
  
After editing the respective files and installations you have added, create the heroku app
* heroku create 
  
Create a postgres addon to your heroku app
* heroku addons:create heroku-postgresql:hobby-dev

Log in to Heroku dashboard to access our app and configure it. Then push it to remote by running the following command:
* git push heroku master
## Built With
  * Python3.8 version
  * Django 3.1
   

 ## Contributing
    Want to contribute? Awesome!
    When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.Please note we have a code of conduct, please follow it in all your interactions with the project.
  ## Pull Request Process
  Ensure any install or build dependencies are removed before the end of the layer when doing a build. 
  Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
  Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent. 
  Here is an example on how to fix a bug or enhance the project, follow these steps:
   * Fork the repo
   * Create a new branch (git checkout -b improve-some-features)
   * Make the changes in the files
   * Add the changes to reflect that they have been made
   * Commit your changes (git commit -am 'Improved feature')
   * Push to the branch (git push origin improve-some-features)
   * Then create a Pull request

## Authors
* Zephon Makale
## Contact Information
Incase you have a query or contributions, please email me at(zephon.makalle@gmail.com)

## License
   * See below for more details on licensing.
   * MIT License "https://choosealicense.com/licenses/mit/"
   * Copyright (c) 2021 Zephon Makale