from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from checkout.models import OrderDetails

from .forms import UpdateUserForm, UserProfileForm
from .models import UserProfile


# Create your views here.
@login_required
def DashboardView(request):
    """
    Render the Dashboard view page.
    """
    return render(request, "profiles/pages/dashboard.html")


@login_required
def OrderHistoryView(request):
    """
    Return the order history for the user.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    order_history = profile.orders.all().order_by("-order_date")
    context = {"order_history": order_history}
    return render(request, "profiles/pages/order-history.html", context)


@login_required
def ConnectionsView(request):
    """
    Render the Social Connections view page..
    """
    return render(request, "profiles/pages/connections.html")


@login_required
def order_summary(request, order_number):
    """
    Given an order number, return the order details.
    """
    order = get_object_or_404(OrderDetails, order_number=order_number)
    context = {
        "order": order,
        "from_dashboard": True,
    }
    return render(request, "profiles/pages/order-summary.html", context)


@login_required
def profileUpdate(request):
    """
    Update the user profile. This is a POST request.
    The user_form is the form that is used to update
    the user's information.
    The profile_form is a form that is used to update
    the user's profile.
    The context is the dictionary that contains the user_form
    and profile_form.
    """
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(
                request, "Your profile is updated successfully"
            )
            return redirect(to="profile-update")
    else:
        user_form = UpdateUserForm(instance=request.user)

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

    context = {"form": form, "user_form": user_form}
    return render(request, "profiles/pages/profile-update.html", context)


@login_required
def deleteAccountView(request):
    """
    Delete an account page.
    """
    return render(request, "profiles/pages/profile-delete.html")


@login_required
@require_http_methods(["POST"])
def remove_account(request):
    """
    Logout the user and delete their account.
    redirect to the homepage.
    """
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).delete()
    messages.info(request, "Your account has been deleted.")
    success_url = "/"
    return redirect(success_url)
