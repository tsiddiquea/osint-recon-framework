import argparse
from subdomains import enumerate_subdomains
from http_check import check_alive
from port_scan import scan_ports
from dir_scan import scan_directories
from report import generate_report


def main():

    parser = argparse.ArgumentParser(description="Recon Automation Tool")
    parser.add_argument("--target", required=True, help="Target domain")

    args = parser.parse_args()
    domain = args.target

    print(f"\n[*] Starting recon on {domain}")

    print("\n[*] Enumerating subdomains...")
    subdomains = enumerate_subdomains(domain)

    print(f"\n[+] {len(subdomains)} Subdomains Found:\n")
    for sub in subdomains:
        print("   ", sub)

    print("\n[*] Checking which subdomains are alive...")
    alive = check_alive(subdomains)

    print(f"\n[+] {len(alive)} Live Subdomains:\n")
    for host, status in alive.items():
        print(f"   {host}  ->  {status}")

    print("\n[*] Running port scan on live subdomains...")
    ports = scan_ports(alive.keys())

    print("\n[+] Open Ports:\n")
    for host, open_ports in ports.items():
        if open_ports:
            ports_str = ", ".join(map(str, open_ports))
            print(f"   {host}  ->  {ports_str}")

    print("\n[*] Checking for exposed directories...")
    dirs = scan_directories(alive.keys())

    print("\n[+] Interesting Findings:\n")
    for url, status in dirs:
        print(f"   {url}  ->  {status}")

    print("\n[*] Generating report...")
    generate_report(domain, subdomains, alive, ports, dirs)


if __name__ == "__main__":
    main()