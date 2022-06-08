# Dynamic DNS through CloudFlare (python script)
### Install
```
git clone https://github.com/ArhostCode/dyndnscf.git
pip install -r requirements.txt
```
### Configuration
1. Create A record in cloudflare
2. In dynamic_dns.py change
```
DOMAIN = "DOMAIN"  
DNS_DOMAIN = "DNS.DOMAIN"  
TOKEN = "CLOUDFLARE_TOKEN"  
EMAIL = "EMAIL"
```
### Usage
```
python dynamic_dns.py
```
