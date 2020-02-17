FROM python:3.7-slim

RUN apt-get update && \
apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0

COPY ./identify_shapes /app
COPY ./resources /resources
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

ENV SMALL_IMAGE small-shades-of-grey.png
ENV IMAGE shades-of-grey.png
ENV METHOD cv2
# or ENV foo=/bar
ADD . $SMALL_IMAGE
ADD . $IMAGE
ADD . $METHOD

ENTRYPOINT ["python", "/app/find_shapes.py"]
