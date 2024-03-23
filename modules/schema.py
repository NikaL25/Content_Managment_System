from ninja import Schema

class BlockSchema(Schema):
    id: int
    article_id: int
    visual_selection: str
    position: str
    row: int
    title: str
    display_title: bool

class MenuSchema(Schema):
    id: int
    name: str
    link: str
    is_external: bool
    category_id: int
    is_active: bool