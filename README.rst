#️⃣ hash_things
-------

*Hash all sorts of things in Python*

Python has some basic tools for hashing stuff, but not all types are easily supported.

This package contains utility functions that make it easy to hash _things_. Including: `Dicts`.


.. image:: https://img.shields.io/pypi/v/hash_things.svg
        :target: https://pypi.org/project/hash_things/

.. image:: https://img.shields.io/pypi/pyversions/hash_things.svg
        :target: https://pypi.org/project/hash_things/

.. image:: https://img.shields.io/pypi/l/hash_things.svg
        :target: https://pypi.org/project/hash_things/

.. image:: https://img.shields.io/pypi/status/hash_things.svg
        :target: https://pypi.org/project/hash_things/

.. image:: https://circleci.com/gh/phalt/hash_things/tree/master.svg?style=svg
        :target: https://circleci.com/gh/phalt/hash_things/tree/master

Installing the project is easy:

.. code-block:: bash

    pip install hash_things

Full blown example:

.. code-block:: python

  from hash_things import hash_dict

  result = hash_dict({'hello': 'world'})

  result
  >>> 164302408563385743

📖 What can I hash?
--------

- Dictionaries with any value - Lists, Tuples, Sets, and even nested Dicts!

✨ Future goals
---------------

- Objects of any type
- *You favourite type here*

🏗 Status
----------

hash_things is currently stable.

🎥 Credits
-----------

This package was created with Cookiecutter_.

We use `Python Requests`_ for talking HTTP.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
