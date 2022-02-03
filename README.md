# Flask tutorial

This app was created from a flask tutorial, the **Flaskr** app: [flask tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)

[![Run Py Tests](https://github.com/FominSergiy/flask-tutorial/actions/workflows/run-py-tests.yml/badge.svg)](https://github.com/FominSergiy/flask-tutorial/actions/workflows/run-py-tests.yml)

## Setup

You will need to setup a virtual env.

```Bash
$ python3 -m venv /your/project/dir
```

Once you have set it up run the command below from the root of your project, which will activate your virtual env.

```Bash
$ source activate.sh
```

Once you are in your virtual env, go ahead and install all the required modules.

```Bash
$ pip install -r requirements.txt
```

init the db

```Bash
$ flask init-db
```

You are good to go! Run the following below to deactivate your virtual env

```Bash
$ deactivate
```

## Running Flaskr

```Bash
$ flask run
```

## Running Tests
### Check Unit Test Results
```Bash
$ pytest -v
```

### Check the Test Coverage
```Bash
$ coverage run -m pytest
```

get the test coverage report

```Bash
$ coverage report
```
