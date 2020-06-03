# may need 'pip install paramiko' beforehand

import subprocess


def detect_changes(old_commit, new_commit, path):
    cmd = "git diff --stat " + old_commit + " " + new_commit + " -- " + path
    print(cmd)
    result = subprocess.check_output(cmd.split())
    return result


print ("now detector")

result = subprocess.check_output(['ls', '-l'])
print(result)

print (detect_changes("50a6eea", "8857709", "repo/componentA"))
