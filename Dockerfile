FROM python:3.7
WORKDIR /MarIA_Project

RUN apt-get update

COPY . /MarIA_Project

RUN ls -la /MarIA_Project

RUN pip install -r requirements.txt --no-cache-dir

RUN python main.py
