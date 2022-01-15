# cxoratest

Purpose is to test using temporary lob of cx_oracle python library.  

Uses oracle docker image below.  

https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g

By default, the password verification is disable(password never expired)
Connect database with following setting:

hostname: localhost
port: 49161
sid: xe
username: system
password: oracle
Password for SYS & SYSTEM

SQL Developer can be installed using these instructions: https://dev.to/ishakantony/how-to-install-oracle-sql-developer-on-ubuntu-20-04-3jpd

Default location for jdk: /usr/lib/jvm/jdk-17/


instant client install help: https://askubuntu.com/questions/159939/how-to-install-sqlplus
https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/install-instant-client-using-zip.html#GUID-D3DCB4FB-D3CA-4C25-BE48-3A1FB5A22E84
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4:$LD_LIBRARY_PATH
ln -s /opt/oracle/instantclient_21_4/libclntsh.so.21.1 /opt/oracle/instantclient_21_4/libclntsh.so
ln -s /opt/oracle/instantclient_21_4/libocci.so.21.1 /opt/oracle/instantclient_21_4/libocci.so


# testing
export PATH=/opt/oracle/instantclient_21_4:$PATH
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4:$LD_LIBRARY_PATH
```bash

sqlplus

insert into test values (1, utl_raw.cast_to_raw('some magic here'));
```