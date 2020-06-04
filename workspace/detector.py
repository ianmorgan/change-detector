# may need 'pip install paramiko' beforehand

import subprocess
import yaml
import sys

old_commit = sys.argv[1]
new_commit = sys.argv[2]


def components_to_check():
    config = yaml.load(open("workspace/config.yaml"))
    return config["components"]


def detect_changed_component(old_commit, new_commit, component, collector):
    cmd = "git diff --stat " + old_commit + " " + new_commit + " -- repo/" + component["path"]
    result = subprocess.check_output(cmd.split())
    if result:
        collector.append(component["name"])

def detect_all_changes(old_commit, new_commit, components, collector):
    for name, component in components.items():
        component["name"] = name  # add the name into the dict
        detect_changed_component(old_commit, new_commit, component, collector)


print ("now run detector")

# keep all the results here
result = {"changesDetected": [],
          "inputs": {"lastCommit": old_commit, "newCommit": new_commit}}


detect_all_changes(old_commit, new_commit, components_to_check(), result["changesDetected"])

# write out the results
with open('workspace/changes.yml', 'w') as yaml_file:
    yaml.dump(result, yaml_file, default_flow_style=False)

print ("Changes detected to components: " + ",".join(result["changesDetected"]))
print ("Full results are are in 'workspace/changes.yml'")


