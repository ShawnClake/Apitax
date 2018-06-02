from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'apitax',
  packages = find_packages(), # this must be the same as the name above
  version = '2.0.1',
  description = 'Apitax combines the power of Scriptax and COmmandtax into a quick and easy to use Python package to facillitate powerful Restful API Request Scripting',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Shawn Clake',
  author_email = 'shawn.clake@gmail.com',
  url = 'https://github.com/ShawnClake/Apitax', # use the URL to the github repo
  #download_url = '', # I'll explain this in a second
  keywords = ['restful', 'api', 'commandtax', 'scriptax'], # arbitrary keywords
  classifiers = (
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ),
  install_requires = [
    'click',
    'bottle',
    'requests',
    'antlr4-python3-runtime',
  ],
)