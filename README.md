# Python-Based Onshape Part Coloring

This allows you to re-color all parts within a document based on a defined set of colors. By default, it colors parts based on descending order of bounding-box size. You must provide a document ID and workspace ID.

---

### Local Setup

Install the dependencies:

* Python 2 (2.7.9+)
* pip
* virtualenv

Then, from this folder:

--for Linux:
```sh
$ virtualenv -p /path/to/python2 env && source env/bin/activate
```

--for Windows:
```sh
$ virtualenv -p /path/to/python2.exe env && env/Scripts/activate.bat
```
References:

* https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate
* https://virtualenv.pypa.io/en/stable/userguide/#activate-script

You can now install the needed Python packages:

--for Linux:
```sh
$ pip install -r requirements.txt
```

--for Windows:
```sh
$ pip install -r requirements-win.txt
```

The windows-specific requirements file encompasses libraries that work for Win-OS

References:
* https://pypi.python.org/pypi/pyreadline

To exit the virtual environment at any time, simply type `deactivate`.

### Running the App

Create a `creds.json` file in the root project directory, with the following format:

```json
{
    "https://cad.onshape.com": {
        "access_key": "ACCESS KEY",
        "secret_key": "SECRET KEY"
    }
}
```

Just replace "ACCESS KEY" and "SECRET KEY" with the values you got from the
developer portal. To test on other stacks, you'll create another object in the file,
with credentials for that specific stack.

To specify your color scheme:
Open color_palette.json and add/change/delete color definitions within the dictionary. Specify the colors to be used and their default ordering within the "default_rotation" list.

To specify which document and workspace to update:
Open app.py and change the global variables DOCUMENT_ID and WORKSPACE_ID to be those of the document and workspace you'd like to update.

To run the basic application:

```sh
$ python app.py
```


### Working with API Keys

For general information on Onshape's API keys and how they work, read this
[document](https://github.com/onshape/apikey/blob/master/README.md).