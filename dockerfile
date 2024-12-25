
FROM python:3.11-slim

WORKDIR /app

COPY requirements/requirements.txt /app/

RUN apt-get update && apt-get install -y tcpdump

RUN apt-get update && apt-get install -y tcpdump tshark

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# Default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
