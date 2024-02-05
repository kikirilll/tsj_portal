FROM python:3.11.4-slim
WORKDIR /tsj_portal
COPY . /tsj_portal
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]