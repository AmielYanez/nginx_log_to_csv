FROM python:2.7

WORKDIR /app

ADD app /app
ADD scripts /scripts
RUN pip install -r requirements.txt

ENTRYPOINT ["/scripts/run_app.sh"]
CMD []