FROM python:3.8

ENV PIP_NO_CACHE_DIR=off \
  PYTHONUNBUFFERED=1


RUN mkdir /server

WORKDIR /server
COPY . .

RUN pip install -U pip setuptools wheel
RUN pip install -U -r requirements.txt

CMD ["uwsgi", "./uwsgi.ini"]