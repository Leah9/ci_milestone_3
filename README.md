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

Bugs will be added as they are found.

## Bugs

* User registration requires restrictions and validation on user input
* No notification if registration is successful or not
* Requires minimal bot protection

# Validation
## HTTP valid


## CSS valid


# Performancee

## Mobile device

## Desktop


# Acknowledgements and credits
 ## Favicon

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
* pip3 install flask-pymongo
* pip3 install dnspython
* pip3 freeze --local > requirements.txt

# Conclusion


