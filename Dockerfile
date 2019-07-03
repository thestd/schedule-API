FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8085

ENTRYPOINT python3 manage.py runserver