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

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        update_form = ReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            return redirect("reviews:index")
    else:
        update_form = ReviewForm(instance=review)

    context = {
        "update_form": update_form,
    }
    return render(request, "reviews/update.html", context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')