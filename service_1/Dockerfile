FROM python:3.6

ADD requirements.txt /web/requirements.txt
RUN pip install -r /web/requirements.txt

ADD . /web/
WORKDIR /web/
VOLUME /web

CMD python app.py
