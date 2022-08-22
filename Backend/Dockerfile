FROM python:3.6

RUN mkdir -p /app
RUN pip install --upgrade pip
WORKDIR /app

COPY . /app


RUN pip install -r requirements.txt
# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade
EXPOSE 5000

CMD ["python", "main.py"]