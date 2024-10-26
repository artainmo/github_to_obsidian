# github_to_obsidian
Personal project. Program to transfer and synchronize all my github repositories into my obsidian. 

## Steps to create
1. Be able to collect all repository links from a user. \
2. Iterate over all projects, to get all its files and then files inside their directory. \
3. Remove in github itself, files or directories that should not be there.
4. Skip certain directories such as .git or submodules or ones related to external library or config files.
5. For synchronization, verify if each file already exists, and if it exists see if its contents are similar and tags are similar.
6. Copy the README files into Obsidian with as obsidian file name its github path.
7. Copy code files and place the code between backtilts to display properly in markdown.
8. Each obsidian file should have a 'view on github' link in its footer. The root file of a project should contain its tags.
9. Use github actions to do the verification once a day.
