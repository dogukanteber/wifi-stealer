#!/usr/bin/python3

import subprocess, re

MESSAGE = """
    This script only retrieves WPA2-Personel authenticated Wi-Fi passwords.
    If you cannot find desired Wi-Fi password that may be because of the Wi-Fi
    is using WPA2-Enterprise authentication.
"""

print(f"\n\n\nATTENTION\n\n\n{MESSAGE}\n\n\n")

list_user_profiles_command = "netsh wlan show profiles"

user_profiles = subprocess.run(list_user_profiles_command, shell=True, capture_output=True, text=True)

user_profiles = user_profiles.stdout.split("\n")

profiles = []

for profile in user_profiles:
    regex = re.findall('Profile\s*:\s(.*)', profile)
    if regex:
        profiles.append(regex[0])
        
key_contents = list()

for profile in profiles:
    user_profile_command = f"""netsh wlan show profile "{profile}" key=clear"""
    user_profile = subprocess.run(user_profile_command, shell=True, capture_output=True, text=True, errors="ignore")      
    password = re.search("(Content\s*:\s)(.*)", user_profile.stdout)
    if password:
        key_contents.append(f"{profile} : {password.group(2)}")
    
print("\n".join(key_contents))
