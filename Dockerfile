FROM python:3.8
WORKDIR /simmulation
COPY . /simmulation

RUN pip3 install -r requirements.txt
CMD ["python", "app.py"]
