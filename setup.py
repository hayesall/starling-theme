# MIT License

# Copyright (c) 2018 Alexander L. Hayes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
``setup.py`` for ``starling_theme``
"""

from codecs import open as open_
from os import path
from setuptools import setup

from starling_theme import __version__

HERE = path.abspath(path.dirname(__file__))
with open_(path.join(HERE, "README.rst"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="starling_theme",
    version=__version__,
    license="MIT",
    author="Alexander L. Hayes",
    author_email="alexander@batflyer.net",
    url="https://github.com/batflyer/",
    description="Sphinx Theme for the StARLinG Lab.",
    long_description=LONG_DESCRIPTION,
    packages=["starling_theme"],
    package_data={"starling_theme": ["theme.conf", "*.html", "static/css/*.css"]},
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["starling_theme = starling_theme"]},
    install_requires=["sphinx"],
    classifiers=[
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation",
    ],
)
