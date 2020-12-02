from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Review
from .forms import ReviewForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_detail', review.pk)
    else: 
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)

def review_list(request):
    community = Review.objects.order_by('-pk')
    num = list(range(len(community)))
    context = {
        'community': community,
        'num':num
    }
    return render(request, 'community/review_list.html', context)


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'community/review_detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'community/form.html', context)


@require_POST
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('community:review_list')