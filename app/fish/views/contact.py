from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from fish.forms import ContactForm


# お問い合わせ
class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('fish:contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

contact_form = ContactFormView.as_view()


# 問い合わせ完了
class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context

contact_result = ContactResultView.as_view()