from rest_framework import viewsets 

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#from rest_framework.generics import ( 
#    ListAPIView,
 #   RetrieveAPIView,
  #  CreateAPIView,
   # DestroyAPIView,
    #UpdateAPIView
#)  


#class Articleview(ListAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer


#class ArticleDetailview(RetrieveAPIView):
#    queryset = Article.objects.all()
#   serializer_class = ArticleSerializer

#class ArticleCreateview(CreateAPIView):
#    queryset = Article.objects.all()
#   serializer_class = ArticleSerializer


#class ArticleUpdateview(UpdateAPIView):
 #   queryset = Article.objects.all()
  #  serializer_class = ArticleSerializer


#class ArticleDeleteview(DestroyAPIView):
 #   queryset = Article.objects.all()
  #  serializer_class = ArticleSerializer  
 