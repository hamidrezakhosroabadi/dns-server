# DNS-Server
### A simple DNS server that listens for incoming DNS requests and responds with a fake IP address.

Usage:
1. Modify the `TARGET_IP` and `TARGET_TTL` variables to specify the fake IP address and time-to-live value for the response.
2. Start the DNS server by running the script.
3. Configure your DNS clients to use the IP address of the machine running the server as their primary DNS server.

Example:
    To start the DNS server listening on all network interfaces on port 53 with a fake IP address of '127.0.0.1' and TTL of 60:

        $ python dns_server.py