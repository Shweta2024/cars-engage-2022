# Contributing Guidelines

This documentation contains a set of guidelines to help you in contributing to this project. 
I'm happy to welcome all the contributions from anyone willing to improve/add new scripts to this project.
Thank you for helping out and remember,
**no contribution is too small.**


## Step-1 : Fork the Project
- Fork this Repository. This will create a Local Copy of this Repository on your Github Profile. Keep a reference to the original project in `upstream` remote.

```
$ git clone https://github.com/<your-username>/cars-engage-2022
$ cd cars-engage-2022
$ git remote add upstream https://github.com/Shweta2024/cars-engage-2022
```

![fork](https://user-images.githubusercontent.com/75883328/170811931-d41b2456-3668-4758-aa5b-4e2839dcc976.png)


## Step-2 :  Create a virtual environment
- Creating a virtual environment isolates the libraries and scripts installed into it from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system. 

```
# It will install virtualenv
$ pip install virtualenv

# You can create a virtualenv using the following command:
$ virtualenv my_name

# To specify Python interpreter of your choice use the below command:
$ virtualenv -p /usr/bin/python3 virtualenv_name

# Now activate the virtual environment with the below command:
$ source virtualenv_name/bin/activate

```

## Step-3 : Download requirements.txt
```
# This will download all the required libraries 
$ pip3 install -r requirements.txt 
```
## Step-4 : Branch
Create a new branch. Use its name to identify the issue your addressing.
```
# It will create a new branch with name Branch_Name and switch to that branch 
$ git checkout -b branch_name
```

- After you've made changes or made your contribution to the project add changes to the branch you've just created by:
```
# To add all new files to branch Branch_Name
$ git add .
```

## Step-5 : Commit


- To commit give a descriptive message for the convenience.
```
# This message get associated with all files you have changed
$ git commit -m "message"
```

## Step-6 : Work Remotely
- When your work is ready and complies with the project conventions, upload your changes to your fork:

```
# To push your work to your remote repository
$ git push -u origin Branch_Name
```

## Step-7 : Pull Request
- Go to your repository in browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution.

- Congratulations ! Your Pull Request has been successfully submitted.
