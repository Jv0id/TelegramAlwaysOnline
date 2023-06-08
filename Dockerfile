FROM python:3.9.2 as builder

RUN apt-get update && apt-get install tzdata git

COPY . /ALWAYS-ONLINE

ENV TZ=Asia/Shanghai

WORKDIR /ALWAYS-ONLINE

RUN pip3 install -r /ALWAYS-ONLINE/requirements.txt

CMD ["python", "main.py"]
