FROM jupyter/base-notebook

USER root

WORKDIR /home/jovyan/work

RUN sudo apt-get update && sudo apt-get -y install ffmpeg

COPY ./requirements.txt /home/jovyan/work

RUN python -m pip install --no-cache -r requirements.txt
