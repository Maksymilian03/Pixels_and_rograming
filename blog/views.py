from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .forms import ArticleForm
# Create your views here.


def article_create_form(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = ArticleForm()

    context = {
        'form': form
    }

    return render(request, 'form.html', context)


class Main_page(ListView):
    template_name = 'main_page.html'
    model = Article


# class ArticleCreateView(PermissionRequiredMixin, CreateView):
#     template_name = 'form.html'
#     form_class = ArticleForm
#     success_url = reverse_lazy('index')
#     permission_required = 'blog.create_article'
