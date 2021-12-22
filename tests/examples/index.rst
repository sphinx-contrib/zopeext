The :mod:`example` Module
=========================

Here is a reference to the Interface: :py:interface:`example.IMyInterface`, and to the
implementation: :py:class:`example.MyImplementation`.

.. autosummary::

   example
   example.IMyInterface
   example.MyImplementation


.. automodule:: example
   :members:


Testing
=======
We now check various options.

* The following also contain private members like `_a`:

  .. automodule:: example
     :members:
     :private-members:
     :noindex:

* Here is an explicit example of `autointerface`

  .. autointerface:: example.IMyInterface
     :members:
     :noindex:

  .. autointerface:: example.IMySecondInterface
     :members:
     :noindex:
     :show-inheritance:

* Now the interface with explicit members.

  .. autointerface:: example.IMyInterface
     :members: _a, equals
     :noindex:

     .. automethod:: __init__

* Now the class with explicit members.

  .. autoclass:: example.MyImplementation
     :members:
     :undoc-members:
     :noindex:

     .. automethod:: __init__
