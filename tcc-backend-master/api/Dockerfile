FROM python:3.10-slim-bullseye

# install some usefull dependencies
RUN apt-get update && apt-get install \
  --no-install-recommends -qq -y \
  build-essential \
  curl \
  libmagic-dev \
  libpq-dev \
  python3-pip \
  python3-setuptools

# Create new directory
RUN mkdir -p /usr/src

# install requirements
WORKDIR /usr/src
COPY requirements.txt /usr/src

WORKDIR /usr/src/api
ADD api /usr/src/api

# install requirements
WORKDIR /usr/src
RUN pip3 install --no-cache-dir -r requirements.txt

#cleanup
RUN rm requirements.txt

WORKDIR /usr/src/api