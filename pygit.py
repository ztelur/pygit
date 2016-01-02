#! /user/bin/python
import sys
import getopt
import os
git = 'git'
pull_cmd = 'pull'
checkout_cmd = 'checkout'
branch_cmd = 'branch'
status_cmd = 'status'
clone_cmd = 'clone'
git_dir = ".git"
def main(argv):
	print str(argv)
	if len(argv) <=0:
		return
	cmd = argv[0]
	if (isAdd(cmd)):
		addAll()
	if (isCommit(cmd)):
		commit();
	if (isStash(cmd)):
		stash(argv[:])
	if isPull(cmd):
		pull(argv[1])
	if isClone(cmd):
		clone(list(argv[1:]))
	if isCheckout(cmd):
		checkout(argv[1])
def isAdd(str):
	return 'add' == str.lower()	
def isCommit(str):
	return 'commit' == str.lower()
def isStash(str):
	return 'stash' == str.lower()
def isClone(str):
	return 'clone' == str.lower()	
def isPull(str):
	return 'pull' == str.lower()
def isCheckout(str):
	return "checkout" == str.lower()
def addAll():
	execute_cmd = git + " add --all . "
	trackAndExecute(execute_cmd)
def commit():
	execute_cmd = git + " commit "
	trackAndExecute(execute_cmd)
def push(branchs):
	execute_cmd = git + " push origin " + branchs
	trackAndExecute(execute_cmd)
def stash(argv):
	execute_cmd = git + " stash "
	if (len(argv) == 2):
		execute_cmd = git + " stash " + "apply"
	trackAndExecute(execute_cmd)
def trackAndExecute(cmd):
	cwd = os.getcwd()
	for repo in os.listdir(cwd):
		if (os.path.isdir(repo)):
			os.chdir(repo)
			if (os.path.exists(git_dir)):
				print repo + " " + cmd
				os.system(cmd)
			os.chdir(cwd)

def pull(branchs):
	execute_cmd = git + " " + pull_cmd +" origin " + branchs
	trackAndExecute(execute_cmd)
def checkout(branchs):
	execute_cmd = git + " " + checkout_cmd + " " + branchs
	trackAndExecute(execute_cmd)
def clone(init_url):
	print init_url;
	for url in init_url:
		execute_cmd = git+" "+clone_cmd+" "+url
		print "execute "+execute_cmd
		os.system(execute_cmd)

if __name__ == "__main__":
   main(sys.argv[1:])

