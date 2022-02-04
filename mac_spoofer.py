#!/usr/bin/env python

import subprocess
import optparse


def arguments_func():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
	parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("\033[1;31m [x] Please specify an interface, use --help for more info")
	elif not options.new_mac:
		parser.error("\033[1;31m [x] Please specify a new MAC address, use --help for more info")
	else:
		return options

def mac_changer(interface, new_mac):
	print("\033[1;34m Your current MAC address is: " + str(subprocess.check_output(["ifconfig", interface]).split()[11][0:17]))
	print("\033[1;33m [+] Changing MAC address for " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])
	print("\033[1;32m Successfully changed MAC address for " + interface + " to " + new_mac)


(options) = arguments_func()
mac_changer(options.interface, options.new_mac)
