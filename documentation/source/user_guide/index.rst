==========
User Guide
==========

This guide is meant to provide a reasonable introduction into building documentation with stable versions of this theme.

* If you are looking for information on how to develop this theme further, see the :doc:`/developer_guide/index`.
* If you are looking for a more general tutorial on Sphinx, the `Official Sphinx Quickstart <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ guide may be helpful.

Sections
--------

.. toctree::
  :glob:
  :maxdepth: 1

  ./*

TL;DR (*Too Long Didn't Read*)
------------------------------

.. code-block:: bash

  # Install sphinx and the theme
  pip install sphinx starling-theme

  # Run sphinx-quickstart and follow the prompts
  mkdir docs; cd docs
  sphinx-quickstart

  # Overwrite the html_theme in conf.py and run `make`
  make html
