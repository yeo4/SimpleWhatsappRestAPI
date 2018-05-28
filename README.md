# SimpleWhatsappRestAPI
Simple Whatsapp Rest API using yowsup-cli and python


## Installation

 - Requires python2.6+, or python3.0 +
 - Required python packages: python-dateutil,
 - Required python packages for end-to-end encryption: protobuf, pycrypto, python-axolotl-curve25519
 - Required python packages for yowsup-cli: argparse, readline (or pyreadline for windows), pillow (for sending images)

1. you need to download the lib 

# lib:
```
pip install yowsup2
```
```
pip install bottle
```
2. you need to registration to Whatsapp
https://github.com/tgalal/yowsup/wiki/yowsup-cli-2.0

3. you need to update the run.py file with the phone and the password from the registration (line 21)
```
CREDENTIALS = ("49XXXXXXXX", "XXXXXXXXXXXXX=") # replace with your phone and password
```
4. you need to set a password to access the REST-API on server.py (line 38)
```
    def Password(self,password):
        return (password == 'PASSWORD')
```

### Linux
```
sudo mv WhatsAppRestAPI /opt/
cd /opt/WhatsAppRestAPI/
chmod u+x *.sh
```

5. to make a systemctl:
```
sudo nano /etc/systemd/system/WhatsAppRestAPI.service
```
edit the user to your user
```
[Unit]
Description=MDA bot Whatsapp
[Service]
Type=forking
WorkingDirectory=/opt/WhatsAppRestAPI/
User=XXXXXX
ExecStart=/opt/WhatsAppRestAPI/startup.sh
ExecStop=/opt/WhatsAppRestAPI/shutdown.sh
Restart=always
[Install]
WantedBy=multi-user.target
```

to active the systemctl run this command:

```
sudo systemctl daemon-reload
sudo systemctl enable WhatsAppRestAPI
sudo systemctl start WhatsAppRestAPI
sudo systemctl status WhatsAppRestAPI
```
