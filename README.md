# github_to_obsidian
Personal project. Program to transfer and synchronize all my github repositories into my obsidian. 

## Steps to create
1. Be able to collect all repository links from a user.
2. Create script that git clones all those repositories, not its submodules.
3. For synchronization, verify if each file already exists, and if it exists see if its contents are similar and tags are similar.
4. Copy the README files into Obsidian with as obsidian file name its github path.
5. Copy code files and place the code between backtilts to display properly in markdown.
6. Each obsidian file should have a 'view on github' link in its footer. The root file of a project should contain its tags.
7. Use github actions to do the verification once a day.
