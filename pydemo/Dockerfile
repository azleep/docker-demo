FROM ubuntu:latest

USER root

RUN apt -y update && apt -y upgrade && \
    apt -y install vim \
        python3 \
        python3-pip

RUN pip3 install bottle

#CMD ["python3", "/opt/workspace/demo.py"]
#ENTRYPOINT ["python3", "/opt/workspace/demo.py"]
#ENTRYPOINT ["echo", "zug"]
