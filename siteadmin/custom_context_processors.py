from siteadmin.models import SiteInfo


def site_info(request):
    """
    Return the site information for the site.
    """
    site_info = (
        SiteInfo.objects.all()
        .filter(is_active=True)
        .order_by("-created_at")[0:1]
    )
    context = {
        "site_info": site_info,
    }
    return context
