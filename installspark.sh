#!/bin/bash
                                             
sudo apt update
sudo apt install wget
sudo apt install python3-pip -y
sudo apt install openjdk-8-jdk-headless -y
wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
tar -xvf spark-3.3.2-bin-hadoop3.tgz
sudo rm *tgz
python3 -m pip install pyspark==3.5.0 --user
python3 -m pip install pandas --user
python3 -m pip install matplotlib --user
spark-3.3.2-bin-hadoop3/sbin/start-master.sh
echo "Started master spark"

