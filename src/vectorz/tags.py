class Tag:
    def __init__(
        self,
        name,
        children: list = None,
        attributes: dict = None,
        self_closing=True,
        *args,
        **kwargs,
    ):
        self.name = name
        self.children = children or ""
        self.attributes = attributes or {}
        self.self_closing = self_closing

    def render(self):
        attributes = " ".join(
            [f'{key}="{value}"' for key, value in self.attributes.items()]
        )

        if self.self_closing:
            return f"<{self.name} {attributes.strip()} />"

        return (
            f"<{self.name} {attributes.strip()}>" + self.children + f"\n</{self.name}>"
        )
