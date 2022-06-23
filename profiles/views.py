from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from checkout.models import OrderDetails

from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
@login_required
def dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You profile has been updated successfully"
            )
        else:
            messages.error(
                request,
                ("Update failed. Please ensure the form is valid."),
            )
    else:
        form = UserProfileForm(instance=profile)

    order_history = profile.orders.all()
    context = {"form": form, "order_history": order_history}
    return render(request, "profiles/pages/dashboard.html", context)


@login_required
def order_summary(request, order_number):
    order = get_object_or_404(OrderDetails, order_number=order_number)

    context = {
        "order": order,
        "from_dashboard": True,
    }
    return render(request, "profiles/pages/order-summary.html", context)
