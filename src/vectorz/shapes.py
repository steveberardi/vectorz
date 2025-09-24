from dataclasses import dataclass, field

from vectorz.tags import Tag

@dataclass(kw_only=True)
class BaseObject():
    classes: str | None = None

    style: dict | None = field(default_factory=dict)

@dataclass
class Circle(BaseObject):
    """Circle shape"""

    x: float
    """Center x-coordinate of the circle"""

    y: float
    """Center y-coordinate of the circle"""

    radius: float
    """Radius of circle"""

    def render(self):
        attributes = dict(cx=self.x, cy=self.y, r=self.radius)
        return Tag("circle", attributes=attributes).render()
