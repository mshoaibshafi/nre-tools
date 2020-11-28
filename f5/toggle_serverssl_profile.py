###################################################################################
# toggle_serverssl_profile.py
#
# author: mS - mshoaibshafi AT gmail.com
# BIGREST version: 1.3.1
# BigIP OS Version: 13.1.3.4
# Python Version: 3.8.2
#
###################################################################################
'''
This module will toggle ServerSSL Profile on a Virtual Server
if serverSSL applied it will remove it
if serverSSL not applied it will add it

This one will use BIGREST instead of f5-SDK (f5-common-python)
''' 

import getpass
from bigrest.bigip import BIGIP
from bigrest.utils.utils import rest_format

profile_name = "serverssl"

# Get username, password, and ip
print("Username: ", end="")
username = input()
password = getpass.getpass()
print("Device IP or name: ", end="")
ip = input()
print("Virtual Server Name: ", end="")
domain_name = input()

print(f"Domain Name is: {domain_name}")

# Connect to BigIP
b = BIGIP(ip, username, password)

# Load the Profiles on a virtual server
profiles = b.load(f"/mgmt/tm/ltm/virtual/{rest_format(domain_name)}/profiles")

print(f"List of Profiles attached to {domain_name}")
profile_context_list = []
for p in profiles:
    profile_context_list.append(p.properties["context"])
print(profile_context_list)

if "serverside" in profile_context_list:
    print("Serverside SSL applied")
    print("Deleting Serverside SSL profile")
    path = (
      f"/mgmt/tm/ltm/virtual/{rest_format(domain_name)}/profiles/{rest_format(profile_name)}"
    )
    b.delete(path)
else:
    print("Serverside SSL doesn't applied")
    print("Adding Serverside SSL Profile")
    data = {}
    data["name"] = profile_name
    data["context"] = "serverside"
    b.create(f"/mgmt/tm/ltm/virtual/{rest_format(domain_name)}/profiles", data)
