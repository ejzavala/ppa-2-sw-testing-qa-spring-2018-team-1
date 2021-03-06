# PPA 2 - Team 1

Software Testing and QA - CSE 4283 - Spring 2018

Professional Practice Assignment 2 - Team 1

[![Coverage Status](https://coveralls.io/repos/github/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1/badge.svg)](https://coveralls.io/github/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)
[![Build Status](https://travis-ci.org/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1.svg?branch=master)](https://travis-ci.org/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)

[Travis-CI](https://travis-ci.org/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)

[Coveralls](https://coveralls.io/github/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)

[Staging Environment](https://ppa-2-team-1.appspot.com/)

[Production Environment](https://ppa-2-team-1-production.appspot.com/)

[Video Capture for Assignment](https://youtu.be/_NZCPxbl0TQ)

`I refuse to upload large binary files to a git repo, it is bad practice.`

## Getting Started
We are going to be working with:

| Program                                                                     | Version |
| --------------------------------------------------------------------------- | :-----: |
| [Windows](https://www.microsoft.com/en-us/software-download/windows10)      | 10      |
| [Python](https://www.python.org/)                                           | 3.6.3   |
| [virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) | 1.2.5   |
| [pytest](https://docs.pytest.org/en/latest/)                                | 3.4.0   |
| [pylama](https://github.com/klen/pylama)									  | 7.4.3   |
| [pytest-cov](https://pypi.python.org/pypi/pytest-cov)						  | 2.5.1   |
| [python-coveralls](https://pypi.org/project/python-coveralls/)			  | 2.9.1   |
| [Flask](http://flask.pocoo.org/)											  | 0.12.2  |
| [Jinja2](http://jinja.pocoo.org/docs/2.10/)								  | 2.10    |
| [Cypress](https://www.cypress.io/)								  		  | 2.1.0   |
| [EditorConfig](http://editorconfig.org/)									  | ----    |

And their respective dependencies...
(Cypress has 187 dependencies by itself, this is what's wrong with js developers, they `npm install` their way through problems. *cough left-pad cough*)

### Install python
Download [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and follow
the on screen instructions leaving all of the settings as default.

### Installing and setting up virtualenv and installing requirements
We will be using a virtual environment to make things a bit easier.  Python 3 ships with
support for this (see: `python -m venv -h`), but we are using
[virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) rather than
directly using the venv package.


**_The following steps assume you have cloned the repo using your preferred method of git
and navigated to the directory that it is located in_**

``` bash
# install virtualenvwrapper-win using pip
pip install virtualenvwrapper-win

# make a new virtual environment
mkvirtualenv --python=C:\\path\\to\\python3.6\\python.exe -a C:\\path\\to\\ppa-2-sw-testing-qa-spring-2018-team-1 -r requirements.txt ppa-2

```

All of the requirements to run this project will be installed when you create the new virtual
environment using requirements.txt

The virtual environment will automatically activate when you create it.

### Reference commands:
``` bash
# activate the virtualenv
# can be done anywhere on the system
# it will take you to the working directory of the project
workon ppa-2

# updating requirements
pip install -r requirements.txt
pip install -e .

# leave the virtualenv
deactivate
```

### Running Tests

Use the following command to run the test suite and style checker and generate a coverage report:

``` bash
# in the project root:
pytest --pyargs app --pylama --cov=app tests/
```

pytest will automatically discover all tests that follow their naming convention
(see [here](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)).

### Running Flask locally

To run flask locally, use the following command:

``` bash
# start flask app
python wsgi.py
```

This will start the flask app on you computer on port `5000`.
To view it, go to [http:\\localhost:5000](http:\\localhost:5000)

### End-to-end Testing with Cypress

For our end-to-end tests, we are using Cypress.
To Use Cypress, make sure you have `Node` and `npm` installed.
Then run the command `npm install` in the root of the repo to install Cypress and it's dependencies.

There are two modes of operation for Cypress, headed and headless:
``` bash
# run headed
npm run cypress:open
# run headless
npm run cypress:run
```

## Configuration files

### `.coveragerc`

Used to configure pytest-cov.

### `.editorconfig`

We're using editorconfig to make sure that everyone's editor is configured to handle line endings, tabs vs. spaces, etc. properly so that everything can be consistent. Please be sure to install the plug-in for whatever editor you're using before editing and committing anything.

### `.travis.yml`

Used to configure Travis-CI for running test, deploying to the staging server, calling coveralls, and sending Discord webhooks.

### `app.yaml`

Used to configure the Google App Engine for automated deployment.
This uses gunicorn to start the flask app defined by `wsgi:app` which is the app run by `wsgi.py`

### `client-secret.json.enc`

This is the encrypted keyfile that Travis uses to deploy to Google App Engine.

### `config.py`

This is our flask configuration file, it contains several different configurations for development and production.

### `cypress.json`

Cypress' configuration file.
Set baseUrl and tell it not to record video.

### `package.json` and `package-lock.json`

These files are for npm and Travis to install Cypress and its many many dependencies.
As well as a few shortcuts for running Cypress. 

### `pylama.ini`

Used to configure pylama.

### `requirements.txt`

Requirement file for python, lets us install all of our dependencies quickly and easily.
Travis and Google App Engine use this to install python dependencies on them.

### `setup.py`

Used to define the custom module so that pytest can import them easier.

### `wspi.py`

Used by gunicorn to start the flask app.
