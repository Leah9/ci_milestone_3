# Glossary of Mortgage Terms
## A glossary of mortgage terms and their meanings
## Flask, MongoDB web application for Code Institute Milestone Project 3

# UX
## Project Goal
The primary goad is to create an easy to use and edit glossary of mortgage terms.

## Target Audience

* Anyone trying to purchase a property or understand more about the process and terminology used.

## User goals
* Understand the mortgage process
* Lookup words and their meaning
* Add or edit words and descriprions

## Required sections
* Welcome, explanation
* Search function
* Create account
* Login
* Display results


## User stories

* I am a potential home buyer trying to understand strange terminology.
* I am a broker or adviser and would like to add addiional words.
* I an just curious about the process.

# Design choices

My design choices are to make a simple layout that will work on all devices from phones to desktop PC within a browser. Main functionality should be easy to find and use.

# Wireframe
Wireframe views of the main pages that the site will have based on my required sections.

## Main Screen
### Mobile
![Mobile](/docs/wire_mobile.jpg "Mobile")

### Laptop / Desktop
![Desktop](/docs/wire_desktop.jpg "Desktop")

# Logical Code Outline

## Requirements
* Ability to create an account / register, logon to add and edit.
* Four main functions to allow the user to Create, Read, Update and Delete words and their associated descriptions.
* Users should only be able to edit their own entries.

## High Level Program flow
1. Main page is displayed with instructions
2. Search or Browse the list of words
3. Clicking a word displays its description
4. Option to create an account or login
5. Options to add, edit or delete words if logged in.

# Database

## Table users
|name | type |
|-|-|
| username | string |
| password| string |
| display_name| string |
| admin| bool |

## Table terms

|name | type |
|-|-|
| term | string |
| description | string |
| created_by | username|



# Testing

Manual testing will be carried out during development and after the major functions are completed.

Bugs and feature requests will be added as they are found.

## Bugs

* User registration requires restrictions and validation on user input
* User registration needs explanation of username / password requirements
* Requires minimal bot protection
* The same term can be added multiple times
* Delete confirmation page needs go back or cancel button, not just delete.
* Clicking the application name should return the user to the home page, It does nothing at present.



## Resolved Bugs

* Logging in on Heroku does not work. https://mortgage-glossary.herokuapp.com/login
    * Secrey key was not entered in Heroku config.


* Notifications are not obvious enough, need styling
    * Styled with materialize css to match the rest of the site.


* No notification if registration is successful or not
    * Now notified with flash message


* Edit term is displayed on delete page instead of delete
    * Corrected text

* Resolve 404 error by adding favicon.ico
## Planned Features
* Search function
* Account area with list of logged in users terms
* Ability to add and use a display name in place of username

# Validation
## HTTP valid
https://validator.w3.org/nu/?doc=https%3A%2F%2Fmortgage-glossary.herokuapp.com%2Fget_terms
Pass

## CSS valid
https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmortgage-glossary.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
Pass

## Python
Linted with Code Instutite linter.

# Performance

## Mobile device
![Mobile](/docs/lighthouse_mobile.jpg "Mobile")

## Desktop
![Mobile](/docs/lighthouse_desktop.jpg "Desktop")

# Acknowledgements and credits

Images from https://www.pexels.com free license.
https://flask.palletsprojects.com
Site based on tutorials from CI

## Favicon
Created by https://favicon.io/

# Deployment

Install Flask:
* pip3 install Flask

Heroku requirements :
* pip3 freeze --local > requirements.txt
* echo web: python app.py > Procfile
* Create a new app on heroku.com
* Connect Heroku to the GitHub repository
* git add requirements.txt
* git add Procfile

MongoDB:
* Create account and new collection
* Create the required tables (terms and users)
* pip3 install flask-pymongo
* pip3 install dnspython
* pip3 freeze --local > requirements.txt
* Add the connection information to the evn file
* Add the connection details on Heroku

