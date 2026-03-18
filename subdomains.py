import socket

def enumerate_subdomains(domain):

    results = []

    with open("wordlists/subdomains.txt") as f:
        words = [w.strip() for w in f]

    for word in words:

        sub = f"{word}.{domain}"

        try:
            socket.gethostbyname(sub)
            results.append(sub)
        except:
            pass

    return results