# SMTP Server Mass checker
Easy script on python for mass checking authorization on SMTP servers

How to use?

1. Create combo txt list with SMTP credentials like: smtp_server|port|login|password
2. Put file permissions: chmod +x script.py
3. Run script: python script.py credentials

Script authomatic checking authorization connection with SMTP servers on ports 465/587. 

Example:

```
$ python script.py credentials.txt
FAILED: xxxxx@xxxxx:xxx - SMTP Server: smtp.xxxx.xxx - Port: 587
SUCCESS: xxxxx@xxxxxx.xxx - SMTP Server: smtp.xxxx.xxx - Port: 465
```
