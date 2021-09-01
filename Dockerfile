
FROM python:3.9.1


WORKDIR /app


COPY . .


RUN pip install -r requirements.txt


EXPOSE 3133

CMD ["python" ,"./app.py"]