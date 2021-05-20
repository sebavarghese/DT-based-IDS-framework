FROM ubuntu:18.04
# COPY ./src .
COPY ./start.sh ./start.sh
RUN apt-get update
RUN apt-get install -y sudo \
    && apt-get install -y python2.7 \
    && apt-get install -y python-pip \
    && apt-get install -y iputils-ping \
    && apt-get install -y net-tools \
    && apt-get install -y git \ 
    && apt-get install -y screen \
    && apt-get install -y vim \
    && git clone git://github.com/mininet/mininet \
    && /mininet/util/install.sh -a \
    && pip install minicps \
    && pip install cpppo==4.1.0 \
    && apt-get install -y ettercap-common \
    && apt-get install -y hping3 \
    && chmod +x ./start.sh
EXPOSE 6633 6653 6640

CMD ["./start.sh"]
