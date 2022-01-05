"""Example module using :mod:`zope.interface`.

Here we define an interface :interface:`IMyInterface` and an
implementation :class:`MyImplementation`.
"""

from inspect import Parameter, Signature
from typing import List, Union


import zope.interface.verify
from zope.interface import Interface, Attribute, implementer

__all__ = ["IMyInterface", "IMyInterface2", "MyImplementation"]


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


class IMyInterface2(IMyInterface):
    """A refinement of the previous interface."""

    y = Attribute("A new required attribute")


@implementer(IMyInterface, IMyInterface2)
class MyImplementation:
    """Example that implements :interface:`IMyInterface`

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


IAlias = IMyInterface
Alias = MyImplementation

#: Here is a doccomment for a docstring
IOtherAlias = IMyInterface


zope.interface.verify.verifyClass(IMyInterface, MyImplementation)
zope.interface.verify.verifyClass(IMyInterface2, MyImplementation)
zope.interface.verify.verifyObject(IMyInterface, MyImplementation(x=1))
zope.interface.verify.verifyObject(IMyInterface2, MyImplementation(x=1))

zope.interface.verify.verifyClass(IAlias, Alias)
zope.interface.verify.verifyObject(IAlias, Alias(x=1))


class Foo:
    pass


class Bar:
    def __init__(self, x, y):
        pass


class Baz:
    def __new__(cls, x, y):
        pass


class Qux:
    __signature__ = Signature(
        parameters=[
            Parameter("foo", Parameter.POSITIONAL_OR_KEYWORD),
            Parameter("bar", Parameter.POSITIONAL_OR_KEYWORD),
        ]
    )

    def __init__(self, x, y):
        pass


class Quux(List[Union[int, float]]):
    """A subclass of List[Union[int, float]]"""

    pass


class Corge(Quux):
    pass


#: docstring
OtherAlias = Bar

#: docstring
IntAlias = int
