# Movie microservice

##### The web application basically, fastAPI based microservices project.

###### Prerequisites
- Python 3.10
- FastAPI
- Psql 14.0

> The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed fast-api apps on Windows, you should have little problem getting up and running.

```
git clone https://github.com/mbrsagor/movie_service.git
cd movie_service
virtualenv venv --python=python3.10
source venv/bin/activate
pip install -r requirements.txt
```

###### Then create ``.env`` file and paste code from `.sample.env` file and add validate information.

-------------------------------------------
```bash
|--> .sample.env
|--> .env
```
