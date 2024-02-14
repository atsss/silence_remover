FROM jupyter/base-notebook

USER root

WORKDIR /home/jovyan/work

COPY ./requirements.txt /home/jovyan/work

RUN sudo apt-get update && \
    sudo apt-get -y install ffmpeg && \
    python -m pip install --no-cache -r requirements.txt
