# github_to_obsidian
Personal project. Program to transfer and synchronize all my public github repositories into my obsidian. 

This is useful because specific information can be found way faster via obsidian.

If a new file has been created or an existing file updated, the program will synchronize this in Obsidian repo, but it won't delete files in Obsidian that have been deleted in github. This is why repositories should only be made public once the code inside is finished to avoid syncronization problems with files deleted on github.

## Steps to create
1. Be able to collect all repository links from a user. \
2. Iterate over all projects, to get all its files and then files inside their directory. \
3. Remove in github itself, files or directories that should not be there. \
4. Skip certain directories and files such as .git or submodules or ones related to external library or config files. \
5. Create the markdown and code files. \
6. For synchronization, verify if each file already exists, and if it exists see if its contents are similar and tags are similar. \
7. Use github actions to do the verification once a day. \

## File management
##### Naming
Use github repository path as file name in obsidian.<br>
Transform '/' into '~'.<br>
Remove '.' if file name starts with that.<br>
Add '.md' extension in the end for obsidian.

##### Tags
Give tags of project to its root README.<br>
Give the 'from-github' tag to all files that come from github.<br>
If on a page of code you can detect the programming language via its extension, add this programming language as a tag.

##### Content
All files' content should be between backtilts as this is how code is displayed in obsidian markdown.<br>
Only README.md files' content should not be between backtilts. And also README.md files, if at root of repository, should start with the tags.<br>
The \<br\> HTML tags can be removed from README.md files for obsidian's markdown.<br>
All files should have the 'from-github' tag.<br>
All files should after the tags and before the content have a line saying: 'View this page on [github](appropriate_link). Only edit this page on github.'.

##### Files to skip
```
Files with no extension besides if makefile/Makefile/dockerfile/Dockerfile
.gitkeep
*.swp
a.out
.env
*.txt 
*.zip
*.csv 
*.svg 
*.png
*.jpg
*.ico
*.json 
*.storyboard
*.plist
telegraf.conf
grafana.db
wordpress.sql
.eslintrc.js
.prettierrc
*.lock
*.options
*.conf.in
*.map
*.pdf
*.bmp
*.rt
*.names
*.pkl
*.log
reportWebVitals.js
app.e2e-spec.ts
```

##### Directories to skip
```
*/*.xcworkspace
*/*.xcodeproj
*/utils/ft_printf
*/utils/get_next_line
*/utils/libft
*/libs/get_next_line
*/libs/libft
*/utils/minilibX
inception-of-things/p1
inception-of-things/p2
matcha/frontend
minishell-unittest/test/test
*/data
*/node_modules
*/js/vendor
webserv/conf
webserv/webserv/frontend
ft_printf/ft_printf
```

## Next things I could do
1. Delete files in Obsidian that have been deleted in github. Maybe do that by removing and regenerating all the files each time. 
2. Generate the files in a folder named 'github' instead of in the root. This is useful to segregate generated github files from files you have written, lowering the risk of injecting faulty generated files at the root in the middle of normal files, but also this is useful to allow plugins to exclude the github files (for example obsidian copilot can benefit from not indexing all the github files).
