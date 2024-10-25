from django.shortcuts import render, get_object_or_404
from .models import Articles, Categories

# Create your views here.
def article_list(request):

    categories = Categories.objects.all()
    selected_category = request.GET.get('categories')
    if selected_category:
        articles = Articles.objects.filter(categories_id=selected_category)
    else:
        articles = Articles.objects.all()
        
    is_empty = not articles.exists()
    context = {
            'articles': articles,
            'categories': categories,
            'selected_category': selected_category,
            'is_empty': is_empty,  
        }
    return render(request, 'shop/article_list.html', context)

def article_detail(request, article_id):

    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'shop/article_detail.html', {'article': article})
