=====================
StARLinG Sphinx Theme
=====================

A Sphinx Theme for `StARLinG Lab <https://starling.utdallas.edu>`_ Documentation.

Installation & Getting Started
------------------------------

1. Clone the repository

  .. code-block:: bash

    $ git clone git@github.com:batflyer/starling_theme.git
    $ python setup.py develop

2. This repository uses itself as a theme. Build the documentation with Sphinx and open it with a browser.

  .. code-block:: bash

    $ cd documentation
    $ make html
    $ firefox build/html/index.html

Project State & Current Goals
-----------------------------

This repository is in an *Exploratory Phase*. The goal is to create a documentation theme which blends seamlessly with the StARLinG Website, but exactly how this may be achieved is up for debate.

**Open Problems:**

* Better navigation (``wy-nav-side`` and ``wy-grid-for-nav`` are currently dumped as links on each page rather than having a navigation menu).
* Standardize the color scheme (rather than defaulting to ``rtd_sphinx_theme`` colors).
* Unit tests for building certain page elements.
* Documentation for building/deploying.
* [*Maybe*]: Hook into the ``starling-lab/starling.utdallas.edu`` repository to automatically copy portions of the header and footer.

License
-------

Copyright © 2018, Alexander L. Hayes

Distributed under the terms of the MIT License. See the LICENSE at the base of the repository for details.
