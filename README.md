This is a TLS/SSL secure connection using Python.

Prerequisite:

-generate a private key and certificate using the following commands:

--openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key
--openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt

How to run:
copy privatekey.key and certificate.crt to /home/user1/ folder.

-Server side:
--python ssl_server.py

-Client side:
--python ssl_client.py

