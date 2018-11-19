==================
Sphinx Quick-start
==================

.. toctree::
  :glob:
  :maxdepth: 1

Check Installation
------------------

This is a short way to check that both Sphinx and starling-theme were installed:

.. code-block:: python

   >>> import sphinx
   >>> print(sphinx.__version__)
   >>> import starling_theme
   >>> print(starling_theme.__version__)

Sphinx-Quickstart
-----------------

During ``sphinx`` installation, a ``sphinx-quickstart`` script should be installed in whatever bin directory your Python installation defaults to.

From the base of your project repository, create a ``documentation`` directory:

.. code-block:: bash

  mkdir documentation
  cd documentation

Within the new documentation directory, run ``sphinx-quickstart``.

The script prompts the user a series of questions, then creates the configuration file (``conf.py``) and respective directories based on the answers.

.. code-block:: bash

  $ sphinx-quickstart
  Welcome to the Sphinx 1.6.3 quickstart utility.

The questions and [default values] for ``1.6.3`` are listed below, but two deviations from the default values are recommended:

* Answer yes (``y``) when asked if you would like to **separate source and build directories**. This comes personal preference, but choosing to keep them separate makes for a more clear distinction between code which *generates* documentation, and the documentation itself.
* Answer yes (``y``) to the ``autodoc`` question. This is the setting which creates the documentation for your Python classes and functions by reading the signatures and module docstrings.

.. code-block:: text

  > Root path for the documentation [.]:
  > Separate source and build directories (y/n) [n]:
  > Name prefix for templates and static dir [_]:
  > Project name:
  > Author name(s):
  > Project version []:
  > Project release []:
  > Project language [en]:
  > Source file suffix [.rst]:
  > Name of your master document (without suffix) [index]:
  > Do you want to use the epub builder (y/n) [n]:
  > autodoc: automatically insert docstrings from modules (y/n) [n]:
  > doctest: automatically test code snippets in doctest blocks (y/n) [n]:
  > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
  > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
  > coverage: checks for documentation coverage (y/n) [n]:
  > imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
  > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
  > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
  > viewcode: include links to the source code of documented Python objects (y/n) [n]:
  > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:
  > Create Makefile? (y/n) [y]:
  > Create Windows command file? (y/n) [y]:

After answering the questions, your documentation directory will contain two directories: ``build/`` and ``source/``, as well as a ``Makefile`` and ``make.bat`` script.

The ``source/`` directory will also contain a ``conf.py`` file (configuration options for Sphinx), ``index.rst`` (basically your home page), and two empty directories: ``_static`` and ``_templates``.

Modifying ``conf.py`` to use ``starling-theme``
-----------------------------------------------

Open ``conf.py`` using your favorite text editor. Then modify the ``html_theme`` variable to use ``starling_theme`` (notice the underscore **_** instead of the hyphen) rather than the default alabaster theme.

.. code-block:: diff

    # -- Options for HTML output ----------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    #
  - html_theme = 'alabaster'
  + html_theme = "starling_theme"

The default Pygments syntax highlighting style can clash with the output, so changing it to something like ``monokai`` is recommended as well.

.. code-block:: diff

      # The name of the Pygments (syntax highlighting) style to use.
    - pygments_style = 'sphinx'
    + pygments_style = "monokai"

Now you're all set! Running ``make`` will produce documentation using the theme:

.. code-block:: bash

  make html
