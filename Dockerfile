FROM python:3.8.0-slim-buster

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app/src

CMD [ "python", "microblog.py" ]
