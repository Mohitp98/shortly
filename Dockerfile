# Using Python 3.6 Slim Buster (A Debian Based Python Distribution for Docker)
FROM python:3.6-slim-buster
MAINTAINER mohitspatil98@gmail.com

# Copying the app folder of Project to the Container Work Directory which is /app
WORKDIR /app
COPY ./app .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8

# Installing Build Essentials for Compiling and Building of Python Packages
RUN apt update
RUN apt-get install -y build-essential

# Installing Application dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Port for Communication
EXPOSE 5000

# Running the Python App
CMD ["python3", "app.py"]