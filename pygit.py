#! /user/bin/python
import sys
import getopt
import os
git = 'git'
pull_cmd = 'pull'
checkout_cmd = 'pull'
branch_cmd = 'branch'
status_cmd = 'status'
clone_cmd = 'clone'
def main(argv):
	print str(argv)
	if len(argv) <=1:
		return
	cmd = argv[0]
	if isPull(cmd):
		pull()
	if isClone(cmd):
		clone(list(argv[1:]))
def isClone(str):
	return 'clone' == str.lower()	
def isPull(str):
	return 'pull'==str.lower()
def pull():
	print "pull"
def checkout():
	print "checkout"
def clone(init_url):
	print init_url;
	for url in init_url:
		execute_cmd = git+" "+clone_cmd+" "+url
		print "execute "+execute_cmd
		os.system(execute_cmd)

if __name__ == "__main__":
   main(sys.argv[1:])

