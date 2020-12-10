# Using Virtualenv

---

## Using built in venv

* Using venv(which is a subset of [virtualenv](https://virtualenv.pypa.io/en/latest/)), which is the recommended method for creating virtual environments starting Python 3.5. and comes inbuilt.

* lets name the local environment Ab-local

  ```bash
  python -m venv Ab-local
  ```

* To activate, run the script on windows terminal

  ```bash
  Ab-local\Scripts\activate.bat
  ```

  On git-bash or linux

  ```bash
  # cd to Ab-local\Scripts, then run
  . activate
  ```

* To deactivate, just type deactivate with environment active

  ```bash
  deactivate
  ```

## Creating virtual environment with virtual environment wrapper

* The advantages of [virtualenvwrapper](https://parbhatpuri.com/virtualenvwrapper-on-top-of-virtualenv.html)
* Install the package, `pip install virtualenvwrapper-win`
* operations,

  ```python
  # Create virtual environment
  mkvirtualenv <envname>

  # Active VE
  workon <envname>

  # Deactivate VE
  deactivate

  # Remove the created environment
  rmvirtualenv <envname>
  ```

* To uninstall any package use `pip uninstall <pkg_name>`
* Other env tools include, [pipenv](https://pipenv.readthedocs.io/en/latest/), it combines package and environment management support into a single tool.
* pipenv is more advanced, find about how to use it [here](https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44).
* If needed isolation between python versions use, [pyenv](https://github.com/yyuu/pyenv).
* For a comparison use this [link](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe).
* virtualenvwrapper installed in the path, `C:\Users\User1\AppData\Local\Programs\Python\Python38\Scripts`
* There is a problem with virtualenvwrapper-win, it got bat scripts needs cmd to run. Use virtualenv or venv for use in bash.

## Using virtualenv

---

1. install virtualenv('Already installed if virtualenvwrapper installed'), `pip install virtualenv`
2. creating a virtual environment, `virtualenv ENV_NAME`.
3. Activating, llr to venv, `cd scripts then, . activate.`
4. deactivating is similar to the venv, to remove simply remove the directory with rm
