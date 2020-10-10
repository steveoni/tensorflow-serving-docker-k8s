FROM python:3.8-slim

ENV PYTHONUNBUFFERED True
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

CMD ["python","app.py"]