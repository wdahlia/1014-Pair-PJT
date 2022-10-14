from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.


def index(request):
    review_list = Review.objects.order_by("-id")
    context = {"review_list": review_list}
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        create_review = ReviewForm(request.POST)
        if create_review.is_valid():
            create_review.save()
            return redirect("reviews:index")
    else:
        create_review = ReviewForm()

    context = {
        "create_review": create_review,
    }
    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)
