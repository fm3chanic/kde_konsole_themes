## fm3chanic Themes for KDE Konsole

This repository contains all color themes for the Konsole terminal emulator I've created so far.<br> 
Konsole is the main terminal emulator of the popular KDE desktop environment for Linux and integrated in Kate. The same themes are also available for Kate. You can find them [here](https://github.com/fm3chanic/ksyntaxhighlighting_themes).

Themes which have been created during my project of color theming Vtubers are in the directory "vtuber_project". The directory "other" contains all color themes which where created outside of the project.

**[HTML Reference Sheets & Galery Non-Project Themes](https://github.com/fm3chanic/color_schemes)**<br>
**[Vtuber Project | Information & Galery](https://github.com/fm3chanic/vtuber_project)**

> [!IMPORTANT]
> Please note that all color themes have been originally created for Notepad++, which has the tendency to show colors lighter as they are in other applications. Therefore it might occur that the color theme is a bit on the darker side.

### Installation:

Copy the theme file to `~/.local/share/konsole` and restart the application. 
The theme should now be selectable in the **Appearence** tab when editing your profile.

### Contribution:

The themes are based on the mapped template in directory **/tools**.<br>
The python script (_\[...\]\_load_colors.py_) reads the colors from a html file from [color_schemes](https://github.com/fm3chanic/color_schemes) and uses replace to fill in the colors.<br>

If you want to work on colors it makes the most sense to change the colors in repository [color_schemes](https://github.com/fm3chanic/color_schemes) so the changes can be applied to all applications using the theme.<br>
If you want to work on the mapping of the colors it might make sense to change the base template, so changes can be applied to all themes of this application.<br>

Neverless, **I also welcome contribution not following this standard**. The standard was made to keep it maintainable for one person, not to block community ideas.<br>