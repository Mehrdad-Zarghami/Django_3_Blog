from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import PostModel
from django.contrib.auth.models import User
from .forms import NewPostForm
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
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            # form = NewPostForm()  # To show an empty form after submitting a form
            return redirect('posts_list_page')  # Automatically uses reverse function
    else:
        form = NewPostForm()
    return render(request, 'blog/post_create.html', context={'new_post_form': form})

    # if request.method == "POST":
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #
    #     user = User.objects.all()[0]
    #     PostModel.objects.create(title=post_title, text=post_text, author=user, status='pub')
    #
    # return render(request, 'blog/post_create.html')


def post_update_view(request, pk):
    # post = PostModel.objects.get(pk=pk)
    post = get_object_or_404(PostModel, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)  # instance --> initial values of the model-form
    # if request.POST does not exist, the first input is None --> form = NewPostForm(instance=post)

    if form.is_valid():  # only gets into this if-statement if we press the submit button--> request.method == "POST"
        form.save()
        return redirect('post_list_page')

    return render(request, 'blog/post_create.html', context={'new_post_form': form})
