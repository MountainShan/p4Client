from scapy.all import *
from subprocess import Popen,PIPE
import os, time

'''
P4Client command connector (v.0.1)
	This is a prototype of P4 runtime command sender.
	Main feature (including module designing): 
		> 1. Basic flow entry generator (mirroring, default entries, flow entries)
		> 2. P4 switch script analysis (JSON file analysis) (in process)
'''

class P4CLI : 
	def __init__(self, numOfSwitch):
		self.switch = ["./commandSender/%s.sh" % str(50000 + x) for x in xrange(numOfSwitch)]
		# self.switch = ["path for all client in bmv2"]
				
	def mirrorAdd(self, switchCLI, idx, portNo):
		# Mirroring Port... (for generating monitor packet)
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		cmd = ['mirroring_add', str(idx), str(portNo)]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
		
	def setDefault_table(self, switchCLI, tableName, action):
		# Setuo default table data
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		cmd = ['table_set_default', tableName, action]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
	
	def matchAction_Table(self, switchCLI, tableName, action, matchData=None, actionData=None):
		# Setup match+action action
		if type(matchData) == list :
			matchDataArray =''.join(str(matchData[e])+" " for e in xrange(len(matchData)))
		else:
			matchDataArray = matchData
		if type(actionData) == list:
			actionDataArray =''.join(str(actionData[e])+" " for e in xrange(len(actionData)))
		else:
			actionDataArray = actionData
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		if matchData is None:
			cmd = ['table_add', tableName, action, '=>', actionDataArray]
		elif actionData is None:
			cmd = ['table_add', tableName, action, matchDataArray, '=>']
		else :
			cmd = ['table_add', tableName, action, matchDataArray, '=>', actionDataArray]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
		
	def setRegister(self, switchCLI, registerName, registerIDX, value):
		# Setup registerValue
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		cmd = ['register_write', registerName, str(registerIDX), value]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
	
	def readRegister (self, switchCLI, registerName, registerIDX):
		# read register result
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		cmd = ['register_read', registerName, str(registerIDX)]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
		
	def readCounter (self, switchCLI, counterName, counterIDX):
		this_dir = os.path.dirname(os.path.realpath(__file__))
		p = Popen(os.path.join(this_dir, switchCLI), stdout=PIPE, stdin=PIPE)
		cmd = ['counter_read', counterName, str(counterIDX)]
		output = p.communicate(input=''.join(cmd[x]+' ' for x in xrange(len(cmd))))[0]
		#print output
		
