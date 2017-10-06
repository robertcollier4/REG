## REG - Syntax Package for Sublime Text 2/3

Windows Registry Script (.reg) Language package for SublimeText. Includes syntax highlighting, comments toggling, declaration snippets, a build system to merge current reg file to registry, and a `Jump To Reg Key` command.

The `Jump To Reg Key` command will use the key name enclosed in square brackets at the location of your keyboard caret and jump to it in your registry editor.

By default this is done using Windows Registry Editor (aka regedit). You can specify to use a different registry editor by selecting the menu item `Preferences > Package Settings > REG > REG Settings - User` and modifying the `reg_editor` entry, and setting `use_regedit` to `false`.

Settings specified in REG.sublime-settings in your User folder are retained even when the package is updated.
