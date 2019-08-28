# Pillar Kata: word search

# Setup and Installation

First, you'll need to create the virtual environment for the project:
```bash
make env
```
To activate:
```bash
source env/bin/activate
```
Once the virtual environment has been activated, install the project
dependencies:
```bash
make init
```
To run the tests:
```bash
make test
```
Lastly, there are few ways to install and run the application, but perhaps the
easiest is to simply run it from the root of the repository with:
```bash
python -m wordsearch <FILE>
```
Alternatively, you may install it using the `setup.py` file that is included in
the project:
```bash
pip install .
```
# Uninstall

If you'd like to uninstall the package while still maintaining the virtual
environment, then use pip:
```bash
pip uninstall wordsearch
```
Or, you could just deactivate the environment:
```bash
deactivate
```
# Documentation

The documentation for this project is written in RST format, and an HTML version
can be generated based on the docstring in each module, class, method, and 
function. To generate the documentation, follow these steps:
```bash
cd docs
make html
```
Once the documentation generates, open the `build/html/index.html` file in a
web-browser to view.
