from dataclasses import dataclass, field

from pyqtree import Index

from vectorz.shapes import BaseObject, Circle
from vectorz.tags import Tag

@dataclass
class Canvas:
    height: int = 600
    """Height of the canvas, in pixels"""

    width: int = 600
    """Width of the canvas, in pixels"""
    
    index: bool = True
    """If True, a spatial index will be created"""

    objects: list[BaseObject] = field(init=False)

    _seq: int = field(init=False, default=0)
    _qtree: Index = field(init=False)

    def __post_init__(self):
        self.objects = []
        if self.index:
            self._qtree = Index(bbox=(0, 0, self.width, self.height))

    def circle(self, x, y, radius, classes=None, style=None):
        c = Circle(x=x, y=y, radius=radius, classes=classes, style=style)

        self.objects.append(c)

        idx = len(self.objects)
        self._seq += 1
        if self.index:
            bbox = (x - radius, y - radius, x + radius, y + radius)
            self._qtree.insert(self._seq, bbox)


    def render(self) -> str:
        children = "\n\t".join([obj.render() for obj in self.objects])
        return Tag(
            "svg",
            children=children,
            attributes={
                "height": self.height,
                "width": self.width,
                "xmlns": "http://www.w3.org/2000/svg",
            },
            self_closing=False,
        ).render()
