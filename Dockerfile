FROM python:3.10.5-slim-buster

WORKDIR /srv

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

ADD . /srv

CMD ["python", "run.py"]