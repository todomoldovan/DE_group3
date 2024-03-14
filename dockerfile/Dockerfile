FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-8-jre-headless
RUN apt install -y scala wget nano screen
RUN wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
RUN tar -xvf spark-3.5.1-bin-hadoop3.tgz
RUN mv spark-3.5.1-bin-hadoop3/ /usr/local/spark
RUN rm spark-3.5.1-bin-hadoop3.tgz
ENV PATH="${PATH}:$SPARK_HOME/bin"
ENV SPARK_HOME="/usr/local/spark"
ENV SPARK_NO_DAEMONIZE="true"
RUN apt-get update && apt-get install -y python3
RUN apt install python3-pip -y
RUN python3 -m pip install pyspark==3.5.1 net-tools
ENV PATH="$HOME/.local/bin:$PATH"
RUN wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
RUN tar -xvf hadoop-3.3.6.tar.gz
RUN rm hadoop-3.3.6.tar.gz
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
RUN mkdir dn
COPY ./hdfs-site.xml hadoop-3.3.6/etc/hadoop/hdfs-site.xml
COPY ./core-site.xml hadoop-3.3.6/etc/hadoop/core-site.xml
RUN apt install openjdk-8-jdk-headless
