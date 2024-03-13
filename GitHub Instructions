Add A GitHub Repository To Your Local Machine

####In your favorite web browser (all users)

Go to your profile on github.com
Click on "Repositories"
Click "New" towards the top-right of the screen
Give your repository a name. Avoid spaces and silly characters
Give your repository a description. Be as descriptive as you can, explain the purpose of the repository
Set your repository to "public" or "private," I suggest public unless required to keep with the spirit of GitHub
Check the "Initialize this repository with a README" box unless you have already run git init in a directory via Terminal
If you know you want to ignore a specific code language, select it in the "Add .gitignore" dropbox, we can add specific folders and files to this later on
Give your repository a usage license. I suggest looking at this site; I prefer the MIT license
Click, "Create repository"
Clone your repository to your local machine
If you use the GitHub app
Open the GitHub app and make sure you are logged into your account using GitHub > Preferences, select "Accounts" and then enter your GitHub username and password, then click "Sign In"
Back in your browser, click on the "Clone in Desktop" button. It will automatically take you to the GitHub app and ask where you would like the repository cloned to
Choose the location and directory name for your local repository and click "Clone"
You can now right-click or control-click the name of your repository from the left sidebar and choose "Open in Atom" to quickly get to work
If you use terminal
On this new page (URL should be github.com/username/repo-name) find the SSH clone URL in the right menu and click the "Copy to clipboard" button. If it says "HTTPS clone URL" above the input box, click on the blue "SSH" link below, this will change the clone URL to use SSH instead of HTTPS, and then click on the "Copy to clipboard" button
####If using the GitHub app

Open the GitHub app and make sure you are logged into your account using GitHub > Preferences, select "Accounts" and then enter your GitHub username and password, then click "Sign In"
Your local repository should already be created (see above steps)
If you have worked on this project on another computer it is wise to push the "sync" button at the top-right before doing any further work on your current machine
Once your files have been edited you will need to add, commit, and sync those changes. There will be a list of files in the center column that, when highlighted, will show what has been changed in the preview window on the right. Select the files that you would like to add to a commit by checking the checkboxes to the left side of the file name.
Add a summary and a description for each commit, and then push the "Add to [branch name]" button.
Once all of your files have been committed, you can sync your repository by clicking the "sync" button at the top-right
Rejoice in all the GitHub simplicity
####If using Terminal

Move to the parent directory where you would like to clone your new GitHub repository. You will use a "/" to move deeper into your folder structure. If you have spaces in your folder names you will have to put a "" before them, like so: cd ~/School/HCC/Spring\ 2015/ART229/Projects. Note: It's quicker, easier, and less confusing if you can avoid using spaces in your directory names as much as possible (but not always possible)
Clone your GitHub repository to a new directory. There are two main ways to do this:
Create the new project repository as you are cloning your repository.
Run git clone git@github.com:username/project-name.git new-project-name you can paste your SSH clone URL in to replace the "git@github.com..." business and avoid any typo errors. You can also leave off the "new-directory-name" in which case your new directory's name will be the same as your GitHub repository's name when you created it. When (if) you designate your new directory's name in the clone command, you can use the same "" character to add a space to name, e.g. git clone git@github.com:username/project-name.git New\ Project\ Name
Note: If you get an error message about your directory already being a GitHub repository, you can change the remote URL by running git remote set-url origin git@github.com:username/project-name.git. This will change which remote repository your local machine points to when running git pull and git push. Avoid this if you can when just starting off. If you do this you will also have to do the following:
Run git fetch
Run git pull origin master. You will likely have merge conflicts, in which case you will have to open the specified files and edit them and then save them.
Run git add [name of file] e.g. "git add index.html" or run git add --all to add all changes to all files to your commit.
Run git commit -m "Write a message about your commit here"
Repeat the previous two steps until all files have been added and committed
Run git push origin master to push your changes to the remote repository.
Create a new directory where we can clone our GitHub repository into before cloning.
Create the new directory in your parent folder. You can use the same "" character before any spaces in your folder name, like so mkdir Project\ 1-Profile\ Page
Move into your new directory, cd Project\ 1-Profile\ Page
Run git clone git@github.com:username/project-name.git . and DO NOT forget the "." at the end. That "." represents the current directory (the one we just made and moved into), which tells GitHub to clone our repository into the directory that we're currently in
Open your repository in your favorite text editor open -a "Atom" . (note the "." again) and get to work!
Once you've edited your files you will need to add and commit them. Run git add [name of file] e.g. "git add index.html" or run git add --all to add all changes to all files to your commit.
Run git commit -m "Write a message about your commit here" 1.Repeat the previous two steps until all files have been added and committed
Run git push origin master to push your changes to the remote repository.
Rejoice in all of your GitHub mastery.
