# texstudio-template
Collect User templates for everyone to use

## How to contribute
Basically this describes the process of generating a pull-request on github. For further question, please google as there are lots of tutorials.
* fork this git repository
* clone the fork to your computer
* checkout a new branch 
* make your own template in TeXstudio with `File/Make Template`
* copy the generated files from `.config/texstudio/templates/user` (OSX/Linux) or `%appdata%\texstudio\templates\user` (win) to your cloned repository. Please use subfolder to sort like `university` for university templates. The names need to be meaningful for a global audience.
* Multi-file templates need to be generated manually, see [manual](https://texstudio-org.github.io/background.html#the-document-template-format) and [example](https://github.com/texstudio-org/texstudio/tree/master/templates) template_Book.(json/png/zip)
* push the branch to your fork.
* On github activate "make pull request" or similar
