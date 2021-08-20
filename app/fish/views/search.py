from django.contrib import messages

from django.views.generic import TemplateView, ListView

from fish.models import Article, Category, Place, Profile

from django.db.models import Q


class SearchView(ListView):
    model = Article
    template_name = 'search/search.html'
    paginate_by = 24

    def get_queryset(self):
        queryset = Article.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(fish_category__title__icontains=keyword)|Q(place__title__icontains=keyword))
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

search = SearchView.as_view()

#魚種検索ページ
class CategorySearchView(TemplateView):
    template_name = 'search/category_search.html'

category_search = CategorySearchView.as_view()

#魚種検索結果
class CategoryResultView(ListView):
    model = Article
    template_name = 'search/category_result.html'
    paginate_by = 24

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all
        return context

    def get_queryset(self):
        queryset = Article.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(fish_category__title__icontains=keyword))
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

category_result = CategoryResultView.as_view()


#場所検索ページ
class PlaceSearchView(TemplateView):
    template_name = 'search/place_search.html'

place_search = PlaceSearchView.as_view()


#場所検索結果
class PlaceResultView(ListView):
    model = Article
    template_name = 'search/place_result.html'
    paginate_by = 24

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all
        return context

    def get_queryset(self):
        queryset = Article.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(place__title__icontains=keyword))
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

place_result = PlaceResultView.as_view()