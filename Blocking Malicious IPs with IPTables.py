#Blocking Malicious IPs with IPTables
#Extend the project to block malicious IPs detected by Snort using iptables.
import subprocess

def block_ip(ip_address):
    try:
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'], check=True)
        print(f"Blocked IP: {ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking IP: {e}")

def monitor_and_block(logfile):
    for line in tail_logfile(logfile):
        if "Potential SYN flood" in line:  
            ip_address = extract_ip_from_log(line)  
            block_ip(ip_address)

def extract_ip_from_log(log_line):
    # Extracts the IP from Snort log (adjust regex based on log format)
    import re
    match = re.search(r'[0-9]+(?:\.[0-9]+){3}', log_line)
    if match:
        return match.group(0)
    return None

# Example 
monitor_and_block('/var/log/snort/alert')
