import zope.interface.verify
from zope.interface import Interface, Attribute, implements


class IMyInterface(Interface):
    """This is an example of an interface."""
    x = Attribute("A required attribute of the interface")

    def __init__(x):
        """Constructor."""

    def equals(x):
        """A required method of the interface."""


class MyImplementation(object):
    implements(IMyInterface)

    def __init__(self, x):
        self.x = x

    def equals(self, x):
        return self.x == x


zope.interface.verify.verifyClass(IMyInterface, MyImplementation)
zope.interface.verify.verifyObject(IMyInterface, MyImplementation(x=1))
