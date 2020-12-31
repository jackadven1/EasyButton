"""
SOURCES:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

#LONG DESCRIPTION
long_description = (here / "README.md").read_text(encoding = "utf-8")

setup(
	name = "pybutton",
  	version = "1.0.0",
  	description = "Easily create interactible button objects in PyGame with just a few short lines of code.",
  	long_description = long_description,
  	long_description_content_type = "text/markdown",
  	url = "https://github.com/jackadven1/PyButton",
  	author = "William Deforest Halsted IV; @jackadven1",
  	author_email = ""
  	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Education"",
		"Topic :: Education :: Games/Entertainment",
		"Natural Language :: English",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python 3 :: Only",
		"Programming Language :: Python 3",
		"Programming Language :: Python 3.5",
		"Programming Language :: Python 3.6",
		"Programming Language :: Python 3.7",
		"Programming Language :: Python 3.8"
	]
	keywords = "pygame, pygame-games, pygame-application, student, easy-to-use, simple, interface, menu, graphical-user-interface, graphical-interface, button",
	packages = find_packages(where = "src"),
	python_requires = ">= 3.5, <4",
	install_requires = ["pygame"]
	project_urls = {
		"Funding": "https://donate.pypi.org",
        "Say Thanks!": "https://saythanks.io/to/william%40thehalsteds.net",
        "Source": "https://github.com/pypa/sampleproject/"
	}
)
license_files = LICENSE.md
