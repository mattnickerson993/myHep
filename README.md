# myHEP

## Demo Site

[myHEP](http://mattnickerson.com)

## Video Walkthrough

[myHEP](https://www.youtube.com/watch?v=WQnXS8tS72w)

## About
myHEP is a project built using a javascript front end and django back end, allowing users to create both exercises and home exercise programs. Home exercise programs can be stored on the site and added to the users google calendar.

## How it Works

- The "exercises" app handles most of the functionality of the site. First, users may register for the site, login and create/edit their user profile. Users may reset their password via a reset email if they happen to forget it. Django's default login, logout and password reset views are used to handle this. Register and login forms are styled via crispy forms and display error messages if credentials are incorrect or do not meet acceptable criteria. The registration is built off of djangos user creation form, with the addition of an email field. A Profile model was created as a OnetoOneField with a User to allow users to add a profile picture.The save method for a Profile was overwritten to reduce image size to 300,300 to optimize storage. (Source - Corey Schafer's youtube tutorials where instrumental in this sections development)

- The primary model used within the webapp is titled "Exercise" and includes a title, description, author ( a user), and optional image. Basic create, read, update, and delete functionality is enabled using classed based views in Django ( ListView, DetailView, CreateView, UpdateView, DeleteView). Users must be logged in to create new exercises and view the exercise detail view. Users may only update and or delete exercises they have created. The Home page displays a button to access the ability to create an exercise and also displays all exercises ordered by most recent creation date. Pagination is enabled on the home page using django's Paginator. 

- The library page includes a search bar that updates every time the input in the search bar is changed. Javascript is used to make an api call to the django backend on keyup. A serialize method was added to the Exercise model to handle this call. The retrieve_exercise_library function then returns all exercises that begin with the input in the search bar. This allows the library to be searched without the necessity of a page reload. Seperate pagination functionality was built using javascript to display up to 6 exercises at a time on the library page (handled entirely on the front end).

- A TrainingProgam model was created to allow users to organize exercise into a training program. This model includes an author, title for the program and contents. 

- Contents are composed of a seperate model titled ExerciseStats. This model allows the user to specify sets, reps, notes,and time details for how each exercise will be performed. **This model is necessary as it allows multiple users to use the same exercise in different programs and in different ways.**

-  The Training program page allows users to create a new training program or to view current programs through a dropdown menu. Each exercise in the program will be displayed with the option to edit sets, reps ect or to delete the exercise from the program. If the user chooses to create a new program, they are redirected to library searchbar. Users may then click on an individal exercise and select the "Add to program" dropdown menu. This will display all of the users current programs and allow selection of the program the user wishes to add the exercise to. Both display and selection of programs are enabled through a javascript API call. The training program model contains a serialize method to return the users training programs and contents. View methods handle retrieving and saving new exercises to programs on the backend.

- The calendar app was created to allow users to add a created training program to their google calendar. Users select a training program, date, start and time. Clicking the "Add to my Google Calendar button", will make an api call through the google calendars api and add the event. Google calendar will open and display the event for users to view.

## Tech Stack used:
- Django
- Vanilla Javascript
- Bootstrap 4
- Google calendar api

## How to run locally:

* create a virtual environment

```
$ python -m venv env

$ source env/bin/activate

```
* clone repository
* run pip install -r requirements.txt
* run python manage.py migrate
* run python manage.py runserver

```
$ python manage.py migrate

$ python manage.py runserver

```
* See .sampldotenv file for configuration


## Reflection

### The Good/ My growth:
- This was the first large project I built with Django
- The Django models used in the site turned out to be fairly complex due to the need to store various statistics (sets, reps, time ect) in multiple exercise programs
- I was able to work with the google calendar api to store a users home exercise programs
- I was to develop a searchbar in vanilla javascript that searches on each keystroke without page refresh

### The Bad/Areas to improve:
- I was not familiar and up to speed on django rest framework at the time of this project. As a result, I developed my own serialize function for models that required it as well my own views that returned a customized JsonResponse method. Looking back, I think this was good initial way to learn before moving onto something like Django Rest Framework.
- I was not skilled enough with any frontend Javascript frameworks at the time of this project to implement them. As a result, the frontend relies heavily on vanilla javascript, leading to bulking code that is a bit harder to read. Despite this, I was able to accomplish what I wanted on the site and feel it helped my learning process and understanding.
- Test coverage is very small as I was just beginning to learn how to implement it at the time


## Timeline
- Project completed mid-late January - Early February 2021
