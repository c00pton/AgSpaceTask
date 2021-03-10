PROGRAM REQUIREMENTS
-
* Python 3.8
* Python 3 virtual environment
* Docker

***
RUN LOCALLY
-
* Set up virtual environment, e.g. `python -m venv venv`
* Activate venv: `.\venv\Scripts\activate `(Windows) or `source ./venv/bin/activate` (Unix)
* `pip install -r requirements.txt`
* `uvicorn --port 8000 main:app`
* Docs: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc

***
CONTAINERISE
-
* `docker build -t agspace task .`
* `docker run -d -p 80:8000 agspacetask`
* Docs: http://127.0.0.1/docs
* Redoc: http://127.0.0.1/redoc

***
ENDPOINTS
-
`curl`, a browser or python `requests` module can be used to access the endpoints in the documentation for the following models
* User
* Account
* Address

***
UNIT TESTS
-
Unit tests will test the lifecycle of a high level User including their associated account and address
* `pytest` or `coverage run -m pytest`

***
BEHAVIOUR TESTS
-
Behaviour tests will test some scenarios encapsulating the lifecycle events of the unit tests
* `behave`
