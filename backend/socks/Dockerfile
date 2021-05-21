FROM python:3.8

WORKDIR /backend-sock-v2

COPY . /backend-sock-v2

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python"]

CMD ["app.py"]