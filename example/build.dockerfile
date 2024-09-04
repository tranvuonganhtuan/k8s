FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app/
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]