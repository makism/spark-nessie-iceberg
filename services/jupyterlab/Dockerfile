FROM eclipse-temurin:8

RUN apt-get update
RUN apt-get install -y \
    iputils-ping \
    python3 \
    python3-pip \
    python3-dev \
    libsasl2-dev \
    curl \
    vim \
    wget \
    software-properties-common \
    ssh \
    net-tools \
    ca-certificates \
    rsync
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /opt/workspace

EXPOSE 8888

CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=