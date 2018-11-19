.. starling_theme documentation master file, created by
   sphinx-quickstart on Fri Nov  2 19:52:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============
starling-theme
==============

``starling-theme``: A Sphinx theme for `StARLinG Lab <https://starling.utdallas.edu>`_ documentation.

A mobile-friendly Sphinx theme based on the design of the StARLinG Lab's website, as well as `sphinx_rtd_theme <https://pypi.org/project/sphinx_rtd_theme/>`_ and the `Minimal Mistakes Jekyll Theme <https://github.com/mmistakes/minimal-mistakes>`_.

.. toctree::
  :hidden:
  :glob:
  :caption: User Guide

  user_guide/index

.. toctree::
  :hidden:
  :glob:
  :caption: Developer Guide

  developer_guide/index
  changelog/index

.. toctree::
  :hidden:
  :caption: Links

  GitHub <https://github.com/batflyer/starling_theme/>
  PyPi <https://pypi.org/project/starling-theme/>

Quick-start
-----------

Stable versions are hosted on `PyPi <https://pypi.org/project/starling-theme/>`_, and may be installed with ``pip``.

.. code-block:: bash

  # Install with pip
  $ pip install starling-theme

  # Check installed version
  $ python
  >>> import starling_theme
  >>> print(starling_theme.__version__)

The ``html_theme`` in your Sphinx ``conf.py`` can then be set to use this theme.

.. code-block:: diff

    # The name of the Pygments (syntax highlighting) style to use.
  + pygments_style = 'monokai'
  - pygments_style = 'sphinx'

    # -- Options for HTML output ----------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the  documentation for
    # a list of builtin themes.
    #
  + html_theme = 'starling_theme'
  - html_theme = 'alabaster'


License
-------

Copyright © 2018, Alexander L. Hayes

Distributed under the terms of the MIT License. See the LICENSE at the base of the repository for details.
