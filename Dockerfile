FROM python:2.7

WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt


ENTRYPOINT ["/app/entrypoint.sh"]
CMD []