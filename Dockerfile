FROM python:3.8.5
LABEL name='API YaMDB Yandex Practicum project' version=1
RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
