FROM python:3.9

RUN pip install pandas

RUN pip install sqlalchemy psycopg2


COPY listings.csv listings.csv

COPY calendar.csv calendar.csv

COPY reviews_details.csv reviews_details.csv

COPY reviews.csv reviews.csv



COPY ingest.py ingest.py

ENTRYPOINT ["python","ingest.py"]






