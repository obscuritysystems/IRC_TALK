import subprocess
output=subprocess.Popen(["ls", "-lah"], stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
print output
