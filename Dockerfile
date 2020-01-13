FROM python:3.7-alpine3.8

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install uvicorn gunicorn \
    && apk del .build-deps gcc libc-dev make \
    && apk add --no-cache bash \
    && apk add --no-cache curl


COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
