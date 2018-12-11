import re

#line = "sh /opt/LookAhead/Gigaspaces/Scripts/STAGE-CDC/ATC/scripts_per/deploy_Perspective_zone.sh"
line = "/opt/LookAhead/Gigaspaces/Deployments/STAGE/ATC/"
env = "STAGE-PDC"
project = "ATC"
suffix = "Deployments"
reStr = r'(/{0}/(\w*-*\w*)/{1}/)'.format(suffix, project)
pattern = re.compile(reStr, re.M | re.I)
match = re.findall(pattern, line)

for matched in match:
    token = matched[1]
    print(token)