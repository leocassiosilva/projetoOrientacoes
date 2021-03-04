from secrets import token_urlsafe

from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from core.models import Area, Tipo
from trabalho.forms import TrabalhoModelForm
from trabalho.models import Trabalho


class TrabalhoCreate(CreateView):
    model = Trabalho
    form_class = TrabalhoModelForm
    template_name = 'trabalho/new-trabalho.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['areas'] = list(Area.objects.all())
        context['tipos'] = list(Tipo.objects.all())
        return context

    def form_valid(self, form):
        trabalho = form.save(commit=False)
        trabalho.id_usuario = self.request.user
        token = token_urlsafe(16)
        trabalho.token = token
        trabalho.save()
        usuario = self.request.user
        data = {'usuario': usuario, 'trabalho': trabalho}
        plain_text = render_to_string('trabalho/emails/email.txt', data)
        html_email = render_to_string('trabalho/emails/email.html', data)
        send_mail("Novo Trabalho",
                  plain_text,
                  "sigoorientacoes@gmail.com",
                  ['{0}'.format(self.request.user)],
                  html_message=html_email
                  )
        return super(TrabalhoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


class TrabalhoListView(ListView):
    model = Trabalho

    def get_queryset(self):
        # trabalhos = Trabalho.objects.all()
        trabalhos = Trabalho.objects.order_by('nome').filter(id_usuario=self.request.user)
        # print(self.request.user)
        return trabalhos


class TrabalhoUpdateView(UpdateView):
    model = Trabalho
    form_class = TrabalhoModelForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('trabalho_listar')


class TrabalhoDeleteView(DeleteView):
    model = Trabalho

    def get_success_url(self):
        return reverse('trabalho_listar')


class TrabalhoDetailView(DetailView):
    model = Trabalho
    fields = ['nome', 'descrição', 'area']
