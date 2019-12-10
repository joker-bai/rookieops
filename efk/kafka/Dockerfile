FROM centos:centos7
LABEL "auth"="rookieops" \
      "mail"="rookieops@163.com"
ENV TIME_ZONE Asia/Shanghai

# install JAVA
ADD jdk-8u131-linux-x64.tar.gz /opt/
ENV JAVA_HOME /opt/jdk1.8.0_131
ENV PATH ${JAVA_HOME}/bin:${PATH}

# install kafka
ADD kafka_2.11-2.3.1.tgz /opt/
RUN mv /opt/kafka_2.11-2.3.1 /opt/kafka
WORKDIR /opt/kafka
EXPOSE 9092 
CMD ["./bin/kafka-server-start.sh", "config/server.properties"]
