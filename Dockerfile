FROM python:3.7-alpine
WORKDIR /EPCapp
COPY . /EPCapp
RUN pip install -U -r requirements.txt
EXPOSE 80
CMD ["python","epc_app.py"]
