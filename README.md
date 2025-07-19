# Windows Vulnerability Scanner

The **Windows Vulnerability Scanner** is a lightweight Python script designed to scan Windows systems for basic security misconfigurations 
and vulnerabilities. This tool is aimed at cybersecurity learners and professionals who want to understand how system-level weaknesses
can be identified through automation.

---

## Features

- Detects:
  - Missing critical Windows updates
  - Weak or misconfigured password policies
  - Open and insecure ports
  - Guest account status
  - User Account Control (UAC) settings
  - Firewall and antivirus status
- Text-based scan output for easy review
- Minimal dependencies and fast execution

---

## Requirements

- Windows Operating System
- Python 3.x

---

## Installation

1. Clone the repository:
https://github.com/your-username/windows-vulnerability-scanner.git

2. Run the script:
python scanner.py


**Note:** Administrator privileges are recommended for a complete scan.

---

## Sample Output
[INFO] Operating System: Windows 10 Pro (64-bit)
[INFO] Logged-in User: Administrator
[OK] Firewall is enabled
[WARNING] Guest account is active
[WARNING] Password policy is weak (min length < 8)
[WARNING] Missing critical updates
[OK] Antivirus is active


---

## Screenshots

> *(Add screenshots here if you want, using Markdown image syntax)*  
> `![Scan Output Screenshot](screenshots/output.png)`

---

## Roadmap

- [ ] GUI integration using Tkinter
- [ ] Export results to PDF or HTML
- [ ] Real-time CVE mapping through public APIs
- [ ] Scheduler for automated scans
- [ ] CVSS score display for known issues

---

## Disclaimer

This tool is intended **for educational and authorized security auditing purposes only**.  
**Do not use this scanner on systems you do not own or have explicit permission to test.**  
Unauthorized usage may be illegal and is strictly discouraged.

---

## License

This project is licensed under the MIT License.  

---

## Author

**Saravana Priyan**  
Cybersecurity Blue Teamer | Vulnerability Researcher  
[LinkedIn](https://www.linkedin.com/) 


