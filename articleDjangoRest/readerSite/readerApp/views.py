import json
import urllib
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Article
from .models import Recommendation
from django.template import RequestContext, loader


def landingPage(request):
    
    #get all articles
    article_list = list(Article.objects.order_by('pub_date'))
    
    #serializing and returning HttpResponse
    
    articlesJson = serializers.serialize('json',article_list)
    return HttpResponse(articlesJson,content_type = "application/json")

def articlePage(request, article_id):
    
    print('articlePage called')
    
    #getting article details
    
    article = Article.objects.get(pk=article_id)
    title = article.title
    author = article.author
    pub_date = article.pub_date
    category = article.category
    text = article.text
    imageMain=article.imageMain
    
    #getting recommendations
    
    recommendations = Recommendation.objects.filter(ref_article=article_id).order_by('timestamp')[:4]
    recommendations_ids=[one_recommendation.recommendation_id for one_recommendation in recommendations]
    recommendedArticles = Article.objects.filter(pk__in=recommendations_ids)
    
    #converting QuerySet type to list for appending later and serialilzing
    
    recommendedArticles=list(recommendedArticles)
    
    # appending article and recommendations
    
    article=[article]+recommendedArticles
    
    #serializing returning HttpResponse
    
    articleJson=serializers.serialize('json',article)
    return HttpResponse(articleJson,content_type="application/json")

def searchResults(request):
    
    #getting the urldecoded string
    search_terms = urllib.unquote(request.GET['terms']).decode('utf8')
    
    #spliting by space
    search_terms = search_terms.split(' ')
    
    #getting all objects on which Q will be applied
    articles = Article.objects.all()
    
    #some validations on search terms
    if len(search_terms)>0:
        q = Q(title__icontains=search_terms[0])
        if len(search_terms)>1:
            for search_term in search_terms[1:]:
                
                #preparing Q
                
                q.add((Q(title__icontains=search_term)), q.connector)
        
        #applying Q object
        articles = articles.filter(q)
        articles = list(articles)
        search_results = serializers.serialize('json',articles)
    else:
        search_results= ""
    return HttpResponse(search_results,content_type = "application/json")
