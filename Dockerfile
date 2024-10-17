FROM python:3.10-slim

WORKDIR /app/

EXPOSE 8000

COPY requirements.txt requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "currency_converter.wsgi", "-w", "4", "-b", "0.0.0.0:8000"]
