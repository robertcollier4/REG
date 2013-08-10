REG - Syntax Package for Sublime Text 2/3
============

Windows Registry Script (.reg) Language package for SublimeText. Includes syntax highlighting, comments toggling, declaration snippets, a build system to merge current reg file to registry, and a `Jump To Reg Key` command.

The `Jump To Reg Key` command will use the key name enclosed in square brackets at the location of your keyboard caret and jump to it in your registry editor. By default this is done using SysInternals RegJump (included in the package folder) to jump to the registry key in the default Windows Registry Editor. You can specify to use a different registry editor by making a copy of `Preferences > Package Settings > REG > REG Settings - Default` at `Preferences > Package Settings > REG > REG Settings - User` and modifying the `RegKeyJumpCmd` entry. Any settings you specify in REG.sublime-settings in your User folder will overwrite the settings in REG.sublime-settings in the package folder - and thus your custom settings will be retained even when the files of this package update.
