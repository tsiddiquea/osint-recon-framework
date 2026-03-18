import requests

def scan_directories(hosts):

    findings = []

    with open("wordlists/directories.txt") as f:
        dirs = [d.strip() for d in f]

    for host in hosts:

        for d in dirs:

            for proto in ["http://", "https://"]:

                url = f"{proto}{host}/{d}"

                try:

                    r = requests.get(url, timeout=3)

                    if r.status_code in [200,301,302,403]:
                        findings.append((url, r.status_code))

                except:
                    pass

    return findings