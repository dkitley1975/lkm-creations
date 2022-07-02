from django.shortcuts import render


def bad_request_error_400(request, exception):
    return render(request, "error/400.html", status=400)


def forbidden_error_403(request, exception):
    return render(request, "error/403.html", status=403)


def page_not_found_view_404(request, exception):
    return render(request, "error/404.html", status=404)


def internal_error_500(request):
    return render(request, "error/500.html", {})
