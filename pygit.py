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
	if len(argv) <=1:
		return
	cmd = argv[0]
	if isPull(cmd):
		pull()
	if isClone(cmd):
		clone(list(argv[1:]))
	if isCheckout(cmd):
		checkout(argv[1])
def isClone(str):
	return 'clone' == str.lower()	
def isPull(str):
	return 'pull' == str.lower()
def isCheckout(str):
	return "checkout" == str.lower()
def pull():
	print "pull"
def checkout(branchs):
	cwd = os.getcwd()
	for repo in os.listdir(cwd):
		if os.path.isdir(repo):
			print "cd "+ repo
			os.chdir(repo)
			if (os.path.exists(git_dir)):
				execute_cmd = git + " " + checkout_cmd + " " + branchs
				print repo + " " + execute_cmd
				os.system(execute_cmd)
			os.chdir(cwd);
	print "checkout finish"
def clone(init_url):
	print init_url;
	for url in init_url:
		execute_cmd = git+" "+clone_cmd+" "+url
		print "execute "+execute_cmd
		os.system(execute_cmd)

if __name__ == "__main__":
   main(sys.argv[1:])

