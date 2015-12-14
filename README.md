This is a simple script designed to update a DNS record for a domain administered on DigitalOcean with the current IP of the machine the script runs on. This is particularly useful if you're running a server from your home with a changing IP.

Required environment variables:

* `DIGITALO_API_KEY`: Your DigitalO API Token
* `DIGITALO_DOMAIN_NAME`: The associated domain name (i.e. `example.com`)
* `DIGITALO_DOMAIN_RECORD_ID`: The domain record id that you wish to keep updated.
