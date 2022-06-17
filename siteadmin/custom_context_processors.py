from siteadmin.models import SiteInfo


def site_info(request):
    """
    Return the site information object from the database.
    filters the by is_active = True, orders by created_at in descending order.
    and then trims the results to the first one."""

    site_info = (
        SiteInfo.objects.all()
        .filter(is_active=True)
        .order_by("-created_at")[0]
    )
    return {
        "site_info": site_info,
    }
