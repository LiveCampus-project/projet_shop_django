from django.shortcuts import render
from .models import Articles, Categories

# Create your views here.
def article_list(request):

    categories = Categories.objects.all()
    categories_id = request.GET.get('categories_id')
    if categories_id:
        articles = Articles.objects.filter(categories_id=categories_id)
    else:
        articles = Articles.objects.all()
        
    is_empty = not articles.exists()
    context = {
            'articles': articles,
            'categories': categories,
            'is_empty': is_empty,  
        }
    return render(request, 'shop/article_list.html', context)

def article_detail(request, article_id):
    return render(request, 'shop/article_detail.html', {'article_id': article_id})
