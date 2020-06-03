# Change Detector 

A simple change detector to monitor a git repo at a folder level to see 
what has changed between commits. This can then be fed into a build pipeline to selectively 
build, test and deploy just the affected components.

The basic building block is the `git diff` command, for example:

```bash 
## Full change details 
git diff 50a6eea 8857709 -- repo/componentA

### Just the stats
git diff --stat 50a6eea 8857709 -- repo/componentA

### Nothing changed for componentB between these commits 
git diff --stat 50a6eea 8857709 -- repo/componentB
```
