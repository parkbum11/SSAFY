from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect(request.GET.get('next') or 'community:review_detail', review.pk)
    else: 
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)


def review_list(request):
    community = Review.objects.order_by('-pk')
    context = {
        'community': community,
    }
    return render(request, 'community/review_list.html', context)


def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'community/review_detail.html', context)


@require_POST
def create_comments(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form =CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('community:review_detail', review.pk)
        context = {
            'comment_form' : comment_form,
            'review' : review
        }
        return render(request, 'community/review_detail.html', context)
    return redirect('accounts:login')

@require_POST
def like(request,review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review,pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:review_detail',review_pk)
    return redirect('accounts:login')            