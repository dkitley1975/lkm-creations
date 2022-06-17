from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

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
            messages.success(request, "Profile updated successfully")

        else:
            messages.error(
                request,
                ("Update failed. Please ensure " "the form is valid."),
            )
    else:
        form = UserProfileForm(instance=profile)

    # orders = profile.orders.all()
    context = {
        "form": form,
        # 'orders': orders,
    }
    return render(request, "profiles/pages/dashboard.html", context)
