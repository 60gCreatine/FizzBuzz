print("PyCharm code change worked")
# For the git to work, I had to do the following:
#       1. Add my ssh via ssh-add ~/.ssh/id_ed25519 // ~ is just saying the home directory
#               Current ssh can be seen via ssh-add -l
#               To test a git ssh, you can do ssh-add -T git@github.com, if correct it will return your username
#
#       2. After this, I had to remove the old HTTPS remote url for the repo
#           2.1 Check current remote URL via git remote -v
#           2.2 Change it to SSH via git remote set-url origin (SHH URL FOR REPO)

