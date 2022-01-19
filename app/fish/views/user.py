from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import UpdateView, DetailView
from django.urls import reverse
from fish.models import Article, Profile
from fish.forms import ProfileForm


# ユーザーページ
class UserPageDetailView(DetailView):
    template_name = 'profile/mypage.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Article_list'] = Article.objects.filter(user=self.object.user).order_by('-created_at')[:15]
        return context

mypage_detail = UserPageDetailView.as_view()



# ユーザーページング
class UserPadingDetailView(DetailView):
    template_name = 'profile/mypading.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Article_list'] = Article.objects.filter(user=self.object.user).order_by('-created_at')[:15]
        return context

mypage_pading = UserPadingDetailView.as_view()


# プロフィール編集
class UserPageUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'profile/profile_edit.html'
    form_class = ProfileForm
    model = Profile

    def get_success_url(self):
        return reverse('fish:mypage_detail', kwargs={'pk': self.object.pk})

profile_edit = UserPageUpdateView.as_view()