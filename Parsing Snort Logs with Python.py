#Parsing Snort Logs with Python
#The Snort alerts are typically saved in /var/log/snort/alert. Use Python to monitor and parse the log file for real-time alerting.

import time

def tail_logfile(filename):
    with open(filename, 'r') as f:
        f.seek(0, 2)  # Move to the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)  # Sleep briefly to avoid busy-waiting
                continue
            yield line.strip()

def monitor_snort_alerts(logfile):
    print("Monitoring Snort alerts...")
    for line in tail_logfile(logfile):
        print(f"ALERT: {line}")

# Example usage
monitor_snort_alerts('/var/log/snort/alert')
