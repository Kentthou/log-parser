#!/usr/bin/env python3
import sys

# Set the file you want to scan
LOG_FILE = "OpenSSH_2k.log" 

# Unified list of "red flag" patterns
attack_patterns = [
    # Web / SQLi / XSS
    "SELECT * FROM", "' OR '1'='1", "DROP TABLE", "<script>", "union select",
    # SSH / Auth Attacks
    "POSSIBLE BREAK-IN ATTEMPT!", "Failed password", "Invalid user", "authentication failure"
]

try:
    with open(LOG_FILE, "r") as log_file:
        # Ask for the Target IP
        search_ip = input("Enter the IP address to search for: ")
        
        # Ask if we should show everything or just the target's actions
        filter_choice = input("Show ALL security alerts in the file? (y/n): ").lower()
        
        print(f"\n--- Scanning {LOG_FILE} ---\n")

        alert_count = 0
        
        for line in log_file:
            line = line.strip()
            
            # 1. Check if the line belongs to our Target IP
            is_target_ip = search_ip in line
            
            # 2. Check if the line contains a "red flag" pattern
            found_pattern = None
            for pattern in attack_patterns:
                if pattern.lower() in line.lower():
                    found_pattern = pattern
                    break # Stop looking for more patterns once one is found

            # LOGIC FOR PRINTING:
            # Always print if the IP matches exactly
            if is_target_ip:
                print(f"[IP MATCH]: {line}")

            # Only print the alert if:
            # a) We found a pattern AND the user wants to see everything (y)
            # b) We found a pattern AND it belongs to our target IP
            if found_pattern:
                if filter_choice == 'y' or is_target_ip:
                    print(f"[!] ALERT - {found_pattern}: {line}")
                    alert_count += 1

        print(f"\n--- Scan Complete. Total Security Alerts Shown: {alert_count} ---")

except FileNotFoundError:
    print(f"Error: {LOG_FILE} not found. Please check the filename.")
