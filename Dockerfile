FROM python:3.7.1
MAINTAINER ArchanaPunia
COPY . /webapp
WORKDIR /webapp
RUN pip install flask
EXPOSE 5000
CMD flask run --host=0.0.0.0 > /tmp/log.txt 2>&1
