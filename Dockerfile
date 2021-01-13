FROM python:3.8
WORKDIR /car_simmulation
COPY . /car_simmulation

RUN pip3 install -r requirements.txt
CMD ["python", "-u", "app.py"]
