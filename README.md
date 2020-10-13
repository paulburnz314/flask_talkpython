### First steps for the python project
1. Make a new project folder
1. Via command prompt navigate to cd c:\users\...\project_folder
1. python -m venv venv  # set up the virtual env
1. 'venv\Scripts\activate'  # activate the virtual env
1. python -m pip install --upgrade pip  # uninstalls pip-20.1.1 then install pip-20.2.2
1. Set up the .gitignore file with at least /venv, *.pyc and __pycache__/
1. Create an \app folder
1. Set up a basic requirements.txt folder (copy portions from previous project)
1. Run 'pip install -r requirements.txt'
1. The venv\Lib\site-packages will now contain quite a few packages

### Running the application
1. set FLASK_APP=run.py
1. set FLASK_ENV=development
1. flask run