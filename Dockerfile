FROM python:3.8

WORKDIR /api

COPY . /api/

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]


