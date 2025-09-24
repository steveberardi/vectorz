import random
import time

from vectorz import Canvas
from vectorz.shapes import Circle

# from starplot import Star, DSO, _

start = time.time()

height = 180 * 5
width = 360 * 5

c = Canvas(height=height, width=width, index=True)

shapes = []

# dsos = DSO.find(where=[_.ngc.notnull()])
# stars = Star.find(where=[_.magnitude < 6])
# print(len(stars))
# for n in stars:
#     c.circle(
#         cx=(360 - n.ra) * 5,
#         cy=(90 - n.dec) * 5,
#         r=(7 - n.magnitude) / 3,
#     )

for n in range(10_000):
    c.circle(
        x=random.randint(10, width),
        y=random.randint(10, height),
        radius=random.randint(1, 5)/2,
    )


with open("scratchpad.svg", "w") as outfile:
    outfile.write(c.render())

duration = time.time() - start
ms = int(duration * 1000)
print(f"{ms}ms")