# pip install python-whois
# pip install whois
from time import sleep
from os import system
import whois

RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
BLUE_BOLD = "\033[1;34m"
MAGENTA_BOLD = "\033[1;35m"
CYAN_BOLD = "\033[1;36m"
WHITE_BOLD = "\033[1;37m"

system("clear" or "cls")

bnr = GREEN_BOLD+"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║       PROJECT NAME v2.0          ─── Hacking Tool ───                ║
║                                                                      ║
╟──────────────────────────────────────────────────────────────────────╢
║                                                                      ║
║  GitHub   → https://github.com/hellobytecodes                        ║
║  Author   → MR.Byte                                                  ║
║  Purpose  → Security / OSINT                                         ║
║  Status   → Active Development (2026)                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
print(bnr)
print("")

domain = input(CYAN_BOLD+"(Enter Your Domain): "+YELLOW_BOLD)

w = whois.whois(domain)

def info_whois():
  print(f"Domain Name: {w.domain_name}")
  print(f"Registrar: {w.registrar}")
  print(f"Registrar URL: {w.registrar_url}")
  print(f"Reseller: {w.reseller}")
  print(f"Whois Server: {w.whois_server}")
  print(f"Referral URL: {w.referral_url}")
  print(f"Creation Date: {w.creation_date}")
  print(f"Expiration Date: {w.expiration_date}")
  print(f"Updated Date: {w.updated_date}")
  print(f"Status: {w.status}")
  print(f"Name: {w.name}")
  print(f"Organization: {w.org}")
  print(f"Address: {w.address}")
  print(f"City: {w.city}")
  print(f"State: {w.state}")
  print(f"Zip Code: {w.zipcode}")
  print(f"Country: {w.country}")
  print(f"Registrant Name: {w.registrant_name}")
  print(f"Registrant Organization: {w.registrant_organization}")
  print(f"Registrant Address: {w.registrant_address}")
  print(f"Registrant City: {w.registrant_city}")
  print(f"Registrant State: {w.registrant_state}")
  print(f"Registrant Zip: {w.registrant_zip}")
  print(f"Registrant Country: {w.registrant_country}")
  print(f"Registrant Email: {w.registrant_email}")
  print(f"Registrant Phone: {w.registrant_phone}")
  print(f"Admin Name: {w.admin_name}")
  print(f"Admin Organization: {w.admin_organization}")
  print(f"Admin Address: {w.admin_address}")
  print(f"Admin City: {w.admin_city}")
  print(f"Admin State: {w.admin_state}")
  print(f"Admin Zip: {w.admin_zip}")
  print(f"Admin Country: {w.admin_country}")
  print(f"Admin Email: {w.admin_email}")
  print(f"Admin Phone: {w.admin_phone}")
  print(f"Tech Name: {w.tech_name}")
  print(f"Tech Organization: {w.tech_organization}")
  print(f"Tech Address: {w.tech_address}")
  print(f"Tech City: {w.tech_city}")
  print(f"Tech State: {w.tech_state}")
  print(f"Tech Zip: {w.tech_zip}")
  print(f"Tech Country: {w.tech_country}")
  print(f"Tech Email: {w.tech_email}")
  print(f"Tech Phone: {w.tech_phone}")
  print(f"Billing Name: {w.billing_name}")
  print(f"Billing Organization: {w.billing_organization}")
  print(f"Billing Address: {w.billing_address}")
  print(f"Billing City: {w.billing_city}")
  print(f"Billing State: {w.billing_state}")
  print(f"Billing Zip: {w.billing_zip}")
  print(f"Billing Country: {w.billing_country}")
  print(f"Billing Email: {w.billing_email}")
  print(f"Billing Phone: {w.billing_phone}")
  print(f"Name Servers: {w.name_servers}")
  print(f"DNSsec: {w.dnssec}")
  print(f"Emails: {w.emails}")
  print(f"Whois Server: {w.whois_server}")
  print(f"Port 43: {w.whois_port43}")
  print(f"Raw Data: {w.text}")
  print(f"Python whois: {w.parser}")
    
info_whois()