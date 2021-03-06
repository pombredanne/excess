from .compat import etree
from .element import Element


class Sequence(object):
    """Python representation of an xs:sequence.

    An instance of this class should be used as the "content" attribute of
    a ComplexType class.
    """

    def __init__(self, *args):
        """Create a new Sequence.

        Each entry in *args should be an xs.Element, but this may later extend
        to allow xs.Choice or other valid constructs.

        Eventually, various kwargs will also be added
        """
        self.components = []
        self.component_dict = {}

        for arg in args:
            if not isinstance(arg, Element):
                raise TypeError("Each item in a sequence must be an Element")
            self.components.append(arg)
            self.component_dict[arg.name] = arg
