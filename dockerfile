FROM alpine:latest
RUN apt-get update


RUN apt-get install -y -q build-essential python-pip python-dev python-simplejson git
RUN pip3 install --upgrade pip
RUN apk add --no cache python3-dev \ 
    && pip3 install --upgrade pip
RUN mkdir deployment
RUN git clone https://github.com/lisboapg93/Test_cloud.git /deployment/
RUN /deployment/env/bin/pip3 install flask
RUN /deployment/env/bin/pip3 install flask-restx
RUN /deployment/env/bin/pip3 install -U flask-cors
WORKDIR /deployment
CMD python3 app.py