from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
def review_list(request):
    review = Review.objects.order_by('-pk')
    context = {
        'review': review,
    }
    return render(request, 'community/review_list.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_detail', review.pk)
    else: # GET, create new
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)


def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review,
    }
    return render(request, 'community/review_detail.html', context)


def update(request, review_pk):
    reviews = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=reviews)
        if form.is_valid:
            form.save()
            return redirect('community:review_detail', review.pk)
    else: # GET, create new
        form = ReviewForm(instance=reviews)
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)


def delete(request, review_pk):
    reviews = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        reviews.delete()
        return redirect('community:review_list')
