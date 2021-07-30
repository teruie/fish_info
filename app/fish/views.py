from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages

from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, DeleteView, ListView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy, reverse

from .models import Article, Category, Place, Profile

from .forms import ArticleForm, ProfileForm, ContactForm

from django.db.models import Q






class IndexView(ListView):
    model = Article
    paginate_by = 6
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all
        return context

    def get_queryset(self):
        queryset = Article.objects.order_by('id')
        return queryset


#投稿作成
class ArticleCreateView(CreateView, LoginRequiredMixin):
    template_name = 'fish/article_new.html'
    success_url = reverse_lazy('fish:index')
    form_class = ArticleForm
    model = Article


    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('fish:index')


#投稿画面詳細
class ArticlDetailview(DetailView):
    template_name = 'fish/article_detail.html'
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article_list'] = Article.objects.filter(user=self.object.user).order_by('?')[:3]
        context['profile_list'] = Profile.objects.filter(user=self.object.user)
        return context


#投稿消去
class ArticleDeleteview(DeleteView, LoginRequiredMixin):
    model = Article
    success_url = reverse_lazy('fish:index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)


#投稿変更
class ArticleUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'fish/article_edit.html'
    form_class = ArticleForm
    model = Article

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(('fish:index'))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('fish:article_detail', kwargs={'pk': self.object.pk})


#検索
class SearchView(ListView):
    model = Article
    template_name = 'fish/search.html'
    paginate_by = 24

    def get_queryset(self):
        queryset = Article.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(fish_category__title__icontains=keyword)|Q(place__title__icontains=keyword))
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset


#魚種検索ページ
class CategorySearchView(TemplateView):
    template_name = 'fish/category_search.html'


#魚種検索結果
class CategoryResultView(ListView):
    model = Article
    template_name = 'fish/category_result.html'
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


#場所検索ページ
class PlaceSearchView(TemplateView):
    template_name = 'fish/place_search.html'


#場所検索結果
class PlaceResultView(ListView):
    model = Article
    template_name = 'fish/place_result.html'
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


#Userpage表示
class UserPageDetailView(DetailView):
    template_name = 'profile/mypage.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Article_list'] = Article.objects.filter(user=self.object.user).order_by('-created_at')[:15]
        return context

#Mypageのページング
class UserPadingDetailView(DetailView):
    template_name = 'profile/mypading.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Article_list'] = Article.objects.filter(user=self.object.user).order_by('-created_at')[:15]
        return context


#プロフィール編集画面
class UserPageUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'profile/profile_edit.html'
    form_class = ProfileForm
    model = Profile

    def get_success_url(self):
        return reverse('fish:mypage_detail', kwargs={'pk': self.object.pk})


class EveryFishResultView(ListView):
    model = Article
    template_name = 'fish/every_fishresults.html'
    paginate_by = 24

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all
        return context


    def get_queryset(self):
        queryset = Article.objects.order_by('-id')
        return queryset


#お問い合わせフォーム
class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('fish:contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
        

class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context