import socket

COMMON_PORTS = [21,22,25,53,80,110,143,443,3306,8080]


def scan_ports(hosts):

    results = {}

    for host in hosts:

        open_ports = []

        for port in COMMON_PORTS:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((host, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        results[host] = open_ports

    return results