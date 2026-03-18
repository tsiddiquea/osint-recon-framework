import json

def generate_report(domain, subs, alive, ports, dirs):

    txt_file = f"{domain}_recon_report.txt"
    json_file = f"{domain}_recon_report.json"

    with open(txt_file, "w") as f:

        f.write("===== Recon Report =====\n\n")

        f.write("Subdomains:\n")
        for s in subs:
            f.write(f"{s}\n")

        f.write("\nLive Subdomains:\n")
        for k,v in alive.items():
            f.write(f"{k} -> {v}\n")

        f.write("\nOpen Ports:\n")
        for host,p in ports.items():
            if p:
                f.write(f"{host} -> {', '.join(map(str,p))}\n")

        f.write("\nInteresting Directories:\n")
        for url,status in dirs:
            f.write(f"{url} -> {status}\n")

    data = {
        "subdomains": subs,
        "live": alive,
        "ports": ports,
        "directories": dirs
    }

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nReport saved to:")
    print(txt_file)
    print(json_file)