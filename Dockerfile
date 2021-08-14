FROM python:3.9.6-alpine3.14

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ADD main.py /main.py

EXPOSE 8080

COPY ./app /app

CMD ["python3", "main.py"]