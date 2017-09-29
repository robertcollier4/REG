from __future__ import print_function
import sublime, sublime_plugin
import subprocess
from os import environ
import re

class jumptoregkeyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regkey = self.view.substr(self.view.line(self.view.sel()[0].begin()))
		openbracketpos = regkey.find('[')
		closebracketpos = regkey.find(']')
		if( (openbracketpos != -1) and (closebracketpos != -1)):
			regkey = regkey[openbracketpos+1:closebracketpos]
			# print(regkey.find('-'))
			if(regkey.find('-') == 0): # remove the - if its a delete reg key
				regkey = regkey[1:]
			# print(regkey)
			use_regedit = sublime.load_settings("REG.sublime-settings").get("use_regedit")
			if use_regedit == True:  # modify regedit settings to make it start in selected key
				# expand abbreviated registry rootkey
				rootmap = {
					"HKLM": "HKEY_LOCAL_MACHINE",
					"HKCU": "HKEY_CURRENT_USER",
					"HKCR": "HKEY_CLASSES_ROOT",
					"HKU" : "HKEY_USERS",
					"HKCC": "HKEY_CURRENT_CONFIG"
				}
				rootregexp = re.compile(r'^(%s)(?=\\)' % '|'.join(rootmap.keys()))
				regkey = rootregexp.sub(lambda match: rootmap[match.group(1)], regkey)
				regkey = 'Computer\\' + regkey  # the LastKey data (below) requires Computer path
				regexec = environ['SystemRoot'] + '\\system32\\reg.exe'
				# print(regexec)
				reglastkeypath = 'HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit'
				# reg add reglastkey /v LastKey /d regkey /f
				reglastkeycmd = '%s ADD %s /v LastKey /d "%s" /f' % (regexec, reglastkeypath, regkey)
				# print("reglastkeycmd:" + reglastkeycmd)
				thisproc = subprocess.Popen(reglastkeycmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				output = thisproc.communicate()[0]
				regjumpcmd = environ['SystemRoot'] + '\\regedit.exe' # just call regedit, it should open to target path
			else:  # else pass selected key to custom regjumper cmd
				regjumpcmd = sublime.load_settings("REG.sublime-settings").get("reg_editor")
				regjumpcmd.append(regkey)
			thisproc = subprocess.Popen(regjumpcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			# print(thisproc.communicate()[0])
		else:
			print("Error: Line does not contain a valid Reg Key enclosed in square brackets")

