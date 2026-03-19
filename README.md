# Osint Recon Framework

## Overview

The Osint Recon Framework is a Python-based cybersecurity reconnaissance framework designed to automate the initial intelligence-gathering phase of security assessments and penetration testing workflows.

This project demonstrates how automated scanning techniques can be integrated into a structured pipeline to efficiently map the external attack surface of a target domain.

By combining network probing, HTTP analysis, DNS enumeration, and directory discovery mechanisms, the tool simulates real-world reconnaissance methodologies used in professional cybersecurity operations.

The system emphasizes defensive security awareness, structured data collection, and report generation for analytical review.


## Core Capabilities

The framework performs multi-stage reconnaissance tasks including:

* Automated subdomain enumeration using wordlist-driven DNS resolution
* Identification of live hosts through HTTP service verification
* Network port scanning across commonly targeted service ports
* Discovery of exposed directories and hidden endpoints
* Concurrent scanning for improved efficiency
* Structured generation of reconnaissance reports in both text and JSON formats
* Modular architecture allowing future integration of additional reconnaissance modules

This design mirrors reconnaissance workflows followed during vulnerability assessments and red-team exercises.

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
git clone https://github.com/tsiddiquea/recon-tool.git
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

## Performance Characteristics

* Lightweight implementation optimized for local execution
* Parallel host verification using thread pooling
* Fast socket-based port probing
* Minimal system resource utilization
* Scalable architecture suitable for expanding reconnaissance datasets


## Security & Ethical Considerations

This tool is developed strictly for:

* Cybersecurity learning and research
* Defensive security simulations
* Authorized penetration testing environments
* Academic demonstrations of reconnaissance methodologies

Unauthorized scanning or misuse against systems without explicit permission is strongly discouraged.


## Learning Outcomes

Through the development and use of this project, the following cybersecurity competencies are demonstrated:

* Practical reconnaissance automation design
* Understanding of network service exposure risks
* Web attack surface discovery techniques
* Secure software structuring for offensive security tooling
* Data analysis and report generation for security intelligence
* Modular cybersecurity tool engineering


## Author

Developed as part of a hands-on cybersecurity engineering initiative focused on reconnaissance automation, secure coding practices, and real-world defensive security awareness.


## License

This project is released for educational and research purposes only.
Users must ensure responsible usage within authorized and ethical cybersecurity contexts.

