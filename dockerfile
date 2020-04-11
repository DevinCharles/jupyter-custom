# docker build -t jupyter/custom .

FROM jupyter/datascience-notebook
LABEL maintainer="devincprescott@gmail.com"

################################
## Installing Cite2c & Zotero ##
################################
USER root
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y gnupg2
RUN wget -qO- https://github.com/retorquere/zotero-deb/releases/download/apt-get/install.sh | sudo bash
RUN apt update && apt upgrade -y
RUN apt install -y zotero
USER jovyan
RUN python3 -m pip install cite2c
RUN python3 -m cite2c.install

########################
## Including MiniSOM  ##
########################
RUN pip install minisom
RUN pip install lxml

#################################
## Update All Python Packages  ##
## The build here takes awhile ##
#################################
RUN conda update -n base conda 
RUN conda update python
RUN conda update --all
RUN jupyter lab build
