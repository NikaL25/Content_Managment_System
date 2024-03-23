from ninja import Router
from modules.models import  Block, Menu
from content.models import Article, Category, Tag
from content.schema import ArticleSchema, CategorySchema, TagSchema,CreateArticleSchema
from modules.schema import BlockSchema, MenuSchema
from user.models import CustomUser
from user.schema import UserSchema
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


router = Router()

# Articles
@router.get("/articles/", tags=["Articles"], response={200: ArticleSchema})
def get_articles(request, category: int = None, tag: int = None, skip: int = 0, limit: int = 10):
    queryset = Article.objects.all()
    if category:
        queryset = queryset.filter(category_id=category)
    if tag:
        queryset = queryset.filter(tags__id=tag)
    articles = queryset[skip:skip+limit]
    return {"articles": [ArticleSchema(article) for article in articles], "total": queryset.count()}



@router.post("/articles/", tags=["Articles"], response={200: ArticleSchema})
def create_article(request, article_data: CreateArticleSchema):
    if request.user.is_authenticated:
        # Extract data from the request body
        title = article_data.title
        description = article_data.description
        publication_datetime = article_data.publication_datetime
        author_id = article_data.author_id
        category_id = article_data.category_id
        tags = article_data.tags
        main_image = article_data.main_image
        publishing = article_data.publishing

        try:
            # Retrieve the Category instance using the provided ID
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Invalid category name"}, status=400)

        try:
            # Retrieve the author using the provided ID
            author = CustomUser.objects.get(id=author_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({"error": "Invalid author ID"}, status=400)

        try:
            # Create the article
            article = Article.objects.create(
                title=title,
                description=description,
                publication_datetime=publication_datetime,
                author=author,
                category=category,
                main_image=main_image,
                publishing=publishing
            )
            # Add tags to the article
            article.tags.add(*tags)
            return JsonResponse({"article": ArticleSchema(article)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "User is not authenticated"}, status=401)

@router.put("/articles/{article_id}/", tags=["Articles"], response={200: ArticleSchema})
def update_article(request, article_id: int, article_data: ArticleSchema):
    article = Article.objects.get(id=article_id)
    for key, value in article_data.dict().items():
        setattr(article, key, value)
    article.save()
    return {"article": ArticleSchema(article)}

@router.delete("/articles/{article_id}/", tags=["Articles"])
def delete_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    article.delete()
    return {"message": "Article deleted successfully."}

# Blocks
@router.get("/blocks/", tags=["Blocks"], response={200: BlockSchema})
def get_blocks(request):
    blocks = Block.objects.all()
    return {"blocks": [BlockSchema(block) for block in blocks]}

@router.post("/blocks/", tags=["Blocks"], response={200: BlockSchema})
def create_block(request, block_data: BlockSchema):
    block = Block.objects.create(**block_data.dict())
    return {"block": BlockSchema(block)}

@router.put("/blocks/{block_id}/", tags=["Blocks"], response={200: BlockSchema})
def update_block(request, block_id: int, block_data: BlockSchema):
    block = Block.objects.get(id=block_id)
    for key, value in block_data.dict().items():
        setattr(block, key, value)
    block.save()
    return {"block": BlockSchema(block)}

@router.delete("/blocks/{block_id}/", tags=["Blocks"])
def delete_block(request, block_id: int):
    block = Block.objects.get(id=block_id)
    block.delete()
    return {"message": "Block deleted successfully."}

# Menus
@router.get("/menus/", tags=["Menus"], response={200: MenuSchema})
def get_menus(request):
    menus = Menu.objects.all()
    return {"menus": [MenuSchema(menu) for menu in menus]}

@router.post("/menus/", tags=["Menus"], response={200: MenuSchema})
def create_menu(request, menu_data: MenuSchema):
    menu = Menu.objects.create(**menu_data.dict())
    return {"menu": MenuSchema(menu)}

@router.put("/menus/{menu_id}/", tags=["Menus"], response={200: MenuSchema})
def update_menu(request, menu_id: int, menu_data: MenuSchema):
    menu = Menu.objects.get(id=menu_id)
    for key, value in menu_data.dict().items():
        setattr(menu, key, value)
    menu.save()
    return {"menu": MenuSchema(menu)}

@router.delete("/menus/{menu_id}/", tags=["Menus"])
def delete_menu(request, menu_id: int):
    menu = Menu.objects.get(id=menu_id)
    menu.delete()
    return {"message": "Menu deleted successfully."}

# Categories
@router.get("/categories/", tags=["Categories"], response={200: CategorySchema})
def get_categories(request):
    categories = Category.objects.all()
    return {"categories": [CategorySchema(category) for category in categories]}

@router.post("/categories/", tags=["Categories"], response={200: CategorySchema})
def create_category(request, category_data: CategorySchema):
    category = Category.objects.create(**category_data.dict())
    return {"category": CategorySchema(category)}

@router.put("/categories/{category_id}/", tags=["Categories"], response={200: CategorySchema})
def update_category(request, category_id: int, category_data: CategorySchema):
    category = Category.objects.get(id=category_id)
    for key, value in category_data.dict().items():
        setattr(category, key, value)
    category.save()
    return {"category": CategorySchema(category)}

@router.delete("/categories/{category_id}/", tags=["Categories"])
def delete_category(request, category_id: int):
    category = Category.objects.get(id=category_id)
    category.delete()
    return {"message": "Category deleted successfully."}

# Tags
@router.get("/tags/", tags=["Tags"], response={200: TagSchema})
def get_tags(request):
    tags = Tag.objects.all()
    return {"tags": [TagSchema(tag) for tag in tags]}

@router.post("/tags/", tags=["Tags"], response={200: TagSchema})
def create_tag(request, tag_data: TagSchema):
    tag = Tag.objects.create(**tag_data.dict())
    return {"tag": TagSchema(tag)}

@router.put("/tags/{tag_id}/", tags=["Tags"], response={200: TagSchema})
def update_tag(request, tag_id: int, tag_data: TagSchema):
    tag = Tag.objects.get(id=tag_id)
    for key, value in tag_data.dict().items():
        setattr(tag, key, value)
    tag.save()
    return {"tag": TagSchema(tag)}

@router.delete("/tags/{tag_id}/", tags=["Tags"])
def delete_tag(request, tag_id: int):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return {"message": "Tag deleted successfully."}

@router.post("/register/", tags=["Register"], response={200: str})
def register(request, username: str, email: str, password: str, profile_picture: str = None, description: str = None):
    # Create user
    user = CustomUser.objects.create_user(username=username, email=email, password=password)
    user.profile_picture = profile_picture
    user.description = description
    user.save()
    
    # Optionally, you can automatically login the user after registration
    login(request, user)
    
    return "Registration successful"

@router.get("/register/", response={200: dict})
def get_registration_form(request):
    registration_form = {
        "fields": [
            {"name": "username", "type": "text", "label": "Username"},
            {"name": "email", "type": "email", "label": "Email"},
            {"name": "password", "type": "password", "label": "Password"}
            # Add more fields as needed
        ]
    }
    return registration_form

@router.post("/login/",tags=["Login"], response={200: str})
def user_login(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "Login successful"
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
@router.get("/login/", response={200: dict})
def get_login_form(request):
    login_form = {
        "fields": [
            {"name": "username", "type": "text", "label": "Username"},
            {"name": "password", "type": "password", "label": "Password"}
            # Add more fields as needed
        ]
    }
    return login_form

@router.post("/logout/",tags=["Logout"] ,response={200: str})
def user_logout(request):
    logout(request)
    return "Logout successful"