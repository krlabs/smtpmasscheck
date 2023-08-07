# SMTP_Server_Mass_checker
Easy script on python for mass checking authorization on SMTP servers

How to use?

1. Create combo txt list with SMTP credentials like: login|password|smtp_server|port
2. Put file permissions: chmod +x script.py
3. Run script: python script.py credentials

Script authomatic checking authorization connection with SMTP servers on ports 465/587. 

For example:

```
$ python script.py credentials <br>
FAILED: xxxxx@xxxxx:xxx - SMTP Server: smtp.xxxx.xxx - Port: 587 <br>
SUCCESS: xxxxx@xxxxxx.xxx - SMTP Server: smtp.xxxx.xxx - Port: 465
```
