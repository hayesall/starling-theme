=====================
StARLinG Sphinx Theme
=====================

A Sphinx Theme for `StARLinG Lab <https://starling.utdallas.edu>`_ Documentation.

There are already a lot of tools that support writing and building documentation with Sphinx. This component makes it easy to generate ``.html`` pages that meld seamlessly with `StARLinG's Webpage <https://github.com/starling-lab/starling.utdallas.edu>`_.

.. raw:: html

  <p align="center">
    <img src="https://raw.githubusercontent.com/starling-lab/starling-theme/master/documentation/source/_static/starling_theme_screenshot_0.1.1.png" width="50%" />
  </p>

Installation & Getting Started
------------------------------

1. Clone the repository

.. code-block:: bash

  $ git clone git@github.com:starling-lab/starling-theme.git
  $ python setup.py develop

2. This repository uses itself as a theme. Build the documentation with Sphinx and open it with a browser.

.. code-block:: bash

  $ cd documentation
  $ make html
  $ firefox build/html/index.html

Project State & Current Goals
-----------------------------

This repository is in an *Alpha Phase*. The goal is to create a documentation theme which blends seamlessly with the StARLinG Website, but exactly how this may be achieved is up for debate.

Open Problems are tracked through the `Issues Page <https://github.com/starling-lab/starling-theme/issues/>`_.

License
-------

Copyright © 2018, Alexander L. Hayes

Distributed under the terms of the MIT License. See the LICENSE at the base of the repository for details.
