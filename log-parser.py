#!/usr/bin/env python3
import sys

LOG_FILE = "OpenSSH_2k.log" # Change to "Apache_2k.log" as needed

# Unified attack patterns for Web (Apache) and SSH
attack_patterns = [
    # Web / SQLi / XSS
    "SELECT * FROM", "' OR '1'='1", "DROP TABLE", "<script>", "union select",
    # SSH / Auth Attacks
    "POSSIBLE BREAK-IN ATTEMPT!", "Failed password", "Invalid user", "authentication failure"
]

try:
    with open(LOG_FILE, "r") as log_file:
        search_ip = input("Enter the IP address to search for (e.g., 173.234.31.186): ")
        print(f"\n--- Scanning {LOG_FILE} ---\n")

        alert_count = 0
        
        for line in log_file:
            line = line.strip()

            # 1. Check IP match
            if search_ip in line:
                print(f"[IP MATCH]: {line}")
            
            # 2. Check for attack patterns
            for pattern in attack_patterns:
                if pattern.lower() in line.lower():
                    print(f"[!] ALERT - {pattern}: {line}")
                    alert_count += 1

        print(f"\n--- Scan Complete. Total Security Alerts: {alert_count} ---")

except FileNotFoundError:
    print(f"Error: {LOG_FILE} not found. Please check the filename.")