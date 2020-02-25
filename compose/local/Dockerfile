FROM python:3.7-slim

RUN apt-get update && \
apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0 python-scipy

COPY ./identify_shapes /app
COPY ./resources /resources
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

ENTRYPOINT ["python", "/app/find_shapes.py"]
