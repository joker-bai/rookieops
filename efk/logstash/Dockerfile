FROM centos:centos7
LABEL "auth"="rookieops" \
      "mail"="rookieops@163.com"
ENV TIME_ZONE Asia/Shanghai

# install JAVA
ADD jdk-8u131-linux-x64.tar.gz /opt/
ENV JAVA_HOME /opt/jdk1.8.0_131
ENV PATH ${JAVA_HOME}/bin:${PATH}

# install logstash
ADD logstash-7.1.1.tar.gz /opt/
RUN mv /opt/logstash-7.1.1 /opt/logstash