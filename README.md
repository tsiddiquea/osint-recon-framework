# Recon Automation Tool

## Overview

The Recon Automation Tool is a Python-based cybersecurity reconnaissance framework designed to automate the process of external attack surface discovery.

This project simulates real-world penetration testing reconnaissance phases including subdomain enumeration, service detection, directory probing, and structured intelligence reporting.

The tool demonstrates how security analysts and ethical hackers gather preliminary information about a target environment before performing deeper security assessments.

## Key Features

* Automated subdomain enumeration using DNS resolution
* Detection of live hosts through HTTP service validation
* Fast scanning of commonly exposed network ports
* Directory and endpoint discovery using customizable wordlists
* Multithreaded scanning for improved performance
* Structured report generation in both TXT and JSON formats
* Modular architecture for easy extension and experimentation
* Lightweight design suitable for lab and research environments


## Project Structure
```
recon-tool/
│
├── recon.py              → Main automation engine
├── subdomains.py         → Subdomain enumeration module
├── http_check.py         → Live host detection logic
├── port_scan.py          → Socket-based port scanner
├── dir_scan.py           → Directory discovery module
├── report.py             → Report generation engine
│
├── wordlists/
│   ├── subdomains.txt
│   └── directories.txt
│
└── README.md
```

## Installation

1. Clone the repository
```
git clone https://github.com/Tahsina-Siddiquea/recon-tool.git
cd recon-tool
```
2. Install dependencies
```
pip install requests
```

## Usage

Run the reconnaissance tool by providing a target domain.
```
python recon.py --target example.com
```
The tool will automatically:

* Enumerate possible subdomains
* Identify which subdomains are alive
* Scan open network ports
* Probe for exposed directories
* Generate structured reconnaissance reports


## Example Output
```
Starting recon on example.com

Subdomains Found:
admin.example.com
api.example.com
dev.example.com

Live Subdomains:
admin.example.com → HTTP 200
api.example.com → HTTP 301

Open Ports:
admin.example.com → 80, 443

Interesting Directories:
http://admin.example.com/admin → 200
http://admin.example.com/api → 403

Report saved:
example.com_recon_report.txt
example.com_recon_report.json
```


## Performance

* Efficient concurrent host verification
* Low-latency socket scanning operations
* Minimal memory footprint
* Scalable design for larger reconnaissance wordlists
* Optimized for fast local execution

## Learning Outcomes

This project demonstrates practical cybersecurity engineering skills such as:

* Automated reconnaissance workflow development
* Network scanning and socket programming
* Web exposure detection techniques
* Multithreaded security tool design
* Security data aggregation and reporting
* Attack surface mapping methodologies


## Security & Ethical Use

This tool is intended strictly for:

* Cybersecurity learning and experimentation
* Authorized penetration testing labs
* Academic research and security demonstrations

Do not scan systems without proper permission.


## Author

Developed as part of hands-on cybersecurity research focusing on reconnaissance automation and offensive security tooling.


## License

This project is released for educational use and research purposes.
