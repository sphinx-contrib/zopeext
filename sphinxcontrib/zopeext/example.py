import zope.interface.verify
from zope.interface import Interface, Attribute, implementer


class IMyInterface(Interface):
    """This is an example of an interface."""
    _a = Attribute("A required attribute of the interface")
    x = Attribute("A required attribute of the interface")

    def __init__(x):
        """The constructor should set the attribute `x`."""

    def equals(x):
        """A required method of the interface.

        .. note::

           The argument `self` is not specified as part of the interface and
           should be omitted, even though it is required in the implementation.
        """


@implementer(IMyInterface)
class MyImplementation(object):
    """Example

    >>> a = MyImplementation(x=2.0)
    >>> a.equals(2.0)
    True
    """
    _a = 1.0

    def __init__(self, x):
        self.x = x

    def equals(self, x):
        return self.x == x


zope.interface.verify.verifyClass(IMyInterface, MyImplementation)
zope.interface.verify.verifyObject(IMyInterface, MyImplementation(x=1))
