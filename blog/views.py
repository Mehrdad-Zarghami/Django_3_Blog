from django.shortcuts import render
from .models import PostModel


def post_list_view(request):
    posts_list = PostModel.objects.all()
    context = {'posts_list': posts_list, }
    return render(request, 'blog/posts_list.html', context=context)



