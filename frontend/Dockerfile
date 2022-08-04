#DockerFile Backend

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install flask

RUN pip3 install flask_restful

RUN pip3 install requests

COPY ./frontend.py ./app.py

EXPOSE 5001

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001"]
