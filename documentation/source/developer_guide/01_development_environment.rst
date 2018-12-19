=================================
Environment Setup and Downloading
=================================

.. toctree::
  :glob:
  :maxdepth: 1

This package is built as a `Sphinx theme <https://www.sphinx-doc.org/en/master/theming.html>`_ with the aim to automatically create HTML documentation for Python packages.

This Developer Guide will hopefully provide some insight for developing this further.

Development Environment
-----------------------

If you've ran/modified/ran your code multiple times without being able to figure out why the output was not changing, you may have experienced poor segmentation of development environments and production environments.

Before developing this theme further, it's strongly suggested to ensure that there is not a production version installed by either:

Uninstalling an existing version:

.. code-block:: bash

  pip uninstall starling-theme

Or, creating an environment for developing this theme (here using `Anaconda <https://www.anaconda.com/download/>`_):

.. code-block:: bash

  conda create -n starling_theme python=3.6 sphinx
  source activate starling_theme


Cloning from GitHub and Installing the Theme
--------------------------------------------

The repository may be forked from the main repository and cloned, or may be cloned and pushed to a different repository later. New versions of the code work off of the development branch prior to being merged into the master branch.

Clone the repository and check out the development branch:

.. code-block:: bash

  git clone git@github.com:starling-lab/starling-theme.git
  git checkout development

Change directory to the base of the repository and run ``setup.py`` to add the development theme.

.. code-block:: bash

  cd starling-theme
  python setup.py develop
