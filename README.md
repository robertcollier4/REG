REG - Syntax Package for Sublime Text 2/3
============

Windows Registry Script (.reg) Language package for SublimeText. Includes syntax highlighting, comments toggling, declaration snippets, a build system to merge current reg file to registry, and a Jump To Reg Key command.

The Jump To Reg Key Command will use the key name enclosed in square brackets at the location of your keyboard caret and jump to it in your registry editor.

For the Jump To Reg Key command - this package by default uses SysInternals RegJump (included in the package folder) to open Windows Registry Editor at the location of a registry key. You can modify REG.sublime-settings if you would like to specify a different 3rd-party Registry Editor to invoke instead. You can access the settings file via Menu Preferences>Package Settings>REG. If you change your settings, you should make a copy of "REG - Default" at "REG - User" since then your settings will be retained through package updates.
