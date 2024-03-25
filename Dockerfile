FROM python:3.10.12-slim
RUN mkdir /src
RUN mkdir /src/main
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/main/. /src/main
CMD ["python3", "/src/main"]