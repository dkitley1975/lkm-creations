[![David's GitHub Banner](/readme/assets/logo/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations - Site Testing<!-- omit in toc -->

[![LKM Creations](/readme/assets/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This document contains a breakdown of the testing preformed on the LKM-Creations website.

# Table Of Contents

- [Table Of Contents](#table-of-contents)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JS](#js)
  - [PYTHON](#python)
- [Automated Testing](#automated-testing)

# Code Validation

## HTML

To validate the html code, each page was opened in a browser and the view page source command was used.
This code was copied and pasted in to [W3C Markup Validation Service](https://validator.w3.org/nu/#textarea "link") This issued a warning that the html code was not valid. The warning was fixed by performing any alterations required and the page code was tested again.
Code such as the toast messages were tested by creating a test page and with a template view. The base page template was used as the base and then the toast message html pasted in. The test page was viewed in the browser and then tested.

The error pages were tested by mistyping in a page address to view the 404 page and the page source page tested,
The 500 error page was tested by corrupting the 404 error page and then mistyping in a page address which forced the 500 error page to be displayed. Then testing the page source code.
The 403 error page was tested by removing the csrf_token from a form and filling in the information, and then testing the page source page.
The 400 error page was tested by replacing the 403.html with the 400.html, create a 403 error, ensured the error was in the 400.html code as expected and then testing the page source page.
Below is a list of the pages tested, the result from [validator.w3.org](https://validator.w3.org/nu/#textarea "link") and a link to a screenshot of the results page.

| File Name | File Path | Result | W3C | Comments |
|--|--|--|--|--|
| index.html | templates/home/index.html | PASS | [link](/readme/assets/validation/html/homepage.png "link") ||
| contact-us.html | templates/home/contact-us.html | PASS | [link](/readme/assets/validation/html/contact-us.png "link") ||
| cookie-policy.html | templates/home/cookie-policy.html | PASS | [link](/readme/assets/validation/html/cookie-policy.png "link") ||
| disclaimer-policy.html | templates/home/disclaimer-policy.html | PASS | [link](/readme/assets/validation/html/disclaimer-policy.png "link") ||
| privacy-policy.html | templates/home/privacy-policy.html | PASS | [link](/readme/assets/validation/html/privacy-policy.png "link") ||
| returns-policy.html | templates/home/returns-policy.html | PASS | [link](/readme/assets/validation/html/returns-policy.png "link") ||
| shipping-policy.html | templates/home/shipping-policy.html | PASS | [link](/readme/assets/validation/html/shipping-policy.png "link") ||
| terms-of-service-policy.html | templates/home/terms-of-service-policy.html | PASS | [link](/readme/assets/validation/html/terms-of-service-policy.png "link") ||
| product-creation.html | templates/product/product-creation.html | PASS | [link](/readme/assets/validation/html/product-creation.png "link") ||
| product-update.html | templates/product/product-update.html | PASS | [link](/readme/assets/validation/html/product-update.png "link") ||
| index.html | templates/store/products.html | PASS | [link](/readme/assets/validation/html/products.png "link") ||
| index.html | templates/store/category.html | PASS | [link](/readme/assets/validation/html/category.png "link") ||
| index.html | templates/store/sale-products.html | PASS | [link](/readme/assets/validation/html/sale-products.png "link") ||
| product-detail.html | templates/store/product-detail.html | PASS | [link](/readme/assets/validation/html/product-detail.png "link") ||
| summary.html | templates/basket/summary.html | PASS | [link](/readme/assets/validation/html/summary.png "link") ||
| checkout-success.html | templates/checkout/checkout-success.html | PASS | [link](/readme/assets/validation/html/checkout-success.png "link") ||
| checkout.html | templates/checkout/checkout.html | PASS | [link](/readme/assets/validation/html/checkout.png "link") ||
| 400.html | templates/error/400.html | PASS | [link](/readme/assets/validation/html/400.png "link") ||
| 403.html | templates/error/403.html | PASS | [link](/readme/assets/validation/html/403.png "link") ||
| 404.html | templates/error/404.html | PASS | [link](/readme/assets/validation/html/404.png "link") ||
| 500.html | templates/error/500.html | PASS | [link](/readme/assets/validation/html/500.png "link") ||
| login.html | templates/allauth/account/login.html | PASS | [link](/readme/assets/validation/html/login.png "link") ||
| signup.html | templates/allauth/account/signup.html | PASS | [link](/readme/assets/validation/html/signup.png "link") ||
| toast_error.html | templates/toasts/toast_error.html | PASS | [link](/readme/assets/validation/html/toast_error.png "link") ||
| toast_info.html | templates/toasts/toast_info.html | PASS | [link](/readme/assets/validation/html/toast_info.png "link") ||
| toast_success.html | templates/toasts/toast_success.html | PASS | [link](/readme/assets/validation/html/toast_success.png "link") ||
| toast_warning.html | templates/toasts/toast_warning.html | PASS | [link](/readme/assets/validation/html/toast_warning.png "link") ||

[Table of Contents  ⇧](#table-of-contents)
***

## CSS

To Validate the css code, each of the css files were copied and pasted in to [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input+with_options "link"), with this service having issues with CSS Variables giving the warning *(Due to their dynamic nature, CSS variables are currently not statically checked)* and as I use these for my colours I also passed the code through [validator.w3.org (css box ticked)](https://validator.w3.org/nu/#textarea "link"),

| File Name | File Path | Result validator.w3.org | Result W3C | comments |
|--|--|--|--|--|
| admin.css | static/css/admin.css | PASS [link](/readme/assets/validation/css/admin.png "link") | PASS [link](/readme/assets/validation/css/admin-w3c.png "link") | W3C warnings regarding CSS variables & vendor extended pseudo-element [link](/readme/assets/validation/css/admin-w3c-warnings.png "link") |
| allauth.css | static/css/allauth.css | PASS [link](/readme/assets/validation/css/allauth.png "link") | PASS [link](/readme/assets/validation/css/allauth-w3c.png "link") |  |
| brand-colours.css | static/css/brand-colours.css | PASS [link](/readme/assets/validation/css/brand-colours.png "link") | PASS [link](/readme/assets/validation/css/brand-colours-w3c.png "link") |  |
| profile.css | static/css/profile.css | PASS [link](/readme/assets/validation/css/profile.png "link") | PASS [link](/readme/assets/validation/css/profile-w3c.png "link") |  |
| social_share.css | static/css/social_share.css | PASS [link](/readme/assets/validation/css/social_share.png "link") | PASS [link](/readme/assets/validation/css/social_share-w3c.png "link") | W3C warnings regarding CSS variables [link](/readme/assets/validation/css/social_share-w3c-warnings.png "link") |
| spinner.css | static/css/spinner.css | PASS [link](/readme/assets/validation/css/spinner.png "link") | PASS [link](/readme/assets/validation/css/spinner-w3c.png "link") | W3C warnings regarding CSS variables [link](/readme/assets/validation/css/spinner=w3c=warnings.png "link") |
| stripe.css | static/css/stripe.css | PASS [link](/readme/assets/validation/css/stripe.png "link") | PASS [link](/readme/assets/validation/css/stripe-w3c.png "link") | W3C warnings regarding CSS variables [link](/readme/assets/validation/css/stripe-w3c-warnings.png "link") |
| styles.css | static/css/styles.css | PASS [link](/readme/assets/validation/css/styles.png "link") | PASS [link](/readme/assets/validation/css/styles-w3c.png "link") | W3C warnings regarding CSS variables & vendor extended pseudo-element [link](/readme/assets/validation/css/styles-w3c-warnings.png "link") |

[Table of Contents  ⇧](#table-of-contents)
***

## JS

| File Name | File Path | Result | JSHint | Comments |
|--|--|--|--|--|
| countryfield.js | static/css/countryfield.js | PASS | [link](/readme/assets/validation/js/countryfield.png "link") | One undefined variable |
| facebook.js | static/css/facebook.js | PASS | [link](/readme/assets/validation/js/facebook.png "link") | One undefined variable |
| mailchimp.js | static/css/mailchimp.js | PASS | [link](/readme/assets/validation/js/mailchimp.png "link") | Mailchimps file -  Two warnings &  One undefined variable |
| return_to_top_button.js | static/css/return_to_top_button.js | PASS | [link](/readme/assets/validation/js/return_to_top_button.png "link") | One unused variable |
| return_to_top_button.js | static/css/return_to_top_button.js | PASS | [link](/readme/assets/validation/js/return_to_top_button.png "link") | One unused variable |
| show_alert_once.js | static/css/show_alert_once.js | PASS | [link](/readme/assets/validation/js/show_alert_once.png "link") | One unused variable |
| show_toast.js | static/css/show_toast.js | PASS | [link](/readme/assets/validation/js/show_toast.png "link") | One unused variable |
| stripe_elements.js | static/css/stripe_elements.js | PASS | [link](/readme/assets/validation/js/stripe_elements.png "link") | Stripes file - Two unused variable |

[Table of Contents  ⇧](#table-of-contents)
***

## PYTHON

| File Name | File Path | Result | JSHint | Comments |
|--|--|--|--|--|
| calc_item_available_stock.py | basket/templatetags/calc_item_available_stock.py | PASS | [link](/readme/assets/validation/python/basket-calc_item_available_stock.png "link") |  |
| calc_item_subtotal.py | basket/templatetags/calc_item_subtotal.py | PASS | [link](/readme/assets/validation/python/basket-calc_item_subtotal.png "link") |  |
| custom_context_processors.py | basket/custom_context_processors.py | PASS | [link](/readme/assets/validation/python/basket-custom_context_processors.png "link") |  |
| urls.py | basket/urls.py | PASS | [link](/readme/assets/validation/python/basket-urls.png "link") |  |
| views.py | basket/views.py | PASS | [link](/readme/assets/validation/python/basket-views.png "link") |  |
| admin.py | checkout/admin.py | PASS | [link](/readme/assets/validation/python/checkout-admin.png "link") |  |
| apps.py | checkout/apps.py | PASS | [link](/readme/assets/validation/python/checkout-apps.png "link") |  |
| apps.py | checkout/apps.py | PASS | [link](/readme/assets/validation/python/checkout-apps.png "link") |  |
| forms.py | checkout/forms.py | PASS | [link](/readme/assets/validation/python/checkout-forms.png "link") |  |
| models.py | checkout/models.py | PASS | [link](/readme/assets/validation/python/checkout-models.png "link") |  |
| signals.py | checkout/signals.py | PASS | [link](/readme/assets/validation/python/checkout-signals.png "link") |  |
| urls.py | checkout/urls.py | PASS | [link](/readme/assets/validation/python/checkout-urls.png "link") |  |
| views.py | checkout/views.py | PASS | [link](/readme/assets/validation/python/checkout-views.png "link") |  |
| webhook_handler.py | checkout/webhook_handler.py | PASS | [link](/readme/assets/validation/python/checkout-webhook_handler.png "link") |  |
| webhooks.py | checkout/webhooks.py | PASS | [link](/readme/assets/validation/python/checkout-webhooks.png "link") |  |
| custom_storages_aws.py | core/custom_storages_aws.py | PASS | [link](/readme/assets/validation/python/core-custom_storages_aws.png "link") |  |
| sitemaps.py | core/sitemaps.py | PASS | [link](/readme/assets/validation/python/core-sitemaps.png "link") |  |
| urls.py | core/urls.py | PASS | [link](/readme/assets/validation/python/core-urls.png "link") |  |
| views.py | core/views.py | PASS | [link](/readme/assets/validation/python/core-views.png "link") |  |
| forms.py | home/forms.py | PASS | [link](/readme/assets/validation/python/home-forms.png "link") |  |
| urls.py | home/urls.py | PASS | [link](/readme/assets/validation/python/home-urls.png "link") |  |
| views.py | home/views.py | PASS | [link](/readme/assets/validation/python/home-views.png "link") |  |
| admin.py | products/admin.py | PASS | [link](/readme/assets/validation/python/products-admin.png "link") |  |
| convert_image.py | products/convert_image.py | PASS | [link](/readme/assets/validation/python/products-convert_image.png "link") |  |
| custom_context_processors.py | products/custom_context_processors.py | PASS | [link](/readme/assets/validation/python/products-custom_context_processors.png "link") |  |
| forms.py | products/forms.py | PASS | [link](/readme/assets/validation/python/products-forms.png "link") |  |
| models.py | products/models.py | PASS | [link](/readme/assets/validation/python/products-models.png "link") |  |
| urls.py | products/urls.py | PASS | [link](/readme/assets/validation/python/products-urls.png "link") |  |
| views.py | products/views.py | PASS | [link](/readme/assets/validation/python/products-views.png "link") |  |
| admin.py | profiles/admin.py | PASS | [link](/readme/assets/validation/python/profiles-admin.png "link") |  |
| forms.py | profiles/forms.py | PASS | [link](/readme/assets/validation/python/profiles-forms.png "link") |  |
| models.py | profiles/models.py | PASS | [link](/readme/assets/validation/python/profiles-models.png "link") |  |
| urls.py | profiles/urls.py | PASS | [link](/readme/assets/validation/python/profiles-urls.png "link") |  |
| views.py | profiles/views.py | PASS | [link](/readme/assets/validation/python/profiles-views.png "link") |  |
| admin.py | siteadmin/admin.py | PASS | [link](/readme/assets/validation/python/siteadmin-admin.png "link") |  |
| custom_context_processors.py | siteadmin/custom_context_processors.py | PASS | [link](/readme/assets/validation/python/siteadmin-custom_context_processors.png "link") |  |
| forms.py | siteadmin/forms.py | PASS | [link](/readme/assets/validation/python/siteadmin-forms.png "link") |  |
| models.py | siteadmin/models.py | PASS | [link](/readme/assets/validation/python/siteadmin-models.png "link") |  |
| product_filter_tag.py | store/product_filter_tag.py | PASS | [link](/readme/assets/validation/python/store-product_filter_tag.png "link") |  |
| urls.py | store/urls.py | PASS | [link](/readme/assets/validation/python/store-urls.png "link") |  |
| views.py | store/views.py | PASS | [link](/readme/assets/validation/python/store-views.png "link") |  |

[Table of Contents  ⇧](#table-of-contents)
***
# Automated Testing
This was an area I intended to test the codebase for automated tests.
At the beginning of the project, I was happy with the automated tests I had written.
But, as the project progressed, and as adjustments were made to the working views and
models the automated tests were not working as expected and then stopped working.
I spent a little time trying to figure out why, but was not been able to figure it out at the time and my time was better spent working on the codebase, rather than testing it.
I have now managed to fix the issues in the automated testing I have completed, but the coverage is not as good as I would like.
The link to the automated test coverage report is [here](/tests/coverage/html_report/index.html "link").

[Table of Contents  ⇧](#table-of-contents)
***
[Main Readme](/README.md)
***
