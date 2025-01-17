import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
import subprocess

# Function to run PowerShell commands and display output in the app
def run_scan():
    output_text.delete("1.0", ttk.END)  # Clear previous output
    
    # PowerShell commands for security checks
    commands = [
        "Write-Output 'Scanning for open ports...'; Get-NetTCPConnection | Where-Object { $_.State -eq 'Listen' } | Select-Object LocalPort",
        "Write-Output '\nChecking firewall status...'; (Get-NetFirewallProfile -Profile Domain,Public,Private).Enabled",
        "Write-Output '\nChecking for user accounts without passwords...'; Get-WmiObject -Class Win32_UserAccount | Where-Object { $_.PasswordRequired -eq $false } | Select-Object Name"
    ]
    
    for command in commands:
        process = subprocess.Popen(
            ["powershell.exe", "-Command", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if stdout:
            output_text.insert(ttk.END, stdout + "\n")
        if stderr:
            output_text.insert(ttk.END, f"Error: {stderr}\n")
    
    output_text.insert(ttk.END, "\nLocal network scan starting...\n")
    output_text.see(ttk.END)
    scan_local_network()

# Function to scan for vulnerable hosts on the local network
def scan_local_network():
    try:
        # Replace IP range with your local network range
        ip_range = "192.168.1.0/24"
        output_text.insert(ttk.END, f"Scanning network: {ip_range}\n")

        # Run nmap scan
        process = subprocess.Popen(
            ["nmap", "-sV", "-T4", "-O", "-F", ip_range],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if stdout:
            output_text.insert(ttk.END, "Network Scan Results:\n" + stdout + "\n")
        if stderr:
            output_text.insert(ttk.END, f"Error during network scan: {stderr}\n")
    except FileNotFoundError:
        output_text.insert(ttk.END, "Error: Nmap is not installed or not found in PATH.\n")
    except Exception as e:
        output_text.insert(ttk.END, f"Unexpected error: {str(e)}\n")
    output_text.see(ttk.END)

# Create the main UI window with a ttkbootstrap theme
app = ttk.Window(themename="darkly")  # Choose theme: 'darkly', 'journal', 'solar', etc.
app.title("Windows Vulnerability Scanner")
app.geometry("900x700")

# Add a title label
title_label = ttk.Label(app, text="Windows Vulnerability Scanner", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Add a button to trigger the scan
scan_button = ttk.Button(app, text="Start Scan", command=run_scan, bootstyle=SUCCESS)
scan_button.pack(pady=10)

# Add a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(app, wrap="word", width=90, height=30, font=("Courier", 10))
output_text.pack(pady=10, padx=10)

# Run the Tkinter event loop
app.mainloop()
