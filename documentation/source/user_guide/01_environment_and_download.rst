=================================
Environment Setup and Downloading
=================================

Getting Python
--------------

Your system requirements may vary, the downloads page on `Python.org <https://www.python.org/downloads/>`_ should have the information needed for your system.

**Linux (yum/dnf)**:

.. code-block:: bash

		sudo yum update
		sudo yum install python

**Linux (apt-get)**:

.. code-block:: bash

		sudo apt-get update
		sudo apt-get install python

For setting up environments, something like `venv <https://docs.python.org/3/library/venv.html>`_ or `Anaconda <https://www.anaconda.com/download/>`_ is recommended (and may save you some trouble at a later date).


Installing ``starling-theme``
-----------------------------

Stable versions of the package are distributed on PyPi, and may be installed using ``pip``.

.. code-block:: bash

		pip install starling-theme

Dependencies
------------

The main dependency for ``starling-theme`` is *Sphinx*, which has its own set of dependencies. All of these should be installed when ``starling-theme`` is installed.
