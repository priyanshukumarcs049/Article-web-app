from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls

#from django.urls import path

# from .views import (
#    Articleview,
#    ArticleDetailview,
#    ArticleCreateview,
#    ArticleUpdateview,
#    ArticleDeleteview
# )


# urlpatterns = [
#    path('', Articleview.as_view()),
#    path('create/', ArticleCreateview.as_view()),
#    path('<pk>', ArticleDetailview.as_view()),
#    path('<pk>/update', ArticleUpdateview.as_view()),
#    path('<pk>/delete', ArticleDeleteview.as_view())

# ]
