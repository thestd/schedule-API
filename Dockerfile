FROM python:3.7.4-alpine3.10 as base
RUN apk add --no-cache build-base libxml2-dev libxslt-dev
COPY ./requirements.txt /requirements.txt
RUN pip3 install --target="/install" -r /requirements.txt


FROM python:3.7.4-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache libxml2-dev libxslt-dev
COPY --from=base /install /usr/local/lib/python3.7/site-packages
RUN mkdir /app
WORKDIR /app
COPY ./ ./
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "manage.py", "runserver"]
