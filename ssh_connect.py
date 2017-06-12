#!/usr/bin/python

import sys
import json
import os 
from subprocess import  call, check_output
import yaml

##debug
from pprint import pprint
from pathlib2 import Path


def kinit():
  op = check_output(['klist', '--json'])
  klistJson = json.loads(op)  
  if len(klistJson) == 0:
    call(["kinit"])

def run_ssh(serverName, config):
  call(["ssh", config['user'] + "@" + serverName, "-K"])

def getConfiguration():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	contents = Path(dir_path + "/parameter.yml").read_text()
	return yaml.load(contents)
	
config = getConfiguration()
serverConfig = config['server']

## =========== Main script =============== ##
if len(sys.argv) < 2:
  print "Needs argument : " + str(serverConfig.keys())
  exit()

arg1 = sys.argv[1]

kinit()

if (arg1 in serverConfig):
  run_ssh(serverConfig[arg1]['name'], config)
else:
  print "Ssh '" + arg1 + "' doesn't exist"