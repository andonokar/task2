FROM python:3.10.12-slim
RUN mkdir /main
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/main/. /main
CMD ["python3", "main"]