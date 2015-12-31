#! /user/bin/python
import sys
import getopt
import os
def git = 'git'
def pull_cmd = 'pull'
def checkout_cmd = 'pull'
def branch_cmd = 'branch'
def status_cmd = 'status'
def clone_cmd = 'clone'
def main(argv):
	if len(argv) <=1:
		return
	if isPull(cmd):


def isPull(str):
	return cmp('pull',str.lower())

def pull():
	print "pull"
def checkout():
	print "checkout"

def clone(init_url):
	for(url:init_url):
		execute_cmd = git+" "+clone_cmd+" "+url
		print "execute "+execute_cmd
		os.system(execute_cmd)



