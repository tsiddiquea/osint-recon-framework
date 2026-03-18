import requests
from concurrent.futures import ThreadPoolExecutor


def check_host(sub):

    for proto in ["http://", "https://"]:

        try:
            r = requests.get(proto + sub, timeout=3)
            return (sub, f"{r.status_code} ({proto})")

        except:
            continue

    return None


def check_alive(subdomains):

    alive = {}

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_host, subdomains)

    for r in results:
        if r:
            alive[r[0]] = r[1]

    return alive