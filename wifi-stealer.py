#!/usr/bin/python3

import subprocess, smtplib, re

command = 'netsh wlan show profiles'

output_profiles = subprocess.run(command, shell=True, capture_output=True, text=True)

profiles = []

for profile in output_profiles.stdout.split('\n'):
    regex = re.findall('Profile\s*:\s(.*)', profile)
    if regex != []:
        profiles.append(regex[0])
        
result = ""

for profile in profiles:
    final_command = "netsh wlan show profile " + profile + " key=clear"
    final_output = subprocess.run(final_command, shell=True, capture_output=True, text=True)
    result += "Showing results for " + profile + ":\n" + final_output.stdout + "\n"
    
print(result)