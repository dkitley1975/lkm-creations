from .models import SiteInfo


def site_info(request):
    """
    The context processor must return a dictionary.
    """
    site_info = SiteInfo.objects.filter(is_active=True).last()
    return {"site_info": site_info}
