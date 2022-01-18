from django.views.generic import ListView

from fish.models import Article, Profile




class IndexView(ListView):
    model = Article
    paginate_by = 6
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.filter(user_id=self.request.user.id)
        return context

    def get_queryset(self):
        queryset = Article.objects.order_by('-created_at')
        return queryset

index = IndexView.as_view()



#みんなの釣果
class EveryFishResultView(ListView):
    model = Article
    template_name = 'fish/every_fish_results.html'
    paginate_by = 24

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.filter(user_id=self.request.user.id)
        return context


    def get_queryset(self):
        queryset = Article.objects.order_by('-created_at')
        return queryset

every_result = EveryFishResultView.as_view()