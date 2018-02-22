FROM python:3.6-alpine
WORKDIR /app

ADD . /app
RUN apk add --update python3 && pip3
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN apk add ffmpeg
CMD ["python", "main.py"]