from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import Http404 

# Create your views here.

# fortunately the built-in ListView works here even if the data is not on Django models and in mongodb
class ArticleListView(ListView):
    model = Article
    template_name = "ph/article_list.html"
    context_object_name = "articles"
    paginate_by = 20

    #for filtering
    def get_queryset(self):
        query_set = Article.objects.all()[:1000]
        #query_set = query_set.order_by("-scraped_date").allow_disk_use(True)
        #filtering by sentiment
        sentiment_color = self.request.GET.get("sentiment_color")
        if sentiment_color:
            query_set = query_set.filter(sentiment_color = sentiment_color)
        
        #filtering by category
        category = self.request.GET.get("category")
        if category:
            query_set = query_set.filter(category__contains = [category])

        return query_set
    
    #returning some more context variables in the template "ph/article_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sentiment_colors"] = Article.objects.distinct("sentiment_color")
        context["selected_sentiment"] = self.request.GET.get("sentiment_color")

        context["categories"] = ["disease information", "suspected outbreak", "confirmed outbreak", "climate", "others"]
        context["selected_category"] = self.request.GET.get("category", "")

        return context
    
    
# the built-in DetailView doesn't work with mongodb
# so I had to use the View and customise it
class ArticleDetailView(View):
    template_name = "ph/article_detail.html"

    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            return render(request, self.template_name, {"article": article})
        except Article.DoesNotExist:
            raise Http404("Article not found")

   
