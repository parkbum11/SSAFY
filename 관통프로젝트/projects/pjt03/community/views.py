from .models import Review
from django.shortcuts import render,redirect


# Create your views here.
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_list.html', context)


def new_review(request):    
    return render(request, 'community/new_review.html')


def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    context={
        'review':review
    }
    return render(request, 'community/review_detail.html',context)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    rank = request.POST.get('rank')
    review = Review()
    review.title = title
    review.content = content
    review.rank = rank
    review.save()
    return redirect('community:review_detail',review.pk)