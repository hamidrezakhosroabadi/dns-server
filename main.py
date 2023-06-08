"""
A simple DNS server that listens for incoming DNS requests and responds with a fake IP address.

Usage:
1. Modify the `TARGET_IP` and `TARGET_TTL` variables to specify the fake IP address and time-to-live value for the response.
2. Start the DNS server by running the script.
3. Configure your DNS clients to use the IP address of the machine running the server as their primary DNS server.

Example:
    To start the DNS server listening on all network interfaces on port 53 with a fake IP address of '127.0.0.1' and TTL of 60:

        $ python dns_server.py

Attributes:
    TARGET_IP (str): The fake IP address to include in the DNS response.
    TARGET_TTL (int): The time-to-live value to include in the DNS response.
    LISTEN_IP (str): The IP address to listen on for incoming DNS requests.
    LISTEN_PORT (int): The port number to listen on for incoming DNS requests.

Classes:
    Handler: A request handler class that handles incoming DNS requests.
"""

from socketserver import ThreadingUDPServer, DatagramRequestHandler
from dnslib import DNSRecord, RR, A

TARGET_IP = '127.0.0.1'
TARGET_TTL = 60
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 53


class Handler(DatagramRequestHandler):
    """
    A request handler class that handles incoming DNS requests.

    Attributes:
        None

    Methods:
        handle: Handles incoming DNS requests and responds with a fake IP address.
    """

    def handle(self) -> None:
        """
        Handles incoming DNS requests and responds with a fake IP address.

        Args:
            None

        Returns:
            None
        """
        data = self.rfile.read(512)
        request = DNSRecord.parse(data)
        for question in request.questions:
            requested_domain_name = question.get_qname()
            response = request.reply()

            response.add_answer(
                RR(requested_domain_name, rdata=A(TARGET_IP), ttl=TARGET_TTL))  # Fake the address
            self.wfile.write(response.pack())


udp_sock = ThreadingUDPServer((LISTEN_IP, LISTEN_PORT), Handler)
udp_sock.serve_forever()
