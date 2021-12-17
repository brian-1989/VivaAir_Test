FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /API

WORKDIR /API

COPY . /API

RUN apt-get update

RUN pip install -r requirements.txt

RUN python3 -m pip install --upgrade pip

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
