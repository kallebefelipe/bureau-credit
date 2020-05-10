FROM python:3.6
EXPOSE 5002

ADD requirements.txt /web/requirements.txt
RUN pip install -r /web/requirements.txt

ADD . /web/
WORKDIR /web/
VOLUME /web

# CMD ["gunicorn", "--bind=0.0.0.0:5002", "app:web"]
CMD python app.py
