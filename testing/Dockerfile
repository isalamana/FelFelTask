FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY consume.py .
CMD ["python", "-u", "consume.py"]
