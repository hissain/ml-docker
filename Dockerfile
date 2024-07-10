FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./ssl_cert.pem /code/ssl_cert.pem

RUN pip install --cert /code/ssl_cert.pem --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
