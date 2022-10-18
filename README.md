# dash-issue
## Steps

### Create Python virtual env
Run `python -m venv .` in the project root to create a virtual env.

Run `source bin/activate` to activate the virtual env.

Run `pip3 install -r requirements.txt` to install the required package. Note the Dash 2.5.1
is added to the dependency. Along with pandas 1.5.0

## Start the server
Run `python3 example/dash/server.py` to start the server. The default setup is expected to
fail due to the hot reload bug.

More details see: example/dash/server.py Line 21 - Line 27.
