"""Example module using :external+zope.interface:doc:`README`

Here we define an interface :interface:`IMyInterface` and an
implementation :class:`MyImplementation`.
"""
import zope.interface.verify
from zope.interface import Interface, Attribute, implementer

__all__ = ["IMyInterface", "IMySecondInterface", "MyImplementation"]


class IMyInterface(Interface):
    """This is an example of an interface."""

    _a = Attribute("A private required attribute of the interface")
    x = Attribute("A required attribute of the interface")

    def __init__(x):
        """The constructor should set the attribute `x`.

        Parameters
        ----------
        x : float
            The parameter `x`.
        """

    def equals(x):
        """A required method of the interface.

        Parameters
        ----------
        x : float
            The parameter `x`.

        Notes
        -----

        The argument `self` is not specified as part of the interface and
        should be omitted, even though it is required in the implementation.
        """


class IMySecondInterface(IMyInterface):
    """A refinement of the previous interface."""

    y = Attribute("A new required attribute")


@implementer(IMyInterface, IMySecondInterface)
class MyImplementation:
    """Example

    >>> a = MyImplementation(x=2.0)
    >>> a.equals(2.0)
    True
    """

    _a = 1.0
    x = None
    y = None

    def __init__(self, x, y=3.0):
        """Constructor.

        Parameters
        ----------
        x : float
            The parameter `x`.
        y : float, optional
            An additional  parameter `y` that is not part of the interface, but which
            has a default value (3.0) and so does not violate the interface definition.
        """
        self.x = x
        self.y = y

    def equals(self, x):
        """A required method of the interface.

        Parameters
        ----------
        x : float
            The parameter `x`.
        """
        return self.x == x


zope.interface.verify.verifyClass(IMyInterface, MyImplementation)
zope.interface.verify.verifyClass(IMySecondInterface, MyImplementation)
zope.interface.verify.verifyObject(IMyInterface, MyImplementation(x=1))
zope.interface.verify.verifyObject(IMySecondInterface, MyImplementation(x=1))
