FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./ ./
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "manage.py", "runserver"]
