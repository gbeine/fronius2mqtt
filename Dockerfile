FROM python:3-alpine

WORKDIR /fronius2mqtt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY fronius2mqtt .

CMD [ "python", "./fronius2mqtt" ]
