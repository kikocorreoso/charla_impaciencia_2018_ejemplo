========
Tutorial
========

This is a basic tutorial to get started with `mylib`.

Importing the lib
-----------------

You should import the lib like this:

.. code-block:: python

    import mylib as ml

Main functionality
------------------

The main functionality is the function `suma`. It can be used as follows:

.. code-block:: python

    ml.suma(1, 2, 3)

And the result should be:

.. code-block:: python

    6

Testing
-------

To run the tests you have to install `pytest` first. Once `pytest` is installed
you can run the tests from the root directory:

.. code-block:: bash

    $ git clone https://path/to/the_repo
    $ cd the_repo
    $ pytest -v