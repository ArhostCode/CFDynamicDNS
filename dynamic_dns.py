import CloudFlare
import requests

DOMAIN = "DOMAIN"
DNS_DOMAIN = "DNS.DOMAIN"
TOKEN = "CLOUDFLARE_TOKEN"
EMAIL = "EMAIL"


def main():
    ip = requests.get('https://api.ipify.org').text
    zone_name = DOMAIN
    cf = CloudFlare.CloudFlare(token=TOKEN, email=EMAIL)

    zone_info = cf.zones.get(params={'name': zone_name})
    zone_id = zone_info[0]['id']
    dns = cf.zones.dns_records.get(zone_id)

    dns_id = ""

    for dns_record in dns:
        if dns_record['name'] == DNS_DOMAIN:
            dns_id = dns_record['id']

    dns_record = {
        'name': DNS_DOMAIN,
        'type': 'A',
        'content': ip,
        'proxied': True
    }

    r = cf.zones.dns_records.put(zone_id, dns_id, data=dns_record)
    exit(0)


if __name__ == '__main__':
    main()
