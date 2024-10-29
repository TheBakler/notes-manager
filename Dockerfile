FROM python:3.9 as todolist
LABEL authors="aconfear"

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY .. /app

WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "webserver:app", "-b :8000"]