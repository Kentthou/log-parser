# Security Threats in Server Logs

## What is this?
This project is a record of my steps into making a log parser in python. I wanted to see if I could use a computer script to do the "heavy lifting" of a Security Analyst job, specifically, reading through thousands of lines of server activity to find signs of a malicious actor.

Instead of reading files manually, Ive used a Python tool that searches for specific people (IP addresses) and "bad behaviors" (attack patterns).

---

## How it works
1. **The Target:** I point the script at a log file (like a list of everyone who tried to log into a server).
2. **The Search:** The script asks me for an IP address.
3. **The Brain:** As the script reads every line, it looks for two things:
   - Does this line belong to the person(IP) I’m looking for?
   - Does this line contain "red flag" words like "Failed password" or "SQL Injection" attempts?
4. **The Result:** It prints out every match it finds and gives me a final count of how many security alerts were detected.

---

## Proof of Concept (Results)
To test the script, I ran it against a server log containing 2,000 entries. By searching for a specific suspicious IP, the script successfully flagged multiple "Brute Force" attempt patterns and provided a final tally of the threats found.


**1. Targeted Search (Filtered)**

By searching for IP 173.234.31.186 and choosing not to show all alerts (n), I can see exactly what this specific actor was doing:

Terminal output
```
Enter the IP address to search for: 173.234.31.186
Show ALL security alerts in the file? (y/n): n

--- Scanning OpenSSH_2k.log ---

[IP MATCH]: Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!
[!] ALERT - POSSIBLE BREAK-IN ATTEMPT!: Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!
...
--- Scan Complete. Total Security Alerts Shown: 8 ---
```

**2. Global Scan (Unfiltered)**

By choosing y, the script performs a wide-lens scan of the entire 2,000-line log file to gauge the overall threat level of the server.

Tail-end output
```
--- Scan Complete. Total Security Alerts Shown: 1477 ---
```

## What I Learned
### 1. Finding "Suspects"
Before running the script, I learned itd be best to use a terminal command to find a list of IP addresses. This saved me from having to open the giant text file and scroll forever just to find a test case.

**The command used:**
```
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" Apache_2k.log | head -n 1
```

### 2. Identifying "Digital Fingerprints"
Different types of attacks leave specific text "fingerprints" in a log.

**Web Attacks:** code snippets used to trick databases (e.g., ' OR '1'='1).

**Server Attacks:** repeated mistakes (e.g., Failed password or Invalid user).

## Citations & Resources
This project was built while following educational resources and using open-source data:

**Instructional Guide:** Based on a Python Log Parser tutorial on YouTube. [Link to Video](https://www.youtube.com/watch?v=I-bqmLSfcn8)

**Practice Data:**
The datasets used in this project are sourced from the **Loghub** repository:

> Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. *Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics.* IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.
