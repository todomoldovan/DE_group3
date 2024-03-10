#!/bin/bash

tee hadoop-3.3.6/etc/hadoop/core-site.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://172.18.0.2:9000</value>
    </property>
</configuration>
EOF

tee hadoop-3.3.6/etc/hadoop/hdfs-site.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>dfs.name.dir</name>
        <value>/nn</value>
    </property>
</configuration>
EOF

hadoop-3.3.6/bin/hadoop namenode -format

