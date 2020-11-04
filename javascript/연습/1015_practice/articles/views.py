from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# 이거 추가! -> json으로 요청을 보냄!
from django.http import JsonResponse

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@require_POST
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


@require_POST
def like(request, article_pk):    
    #  context가 if문을 안들어갔을 경우 아무것도 안담겨 있으니 error를 담아서 넘겨줌
    context = {
        'error':'unauthorized'
    }
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        if article.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
        # 이 유저가 현재 좋아하는지 안좋아하는지
            liked = True
        # 위의 context가 이거로 바뀜
        context = {
            'liked':liked,
            # 이 유저를 좋아하는 수를 count한걸 값으로 보내줌!
            'count':article.like_users.count(),
        }
        # return redirect('articles:index')
        # data를 json으로 요청보냄
    return JsonResponse(context)
    # 브라우저 요청을 했을 때 redirect가 되는거지 JavaScript에서는 아무소용없기 때문에 필요없는 코드
    # return redirect('accounts:login')