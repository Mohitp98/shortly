# SHORTLY
URL Shortener Service

## Technical Stack

Shortly uses following open source projects:

* [Python3](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries..
* [Flask-RestFul Framework](https://flask-restful.readthedocs.io/en/latest/) - Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
* [Swagger](https://swagger.io/) - Swagger is an open-source software framework that helps developers to design, build, document, and consume RESTful web services.
* [Pytest](https://docs.pytest.org/en/stable/contents.html) - Pytest is a testing framework that makes building simple and scalable tests easy.


## Installation

### Step 1: Clone the Repo

```sh

$ git clone git@github.com:Mohitp98/shortly.git 

```

### Step 2: Install the dependencies

```sh
$ pip3 install -r app/requirements.txt
```

**Note:- Default port number for the service: `5000`**

### Step 3:  Run application

```sh
$ cd app/
$ python3 app.py
```


## Unit Testing
**NOTE: All Unit Test cases are kept in [tests](tests) folder.**

To run unit test cases for Service. Firstly clone this repo and run following commands:

```sh
# install dependencies
$ pip install -r app/requirements.txt

# execute unit tests
$ pytest tests/
```

## API Documentation

You can check out API documentation after running the service using Swagger UI [here][1].

[1]: http://localhost:5000/api/spec.html
