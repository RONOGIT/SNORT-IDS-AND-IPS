# Integrating Python for Email Alerts
#Set up email notifications when a critical alert is triggered.

import smtplib
from email.mime.text import MIMEText

def send_email_alert(alert_msg):
    msg = MIMEText(alert_msg)
    msg['Subject'] = 'Snort Alert Detected'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)
        print("Email alert sent!")

# Usage within log monitoring
def monitor_snort_alerts_with_email(logfile):
    for line in tail_logfile(logfile):
        print(f"ALERT: {line}")
        if "Potential SYN flood" in line:  
            send_email_alert(line)

# Example 
monitor_snort_alerts_with_email('/var/log/snort/alert')
