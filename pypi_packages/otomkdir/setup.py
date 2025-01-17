from setuptools import setup, find_packages
import codecs
import os

version = "0.0.1.4"

description = "to automate creation of folders and subfolders"

with open( "README.md", "r" ) as f:
    long_description = f.read( )

# setting up
setup(
     name = "otomkdir"
    , version = version
    , author = "mose_tucker_0159"
    , author_email = "mose.tucker.0159@gmail.com"
    , description = description
    , long_description = long_description
    , long_description_content_type = "text/markdown"
    , packages = find_packages( )
    , install_requires = [

      ]
    , keywords = [ "python" ]
    , classifiers = [
             "Development Status :: 1 - Planning"
            ,  "Intended Audience :: End Users/Desktop"
            ,  "Programming Language :: Python :: 3"
            ,  "Operating System :: Microsoft :: Windows"
      ]
)
