 FROM debian

## Environmental variables to configure things
## Setting shell so pipenv shell works
ENV SHELL=/bin/bash

## Update and install dependencies
RUN apt update && \
  apt upgrade -y && \
  apt install -y python3-pip && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple lambdata-jayadamo