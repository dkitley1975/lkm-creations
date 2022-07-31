[![David's GitHub Banner](/readme/assets/logo/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations <!-- omit in toc -->

[![LKM Creations](/readme/assets/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This documentation explains the site features with screenshots of each section.
It goes through the site, from landing on the home page, purchasing items, basket summary, the checkout page, order summary, profile pages and much more.

# Table Of Contents

- [Table Of Contents](#table-of-contents)
- [Site Features](#site-features)
  - [Home Page](#home-page)
  - [Common Features](#common-features)
    - [Navigation bar](#navigation-bar)
    - [Footer](#footer)
  - [Browsing Products](#browsing-products)
  - [Sorting Products](#sorting-products)
  - [Product Details](#product-details)
  - [Basket Notifications](#basket-notifications)
  - [Basket Summary](#basket-summary)
  - [Checkout](#checkout)
    - [Order Confirmation emails](#order-confirmation-emails)
    - [User order confirmation email](#user-order-confirmation-email)
    - [Admin order confirmation email](#admin-order-confirmation-email)
  - [Registration](#registration)
- [User Dashboard](#user-dashboard)
  - [Update User Details](#update-user-details)
  - [Social Account Connections](#social-account-connections)
  - [Order History](#order-history)
  - [Contact Us](#contact-us)
  - [Newsletter](#newsletter)
  - [Site Policies](#site-policies)
  - [Error Pages](#error-pages)
  - [Site Maps](#site-maps)
    - [Rich Results](#rich-results)

# Site Features

The website has the following features:

## Home Page

One of the most important features of the website is the *Home Page*.
This is the first page that is displayed when the user visits the website.

On opening the site for the first time, a cookies disclaimer is displayed to the user. This is to ensure that the user is aware of the cookies that are being used on the site.
The cookies disclaimer can be dismissed by clicking the *Got it!* button.
Also displayed is a Site information message. This is to inform the user of any information the site owner wishes. Such as store holidays. This message can be dismissed by clicking the *close* button.
Additionally, the *Home Page* also contains a *Product Sales* section.
*Home Page*
![Home Page](/readme/assets/site-screenshots/screenshot-home-page.png)
[Table of Contents  ⇧](#table-of-contents)

## Common Features

This features include the *Navbar* which contains a *Logo*, a *Search Bar* and a *Basket* icon.
The *Navbar* is also used to display the *Categories* and *Products* that are available for sale.
The *Search Bar* allows the user to search for a *Product* by name or category.
The *Basket* icon displays the number of items in the basket and the current total price.

### Navigation bar

- The navigation bar is present at the top of every page and houses all links to the various other pages.
- The active page will be shown to have a bolder font helping users understand what page they're on.
- Hovering over the links will lighten the font slightly.
- The options to Register or Log in change to the option to log out once a user has logged in.
- Once a user has signed in, The 'My Account' become available.
- A search bar is nested in the navbar to search for items on the site.
- There is a Newsletter sign up form on the navbar. This opens a modal, using Mailchimp as its provider.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes small.

*Navbar Signed Out*
![Navbar Signed Out](/readme/assets/site-screenshots/screenshot-nav-bar-signed-out.png)

*Navbar Signed In*
![Navbar Signed In](/readme/assets/site-screenshots/screenshot-nav-bar-signed-in.png)
[Table of Contents  ⇧](#table-of-contents)

### Footer

The footer is present at the bottom of every page and houses links to the sites social media, on the desktop site a link to the site cookies, privacy information and other  documentation. As well as the site copyright information

*Footer*
![Footer](/readme/assets/site-screenshots/screenshot-footer.png)
[Table of Contents  ⇧](#table-of-contents)

## Browsing Products

- Browsing the products, You can view the products by, Sale Items, All Products and Category.
- The active page will be shown to have a bolder font helping users understand what page they're on.
- The total amount of products in the view is shown on screen.
- There is the ability to sort the products by name or price. Either assending or descending order.
- A search bar is nested in the navbar to search for items on the site.
- Each product cards displays the product name, image, price, sale price, rating if any, category and inventory.
- The page is fully responsive, reducing the amount of product cards on each row dependant on the screen size.
- The product cards are clickable and will take you to the product page.
- The product card images are in WEBP format, this is to reduce the amount of data being sent to the browser. But there are fallback jpg images for when the browser does not support webp.
- 6 products are shown to a page by default and a navigation panel is shown beneath the products with an indicator for the current page. Additional products can be viewed by clicking the next or previous buttons.

*Products list (top of the page)*
![Products listings page - Bottom of Screen](/readme/assets/site-screenshots/screenshot-products-page-top.png)
*Products list (bottom of the page)*
![Product listings - Bottom of Screen](/readme/assets/site-screenshots/screenshot-products-page-bottom.png)
[Table of Contents  ⇧](#table-of-contents)

## Sorting Products

On the *Products* page, *Sale Items*page and *Category* pages you can sort the products by, Price, Name, by Ascending and Descending order.
The pagination is also shown on the page and the links to the next, previous pages and individual page numbers respect the sort and search queries.

Custom template filter

```Python
@register.simple_tag()
def paginated_filter(value, field_name, urlencode=None):
 url = "?{}={}".format(field_name, value)
 if urlencode:
  querystring = urlencode.split("&")
  filtered_querystring = filter(
   lambda p: p.split("=")[0] != field_name, querystring
  )
  encoded_querystring = "&".join(filtered_querystring)
  url = "{}&{}".format(url, encoded_querystring)
 return url

```

Navigation link

```HTML
<a href="{% paginated_filter i 'page' request.GET.urlencode %}">{{ i }}</a>

```

[Table of Contents  ⇧](#table-of-contents)

## Product Details

- There is a large image of the product.
- There is a description of the product.
- There is a rating of the product.
- There is a price of the product.
- The Sale price is shown if applicable with the original price Striked out.
- The Inventory is shown.
- There is a button to add the product to the basket.
- If a product is added to the basket, the basket icon in the Navbar  updates the total price.
- If the quantity is amended and added to the basket after previously being added, it replaces the product quantity instead of adding it to the products basket total. I have done it this way because the inventory is used to determine the quantity of the product available in the quantity input, and it is not possible to add more than the inventory amount of products to the basket.
- The product images are in WEBP format, this is to reduce the amount of data being sent to the browser. But there are fallback jpg images for when the browser does not support webp.
- The reviews are displayed in a list, with the most recent review at the top. if there is a image associated with the review it is displayed, otherwise the area is made available to display the review.
- There is a signin to review product button. If a user is not signed in, they will be prompted to sign in before they can review the product. This is to ensure that only registered users can review products. The review is entered in a modal.

*Product Details (top of page)*
![Product Details page - Top of Screen](/readme/assets/site-screenshots/screenshot-product-details.png)

*Product Details (bottom of page)*
![Product Details page - Bottom of Screen](/readme/assets/site-screenshots/screenshot-product-details-bottom.png)

*Product Leave A Review*
![Leave a review](/readme/assets/site-screenshots/screenshot-leave-a-review.png)

*Product purchase options (before adding to basket)*

![Purchase button - showing add to basket prior to item added to basket](/readme/assets/site-screenshots/screenshot-product-details-purchase-option-if-not-in-basket.png)

*Product purchase options (after adding to basket)*

![Purchase button - showing update product after item added to basket](/readme/assets/site-screenshots/screenshot-product-details-purchase-option-if-in-basket.png)

*Product purchase options (select quantity 0 to remove product)*
![Purchase Quantity - set to 0 to remove product](/readme/assets/site-screenshots/screenshot-product-details-purchase-option-to-remove-product.png)

*Product Item added to basket (showing basket quantity and total price in the Nav Bar)*
![Navbar with product showing in the basket](/readme/assets/site-screenshots/screenshot-nav-bar-item-in-basket.png)

[Table of Contents  ⇧](#table-of-contents)

## Basket Notifications

When a product is added to the basket, a notification is displayed in a toast by the navbar.
The notification contains the product name, quantity and total price.
When a product is updated in the basket, the notification confirms the product has been updated.
When a product is removed from the basket, the notification confirms the product has been updated.
The notification can be dismissed by clicking the *close* button, but will autohide after a short duration.
If there are items in the basket and the user is not viewing the basket summary, the notification also includes a full basket summary, and buttons to view the basket or checkout.

*Toast Notification (Item added to basket)*

![Toast Notification - Item Added](/readme/assets/site-screenshots/screenshot-toast-success-item-added-to-basket.png)

*Toast Notification (Item updated in basket)*

![Toast Notification - Item Updated](/readme/assets/site-screenshots/screenshot-toast-success-item-updated-in-basket.png)

*Toast Notification (Item removed from basket)*

![Toast Notification - Item Deleted](/readme/assets/site-screenshots/screenshot-toast-success-item-removed-to-basket.png)

## Basket Summary

By clicking on the *Basket icon* in the Navbar or basket notification toaast, the user is taken to the Basket Summary page.
The Basket Summary page displays an image of the product, the product name, a trunculated description of each product.
It allows the user to update the required quantity, displaying the current inventory available, and remove the product from the basket.
It also display the Subtotal, Delivery Price and the total price.

*Basket Summary (top)*

![Basket Summary - Top of Screen](/readme/assets/site-screenshots/screenshot-basket-summary-top.png)

*Basket Summary (bottom - subtotal over the price given in the Modal Site Information)*
![Basket Summary - Bottom of Screen with out Delivery Charge](/readme/assets/site-screenshots/screenshot-basket-summary-no-delivery-charge.png)

*Basket Summary (bottom - subtotal under the price given in the Modal Site Information)*
![Basket Summary - with Delivery Charge](/readme/assets/site-screenshots/screenshot-basket-summary-delivery-charge.png)

[Table of Contents  ⇧](#table-of-contents)

## Checkout

The checkout page is the final page of the purchase. It displays the products in the basket, the total price, the delivery price and the total price including the delivery price.
The user can enter their details and payment details.
If the user is registered and signed in, they can save their details as future preferred delivery details.
If the user is not registered, they can sign up for an account.

*Checkout (top)*
![Checkout Top of Screen](/readme/assets/site-screenshots/screenshot-checkout-top.png)

*Checkout (bottom)*
![Checkout Bottom of Screen](/readme/assets/site-screenshots/screenshot-checkout-bottom.png)

On submission of the payment details, the order is processed through *Stripe* and the user is redirected to the payment confirmation page.

*Checkout (processing)*
![Checkout Processing](/readme/assets/site-screenshots/screenshot-checkout-processing.png)
Ater the order is processed, the user is redirected to the order confirmation page.
This page displays the order number, the date and time of the order, the products in the order, the total price, the delivery price and the total price including the delivery price.
The user can print this page out as their receipt. As the items on screen which are irrelevant are hidden from print, and additional required items are added to the page but hidden from display.

The page The user can also view the order in their Dashboard *Orders* page.

*Order confirmation*
![Order Confirmation](/readme/assets/site-screenshots/screenshot-order-confirmation.png)

*Order confirmation - printed version from the order confirmation page*
![Order Confirmation Print](/readme/assets/site-screenshots/LKM-Creations-Order-0F01B6E8D335.png)

### Order Confirmation emails

When an order is placed, an email is sent to the user with the order details.

### User order confirmation email

>Hello Bilbo Baggins!
>This is a confirmation of your order at LKM Creations . Your order information is below:
>
>Order Number: 15468546EED1
>Order Date: July 29, 2022, 12:33 p.m.
>
>
>
>
>
>Beril The Bunny (sku: 56392)
>
>Item total = £10.00 (1 x £10.00)
>***
>
>Dinosaur T-Rex (sku: 56403)
>
>Item total = £24.50 (1 x £24.50)
>***
>
>Bunny Doll (sku: 56389)
>
>Item total = £22.49 (1 x £22.49)
>***
>
>
>Subtotal: £56.99
>Delivery: £0.00
>Grand Total: £56.99
>
>Your selected Delivery address is:
>Bilbo Baggins
>Bag End,
>1 Bagshot Row,
>Hobbington, The Shire,
>Middle-earth, Arda,
>BE1 2SH,
>GB,
>
>
>We've got your contact number for this order as as 0123456789.
>
>If you have any questions, feel free to contact us at lkm-creations@kitley-mcnamara.com.
>
>You can view your order details here: https:/lkm-creations.herokuapp.com/dashboard/order-summary15468546EED1
>
>If you have an account you can view your previous orders, link your social acount to your LKM Creations account and update your profile information here: <https://lkm-creations.herokuapp.com/dashboard/>
>
>Thank you for your valued order!
>
>Sincerely,
>
>LKM Creations
>lkm-creations@kitley-mcnamara.com
>Please follow our facebook page for regular updates regarding new products and offers.

### Admin order confirmation email

An email is also sent to the Site Administrator with the order details.

>Hello LKM Creations
>
>This is a confirmation of an order at LKM Creations .
>The order information is as below:
>
>Order Number: 15468546EED1
>Order Date: July 29, 2022, 12:33 p.m.
>Cleint Name: Bilbo Baggins
>
>
>
>
>Beril The Bunny (sku: 56392)
>
>Item total = £10.00 (1 x £10.00)
>***
>
>Dinosaur T-Rex (sku: 56403)
>
>Item total = £24.50 (1 x £24.50)
>***
>
>Bunny Doll (sku: 56389)
>
>Item total = £22.49 (1 x £22.49)
>***
>
>
>Subtotal: £56.99
>Delivery: £0.00
>Grand Total: £56.99
>
>The Delivery address is:
>Bilbo Baggins
>Bag End,
>1 Bagshot Row,
>Hobbington, The Shire,
>Middle-earth, Arda,
>BE1 2SH,
>GB,
>
>
>We received this contact number for the order: 0123456789.
>
>
>You can view the order details here: <https://lkm-creations.herokuapp.com/admin/checkout/orderdetails/10/change/>
>
>Sincerely,
>
>LKM Creations
>
>lkm-creations@kitley-mcnamara.com

[Table of Contents  ⇧](#table-of-contents)
***

## Registration

The link to the registration page from the navigation bar. Takes the user to the registration page. This uses Django's built in registration system. Once the user has registered, they are sent an email requesting they confirm their email. On following the link in the email, the user is redirected to the login page.

*Registration*
![Registration Page](/readme/assets/site-screenshots/screenshot-registration.png)
*Sign in page*
![Sign In Page](/readme/assets/site-screenshots/screenshot-sign-in-page.png)

Once the user has registered the user profile is created for the automatically, this ensures that the user id and profile id are identical.

The user can Sign in and Sign out of the site. using links in the navigation bar. Using either their username or email address.
There is the ability to link their social account to their LKM Creations account.

*Sign in Modal*
![Sign in Modal](/readme/assets/site-screenshots/screenshot-sign-in-modal.png)
*Sign out Modal*
![Signout Modal](/readme/assets/site-screenshots/screenshot-sign-out-modal.png)
*Signin/out confirmation*
![Sign In Out Confirmation](/readme/assets/site-screenshots/screenshot-sign-out-in-confirmation.png)

# User Dashboard

The user dashboard is accessible using the My Account link in the navigation bar. This is only visible and accessible to the user if they are logged in. If you are not logged in, you will be redirected to the login page, which will then redirect back to the dashboard.

*User Dashboard*
![User Dashboard](/readme/assets/site-screenshots/screenshot-dashboard-home.png)

The User Dashboard contains a selection of links to the user's account.
The user can view their order history, view their profile, and update their profile. They can connect their social accounts to their LKM Creations account and delete their account
The dashboard navigation. On larger screens the navigation displays under the main navigation. on smaller screens the navigation is a collapsable menu.

*User Dashboard Navigation*
![User Dashboard Navigation](/readme/assets/site-screenshots/screenshot-dashboard-navigation.png)

## Update User Details

Here the user can update their profile details.
Change the user's email address, password, and address.
Change the default delivery address.
With an option to delete their account.

*User Update Details (top of page)*
![User Update Details top of page](/readme/assets/site-screenshots/screenshot-dashboard-update-account-top.png)
*User Update Details (bottom of page)*
![User Update Details bottom of page](/readme/assets/site-screenshots/screenshot-dashboard-update-account-bottom.png)

*User Delete Account*
![User Delete Account](/readme/assets/site-screenshots/screenshot-dashboard-delete-account.png)

## Social Account Connections

Here the user can connect and to remove the links to their social accounts and their LKM Creations account.

*User Update Details (top of page)*
![User Update Details top of page](/readme/assets/site-screenshots/screenshot-dashboard-connect-social.png)

## Order History

Here the user can view their order history.
Each order connected with their account is displayed as a summary in a card.
This displays the order number, date, items and total.
The user can view the order details by clicking the view order button.
*User Dashboard Previous Orders*
![User Dashboard Previous Order History](/readme/assets/site-screenshots/screenshot-dashboard-order-history.png)

Clicking the view order button will take the user to the order details page.
*User Previous Order Details*
![User Dashboard Previous Order Details Top](/readme/assets/site-screenshots/screenshot-dashboard-order-history-details-top.png)
![User Dashboard Previous Order Details Bottom](/readme/assets/site-screenshots/screenshot-dashboard-order-history-details-bottom.png)

The order details page when printed removes elements from the display that are not necessary for the receipt.
*User Previous Order Details Print version*
![User Dashboard Previous Order Details Top](/readme/assets/site-screenshots/screenshot-dashboard-order-history-details-print-view.png)
[Table of Contents  ⇧](#table-of-contents)
***

## Contact Us

Here the user can contact us.
The user can send an email message to the site, by filling in the contact form.
The user receives a confirmation email and the site admin receives an email.

*Contact Us Form*
![Contact Us Form](/readme/assets/site-screenshots/screenshot-contact-form.png)

*Email to user from Contact Us Form*
>Subject: LKM_Creations Contact Form - sent confirmation
>From: address@gmail.com
>To: test@test.com
>Date: Fri, 29 Jul 2022 19:41:46 -0000
>
>Thank you Peter The information you sent was as follows:
>Phone: 0123456789
>Email: test@test.com
>
>
>This is your enquiry:
>I would like to enquire about the lovely T-Rex I saw last week, has this item  sold out? if so would you be able to make me one for my nephew, preferably in a green and yellow.
>BR
>Peter
>
>
>We will respond to your message shortly.
>Best Regards,
>Leanne
>
*Email to Site Owner from Contact Us Form*
>Subject: LKM_Creations Contact Form - sent confirmation
>From: address@gmail.com
>To: lkm-creations@kitley-mcnamara.com
>Date: Fri, 29 Jul 2022 19:41:46 -0000
>
>You have been contacted via the online contact form.
>
>Peter Smith has emailed you.
>Phone: 0123456789
>Email: test@test.com
>
>
>This is their enquiry:
>I would like to enquire about the lovely T-Rex I saw last week, has this item  sold out? if so would you be able to make me one for my nephew, preferably in a green and yellow.
>BR
>Peter
>
[Table of Contents  ⇧](#table-of-contents)
***

## Newsletter

The user can subscribe to the newsletter.
This functionality is handled by the newsletter sign up form.
It uses Mailchimp to handle the subscription.
I have enable Mailchip to handle the subscription sign ups and mailings of the Newsletters. Using this service will help to ensure that the newsletters are sent to the correct email address. Allow users to unsubscribe from the newsletter easily.

I have embedded the newsletter sign up form within a model.
Once the user has signed up, the modal remains on screen with a Success message displayed.

*Mailchimp Newsletter sign up*
![Mailchimp Newsletter sign up](/readme/assets/site-screenshots/screenshot-newsletter-sign-up.png)

[Table of Contents  ⇧](#table-of-contents)
***

## Site Policies

The user can view the site policies.
The menu location for the site policies is in the footer on the larger screens and in the main menu on the small screens.
The site policies are also linked from the cookie policy agreement displayed on the first visiting the site.
The smaller screen has a drop down menu for the site policies.
Where the larger screens have the menu on the left side of the page.

*Site Policy Documents*
![Site Policy Documents](/readme/assets/site-screenshots/screenshot-site-policy-readme.png)

[Table of Contents  ⇧](#table-of-contents)
***

## Error Pages

The error pages are customised for each error.
The error pages are displayed when an error occurs.
Each page has an error code and a message.
The error code is displayed in the header.
The message is displayed in the body.
Each page has an email link which prefills the information with
mailto: lkm-creations@kitley-mcnamara.com
Subjet: LKM Creations 404 Error or 400, 403, 500  etc

*400 Error Page*
![400 Error](/readme/assets/site-screenshots/screenshot-400-error.png)
*403 Error Page*
![403 Error](/readme/assets/site-screenshots/screenshot-403-error.png)
*404 Error Page*
![404 Error](/readme/assets/site-screenshots/screenshot-404-error.png)
*500 Error Page*
![500 Error](/readme/assets/site-screenshots/screenshot-500-error.png)
[Table of Contents  ⇧](#table-of-contents)
***

## Site Maps

Site maps are created dynamically each time they are requested, ensuring that the site is always up to date.
The code below is the code used to create the site maps.

urls
```urls

from .sitemaps import CategorySitemap, ProductSitemap, StaticSitemap

sitemaps = {
    "products": ProductSitemap,
    "static": StaticSitemap,
    "categories": CategorySitemap,
}

path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
```






Python
```from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from products.models import Category, Product


class ProductSitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the products.
    """

    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Product.available_items.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return "/store/%s" % (obj.slug)


class CategorySitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the categories.
    """

    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return "/store/category/%s" % (obj.slug)


class StaticSitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the main static pages with important content.
    """

    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            "home:home",
            "home:privacy-policy",
            "home:terms-of-service-policy",
            "home:returns-policy",
            "home:disclaimer-policy",
            "home:shipping-policy",
            "home:cookie-policy",
        ]

    def location(self, item):
        return reverse(item)
```

The sitemap can be viewed using the following URL:

```
lkm-creations.herokuapp.com/sitemap.xml
```
this is the output of the sitemap.xml file.
```
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<url>
<loc>https://lkm-creations.herokuapp.com/store/albino-whale</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/alpaca</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/baby-bella-bunny-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/beril-the-bunny</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/berlinda-the-bunny</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/brenda-the-bunny</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/bumble-bee</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/bunny-doll</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/bunny-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/bunny-siblings</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/buzzy-bee-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/christine-the-cow</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/dinosaur-t-rex</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/dinosaur-triceratops</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/dog-pug</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/doll</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/doll-jessica</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/gina-the-giraffe-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/hedgehog-pattern</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/hettie-the-highland-cow-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/jellyfish</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/jolly-jellyfish</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/lionel-the-lion-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/sarah-the-sheep-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/sean-the-seagull</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/simon-the-shark</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/teddy-bear</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/teddy-bear-and-rabbit-pattern</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/terrance-the-triceratops</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/terry-the-turtle</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/thomas-the-turtle</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/turtles-pair</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/willma-the-whale</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/willma-the-whale-kit</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/willy-the-whale</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/winnie-the-whale</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-black</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-blue</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-brown</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-green</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-grey</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-indigo</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-lilac</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-orange</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-pink</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-purple</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-red</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-violet</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-white</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/yarn-yellow</loc>
<lastmod>2022-03-12</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/privacy-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/terms-of-service-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/returns-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/disclaimer-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/shipping-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/documents/cookie-policy</loc>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/accessories</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/doll</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/kit</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/pattern</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/stuffed-animal</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
<url>
<loc>https://lkm-creations.herokuapp.com/store/category/yarn</loc>
<lastmod>2022-07-30</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url>
</urlset>
```

### Rich Results

Rich Results are applied dynamically in the product-details page.
the following code is used to apply the rich results to the product-details page.

```
<script type="application/ld+json">
 {
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "{{ product.name|title }}",
  "image": [
   "{{ product.image.url }}"
  ],
  "description": "{{ product.description }}",
  "sku": "{{ product.sku }}",
  "brand": {
   "@type": "Brand",
   "name": "LKM-Creations"
  },
  "review": {
   "@type": "Review",
   "reviewRating": {
    "@type": "Rating",
    "ratingValue": "{{ lastreview.rating }}",
    "bestRating": "{{ product.get_review_highest_rating }}"
   },
   "author": {
    "@type": "Person",
    "name": "{{ lastreview.created_by }}"
   }
  },
  "aggregateRating": {
   "@type": "AggregateRating",
   "ratingValue": "{{ product.get_review_average_rating }}",
   "reviewCount": "{{ product.get_review_count }}"
  },
  "offers": {
   "@type": "Offer",
   "url": "https://{{ request.site.domain }}/store/{{ product.slug }}",
   "priceCurrency": "GBP",
   "price": "{{ product.retail_price}}",
   "itemCondition": "https://schema.org/NewCondition",
   "availability": "https://schema.org/InStock"
  }
 }
</script>
```

and tested here: [Rich-Results](https://search.google.com/test/rich-results "rich-results")
There are two warnings regarding optional values:
The first is that the brand of the product is invalid. There is now brand applicable.
The second is that optional field  'priceValidUntil' is missing. This is because this value has not been supplied and is not required.
*Rich-Results*
![Rich-Results](/readme/assets/site-screenshots/Rich-Results-Test-Google-Search-Console.jpg)

*Google Card Preview*
![Google Card Preview](/readme/assets/site-screenshots/Rich-Results-Test-Google.png)

[Table of Contents  ⇧](#table-of-contents)
***

[Main Readme](/README.md)

***
