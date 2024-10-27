from django.shortcuts import render, get_object_or_404
from .models import Articles, Categories

def article_list(request):

    categories = Categories.objects.all()
    categorie_id = request.GET.get('categorie_id')
    if categorie_id:
        articles = Articles.objects.filter(categorie_id=categorie_id)
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

    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'shop/article_detail.html', {'article': article})
