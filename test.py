import os
print("doing run smb")
os.system("smbclient -N -c \'recurse ON; prompt OFF; mget *\' //192.168.10.10/dev_share")
