FROM python:3
RUN mkdir /data
WORKDIR /data
COPY requirements.txt /data
RUN pip install python-Levenshtein==0.12.0
RUN pip install -r requirements.txt
COPY ./shop /data
