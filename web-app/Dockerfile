FROM python:3.9.1
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3.9" ]

CMD [ "app.py" ]
