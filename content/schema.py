from ninja import Schema

class ArticleSchema(Schema):
    id: int
    title: str
    description: str
    publication_datetime: str
    author: str
    category: str
    tags: list
    main_image: str
    publishing: bool

class CreateArticleSchema(Schema):
    title: str
    description: str
    publication_datetime: str
    author_id: int
    category_id: int
    tags: list
    main_image: str
    publishing: bool

class CategorySchema(Schema):
    id: int
    name: str
    logo: str
    parent_id: int

class TagSchema(Schema):
    id: int
    name: str