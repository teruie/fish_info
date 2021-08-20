from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from django.urls import reverse_lazy, reverse

from fish.models import Article, Profile, Comment

from fish.forms import ArticleForm, CommentCreateForm




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

article_create = ArticleCreateView.as_view()



#投稿画面詳細
class ArticlDetailview(DetailView):
    template_name = 'fish/article_detail.html'
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article_list'] = Article.objects.filter(user=self.object.user).order_by('?')[:3]
        context['profile_list'] = Profile.objects.filter(user=self.object.user)
        context['comment'] = Comment.objects.filter(target=self.object.pk)
        return context

article_detail = ArticlDetailview.as_view()


#投稿消去
class ArticleDeleteview(DeleteView, LoginRequiredMixin):
    model = Article
    success_url = reverse_lazy('fish:index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

article_delete = ArticleDeleteview.as_view()


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

article_edit = ArticleUpdateView.as_view()