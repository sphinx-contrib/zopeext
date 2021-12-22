The :mod:`example` Module
=========================

.. autosummary::

   sphinxcontrib.zopeext.example
   sphinxcontrib.zopeext.example.IMyInterface
   sphinxcontrib.zopeext.example.MyImplementation


.. automodule:: sphinxcontrib.zopeext.example
   :members:


Testing
=======
We now check various options.

* The following also contain private members like `_a`:

  .. automodule:: sphinxcontrib.zopeext.example
     :members:
     :private-members:
     :noindex:

* Here is an explicit example of `autointerface`

  .. autointerface:: sphinxcontrib.zopeext.example.IMyInterface
     :members:
     :noindex:

  .. autointerface:: sphinxcontrib.zopeext.example.IMySecondInterface
     :members:
     :noindex:
     :show-inheritance:

* Now with explicit members.

  .. autointerface:: sphinxcontrib.zopeext.example.IMyInterface
     :members: _a, equals
     :noindex:

     .. automethod:: __init__

* Now with explicit members.

  .. autoclass:: sphinxcontrib.zopeext.example.MyImplementation
     :members:
     :undoc-members:
     :noindex:

     .. automethod:: __init__
