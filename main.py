#!/usr/bin/python

import os
import requests
from digitalocean import Domain, Record

API_TOKEN = os.environ.get('DIGITALO_API_KEY', '')
DOMAIN_NAME = os.environ.get('DIGITALO_DOMAIN_NAME', '')
DOMAIN_RECORD_ID = os.environ.get('DIGITALO_DOMAIN_RECORD_ID', '')


def main():
    domain = Domain().get_object(API_TOKEN, DOMAIN_NAME)
    record = Record().get_object(API_TOKEN, domain, DOMAIN_RECORD_ID)

    ip = requests.get('http://icanhazip.com').text.strip()

    record.data = ip

    record.save()

if __name__ == '__main__':
    main()
