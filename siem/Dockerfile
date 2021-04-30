FROM ubuntu:18.04

USER root
WORKDIR /root

#COPY ENTRYPOINT.sh /
COPY run.py ./run.py
COPY start.sh ./start.sh

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    python2.7 \
    python-pip \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    git \
    x11-xserver-utils \
    xterm \
    ettercap-graphical \
 && pip install --upgrade setuptools \
 && pip install minicps \
 && pip install cpppo==4.1.0 \
 && git clone https://github.com/FrauThes/DigitalTwin-SIEM-integration.git \
 && rm -rf /var/lib/apt/lists/* \
# && chmod +x /ENTRYPOINT.sh \
 && chmod +x ./start.sh \
 && chmod 777 ./run.py

RUN cd DigitalTwin-SIEM-integration/src/ && mv /root/run.py run.py

EXPOSE 6633 6653 6640

#ENTRYPOINT ["/ENTRYPOINT.sh"]
CMD ["./start.sh"]
