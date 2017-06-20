How to start your application README
--------------------------------------------------------------

- How to install pip::

The good news is that pip comes installed with virtualenv. We need to make sure though that we install pip and virtualenv for the correct version of Python on your computer. Open a terminal and run the following command:


    $ python --version

It should say something like the following:

    python --version
    Python 3.6.1

Find the instructions below to install virtualenv for the version of Python reported by your terminal.

You can install virtualenv using pip, which is included in Python 3.4+ installations:


    # If you get 'permission denied' errors, try running "sudo python" instead of "python"
    $ pip install virtualenv

Now activate the virtual environment.

    source bin/activate

- download or clone project in Terminal (OSX) or CMD (Window)
- $ git clone https://github.com/scheung38/qbe-flaskapp.git




- Install it::

	$ pip install -r requirements.txt

- Run it::

	$ fabmanager create-admin
	(Go through and create admin logins)


	$ fabmanager run

    Select Client Portfolio ->

	Login and create new items, UI allows CREATE, EDITS, DELETE


	API Endpoints are available in List Plans ->
	Initially will be empty, go ahead and click + to add to 'Add a new record'
	Fill in the required field -> Save

	Now it should populate landing page database showing item just created.
	Left if it are EDIT, DELETE, SEARCH buttons

    These end points are shown :

	http://localhost:8080/api/plans


to deactivate and exit back to normal shell:

    source/deactivate


That's it!!

