import ssl

port = 8081

import socket, ssl

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Require a certificate from the server. We used a self-signed certificate
    # so here ca_certs must be the server certificate itself.
    ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED, ca_certs='/home/user1/server.crt')


    ssl_sock.connect(('127.0.0.1', 8081))

    ssl_sock.write(str(raw_input("Enter text : ")).encode())

    ssl_sock.close()

