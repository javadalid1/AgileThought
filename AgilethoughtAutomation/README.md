
You must clone the project in your local machine using git clone command.

To install the TestProject Python OpenSDK, you need first to install Python, a Python code Editor and you are good to go.


To create a new python virtual environment, do the following:

Using the terminal, or cmd; go to the main directory in which you want to create the virtual env:

**cd my-directory**

And type the following commands:

**sudo pip3 install virtualenv** (or without sudo for Windows)

**python3 -m venv .venv**

This creates a subdirectory called .venv that contains the virtual environment.

**python3 -m venv /path/to/new/virtual/environment**

Activate the virtual environment with this command:

**source venv/bin/activate**

We need to ensure that pip is installed:

**python -m ensurepip -U**

Then, ensure that the testproject SDK is installed on it by running the following command:

**pip3 install testproject-python-sdk**

As a prerequisite, you must need to add an agent in TestProject, register it and be sure it is running.

To run a test you only need to run the following command in the terminal or cmd:

**pytest test/file/location.py**

Add the **-s** parameter at the end of the command if you want the execution 
to pause where indicated in the code.
