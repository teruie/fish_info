from django.shortcuts import redirect, get_object_or_404


from django.views.generic import CreateView

from fish.models import Article, Comment

from fish.forms import CommentCreateForm


# コメント
class CommentCreate(CreateView):
    template_name = 'fish/comment_form.html'
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        article_pk = self.kwargs['pk']
        article = get_object_or_404(Article, pk=article_pk)
        comment = form.save(commit=False)
        comment.target = article
        comment.save()
        return redirect('fish:article_detail', pk=article_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs['pk'])
        return context

comment_create = CommentCreate.as_view()