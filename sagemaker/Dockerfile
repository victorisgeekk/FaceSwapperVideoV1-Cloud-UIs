FROM python:3.10-slim

WORKDIR /opt/program

COPY requirements.txt /opt/program/requirements.txt
RUN pip install --upgrade pip && pip install -r /opt/program/requirements.txt

COPY app.py /opt/program/app.py

EXPOSE 8080

CMD ["python", "/opt/program/app.py"]
