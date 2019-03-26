FROM python:3.7-alpine
WORKDIR /EPCapp
COPY . /EPCapp
RUN pip install -U -r requirements.txt
EXPOSE 8080
CMD ["python","epc_app.py"]
