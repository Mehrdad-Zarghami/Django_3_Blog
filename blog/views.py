from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import PostModel
from django.core.exceptions import ObjectDoesNotExist


def post_list_view(request):
    # posts_list = PostModel.objects.all()
    posts_list = PostModel.objects.filter(status='pub')
    context = {'posts_list': posts_list, }
    return render(request, 'blog/posts_list.html', context=context)


def post_detail_view(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    # try:
    #     post = PostModel.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None

    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    return render(request, 'blog/post_create.html')
