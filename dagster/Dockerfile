FROM python:3.11-slim

ENV DAGSTER_HOME=/opt/dagster/dagster_home

WORKDIR /opt/dagster/app

COPY requirements.txt /opt/dagster/app/requirements.txt
RUN pip install --no-cache-dir -r /opt/dagster/app/requirements.txt

RUN mkdir -p /opt/dagster/dagster_home

COPY . /opt/dagster/app
