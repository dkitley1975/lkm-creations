# TODO COMMENT OUT THE next two blocks when initially migrating
# to the databases and once the site info is set up
# they should then be uncommented
# the orders sample data will not install without this
# being uncommented


def default_delivery_price():
    try:
        default_delivery_price = (
            SiteInfo.objects.all()
            .filter(is_active=True)
            .order_by("-created_at")[0]
            .delivery_price
            )
        return default_delivery_price
    except:
        return "10"

default_delivery_price = default_delivery_price()


def free_delivery_threshold():
    try:
        free_delivery_threshold = (
            SiteInfo.objects.all()
            .filter(is_active=True)
            .order_by("-created_at")[0]
            .free_delivery_over
            )
        return free_delivery_threshold

    except:
        return "0"

    # free_delivery_threshold = (
    # SiteInfo.objects.all()
    # .filter(is_active=True)
    # .order_by("-created_at")[0]
    # .free_delivery_over
    # )
    # return free_delivery_threshold

free_delivery_threshold = free_delivery_threshold()