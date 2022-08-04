#Docker File for Backend.py

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install flask

RUN pip3 install flask_restful

COPY ./backend.py ./app.py

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]

