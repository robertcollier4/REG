from __future__ import print_function
import sublime, sublime_plugin
import subprocess

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
			RegKeyJumpCmd = sublime.load_settings("REG.sublime-settings").get("RegKeyJumpCmd")
			RegKeyJumpCmd = [s.replace("{PACKAGE_PATH}", sublime.packages_path()) for s in RegKeyJumpCmd]
			RegKeyJumpCmd.append(regkey)
			# print(RegKeyJumpCmd)
			thisproc = subprocess.Popen(RegKeyJumpCmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			# output = thisproc.communicate()[0]
			# print(output)
		else:
			print("Error: Line does not contain a valid Reg Key enclosed in square brackets")

