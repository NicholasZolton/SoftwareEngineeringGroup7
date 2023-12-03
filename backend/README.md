# Running In General

To run this project, first make sure to create a python virtual environment with `python -m virtualenv ./.venv` and activate it.

Next, make sure to install the requirements with `pip install -r requirements.txt`.

After that, you should be able to run `flask run` in this subdirectory (`project/backend`) and when it starts you should see
something like the following: `Running on http:127.0.0.1:5000`.

This means that the server has started and everything is working, so you can go ahead and start the frontend successfully.

# Running Tests

To run the unit tests, follow the above steps up to `pip install -r requirements.txt` to make sure you have the virtual environment
set up, and then go ahead and run the `project/backend/tests.py` file with `python tests.py`.

This will run all the tests and you should see something like `Ran 14 tests. x.xxxs` followed by `OK`.

Please feel free to reach out over Teams if anything is not working.