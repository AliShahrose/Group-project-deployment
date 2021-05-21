FROM python:3.8

WORKDIR /backend-api-v2

COPY . /backend-api-v2

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]