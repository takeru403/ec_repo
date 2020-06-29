from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class Home(TemplateView):
    template_name = "amazon/home.html"



class ProductListView(ListView):
    model = Product
    template_name = "amazon/list.html"

#queryというのは検索ワードのこと
    def get_queryset(self):
        queryset = Product.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name_contains=qs)
        return queryset
        
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "amazon/detail.html"

# Create your views here.
