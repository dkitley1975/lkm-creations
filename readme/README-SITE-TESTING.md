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
- [Manual Testing](#manual-testing)
- [Lighthouse testing](#lighthouse-testing)

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
| -- | -- | -- | -- | -- |
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
| -- | -- | -- | -- | -- |
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
| -- | -- | -- | -- | -- |
| countryfield.js | static/css/countryfield.js | PASS | [link](/readme/assets/validation/js/countryfield.png "link") | One undefined variable |
| facebook.js | static/css/facebook.js | PASS | [link](/readme/assets/validation/js/facebook.png "link") | One undefined variable |
| mailchimp.js | static/css/mailchimp.js | PASS | [link](/readme/assets/validation/js/mailchimp.png "link") | Mailchimps file -  Two warnings &  One undefined variable |
| return_to_top_button.js | static/css/return_to_top_button.js | PASS | [link](/readme/assets/validation/js/return_to_top_button.png "link") | One unused variable |
| return_to_top_button.js | static/css/return_to_top_button.js | PASS | [link](/readme/assets/validation/js/return_to_top_button.png "link") | One unused variable |
| show_alert_once.js | static/css/show_alert_once.js | PASS | [link](/readme/assets/validation/js/show_alert_once.png "link") | One unused variable |
| show_toast.js | static/css/show_toast.js | PASS | [link](/readme/assets/validation/js/show_toast.png "link") | One unused variable |
| stripe_elements.js | static/css/stripe_elements.js | PASS | [link](/readme/assets/validation/js/stripe_elements.jpg "link") | Stripes file - Two unused variable |

[Table of Contents  ⇧](#table-of-contents)
***

## PYTHON

| File Name | File Path | Result | JSHint | Comments |
| -- | -- | -- | -- | -- |
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
This is the automated test coverage report: [link](/readme/assets/validation/automated-test-coverage.png "link").

[Table of Contents  ⇧](#table-of-contents)
***

# Manual Testing

This is a break down of the manual testing I have done.

| Test | Tested by | Result |
| -- | -- | -- |
| A user can create an account | Creating an account for Peter using the register modal, and the url accounts/signup/ | Peters account showed in the admin panel
| Registration verification email is sent and links work | Created an new account for peter, and email responded to | Peters account in the admin showed email verified |
| Peters user id and email address id are the same | Created an new account for Peter | Peters users details in AUTHENTICATION AND AUTHORIZATION and Email address in ACCOUNTS both have the ID 4 |
|Peter can delete his account | Used the Delete account section in Profile Dashboard | Peters account details are no longer show in the admin panel |
| Bilbo once Signed in can access the registered user areas | Logged Bilbo in | The Navigation area changes from 'Register', 'Sign In' to  'My Account", "Sign Out" |
| Bilbo can only access his own details in the dashboard | Logged Bilbo in and visited the dashboard. | Bilbo's orders appear, but the address bar shows no indication of a user, and a user would be unable to access another account this way. |
| Bilbo can only see his individual order summary's | Logged Bilbo in to his Order History section. He could theoretically guess previous order numbers belonging to other users by guessing random numbers, (The order numbers are random generated numbers and not generated sequentially, to decrease the chances of this). The main prevention of seeing other users orders is if the logged in user.id and the order.id do not match the order summary will not display, showing an error message instead with a Return Home button. | This was fixed in [#59](https://github.com/dkitley1975/lkm-creations/issues/59) - resulting in No access to another users order history |
| Bilbo can only see and edit his own Profile details | Logged Bilbo in to the user dashboard, there is no url indication as to the users id, so unable to guess user.ids to input into the address bar. |  |
| Bilbo can edit his username | With Bilbo logged into the User Dashboard - Update Profile Details, Changed his Profile details, Password and Default Delivery Address | After forms submission the details are updated. |
| Biblo can connect his Google account to his LKM Creations Account | Logged Bilbo in to the user dashboard - Social Accounts and proceeded to connect with Google | Google account connected successfully |
| Biblo can disconnect his Google account from his LKM Creations Account | Logged Bilbo in to the user dashboard - Social Accounts and proceeded to disconnect with Google | Google account disconnected successfully |
| Biblo can connect his Facebook account to his LKM Creations Account | Logged Bilbo in to the user dashboard - Social Accounts and proceeded to connect with Facebook | Currently Failing [#60](https://github.com/dkitley1975/lkm-creations/issues/60) |
| Biblo can disconnect his Google account from his LKM Creations Account | Logged Bilbo in to the user dashboard - Social Accounts and proceeded to disconnect with Google |  |
| Footer links work | Clicked on all links within the footer | All external links open in a new tabs, site links open in the same tab |
| Contact LKM Creations | Through the site, using the Contact Us view from the NavBar the contact form was filled in and submitted | Two email were sent, one to the email used on the form and another to the site admin. These differ in the way they are worded. One is clearly a confirmation for the originator of the contact. The other uses references such as your were contacted. |
|  | clicking on the social media links in the footer and in the emails, you can contact The social media profile owner | Contact is successful through Facebook, The links work for the other social media platforms so contact would be possible through those |
| Navbar Logo Links to Home | Click on Navbar logo | directed to the home page |
| Navbar links work |  |  |
| Sale Items | Clicked on link | Opens in the same tab |
| All Products | Clicked on link | Opens in the same tab |
| Shop By Category | Clicked on links | Opens in the same tab. Displaying the filtered Category results|
| Newsletter Signup | Clicked on link | Opens Modal |
| Bilbo can signup to the Newsletter | Clicked on the Newsletter signup Navbar link and filled in the details and Submitted |  Bilbo's details are submitted and entered in to the mailing list at LKM Creations Mailchimps account |
| Search Bar gives relevant results| Searched for Dolls | Products page opened and showed dolls from product names or category names |
| My Account | Clicked on link | Opens in the same tab |
| Log in | Clicked on link | Opens Modal and allows user to Sign In |
| Log out | Clicked on link | Opens Modal and allows user to Sign Out |
| Basket | Clicked on link | Opens in the same tab |
| Bilbo can browse products | Clicked on the Products links | Opens the relevant Products |
| Bilbo can Navigate through the products | Products are paginated in to 6's. Clicked on the pagination navigation links at the bottom of the screen | Displayed the relevant page dependant on the link clicked and showed the correct page number |
| Bilbo can sort the products | Sorted the Products by price and name, Ascending and Descending | Products are sorted correctly and the pagination navigation works correctly |
| Bilbo can view important information whilst browsing the products  | Clicked on the all products link | The Product cards display the Product Name, Price, and Sale Price, Product Review Ratings, Category and Current Inventory |
| Bilbo can view additional product information | Clicked on Product card | Product Details opened, displaying the products full details |
| Bilbo can share the product socially with friends | Clicked on each of the share socially links | In future the images should adjusted for each platform |
|  | Facebook | Opens the share on facebook, with image, url and description |
|  | Twitter | Opens Twitter, dispalys the Product Name, URL and show the product card. |
|  | Pinterest | Opens Pinterest and allows the board to pin the item to |
|  | LinkedIn | Opens LinkedIn and shares image Product Name and URL |
|  | email | opens email client with message: I absolutely love this 'Beril The Bunny', check it out here <https://lkm-creations.herokuapp.com/store/beril-the-bunny/> |
| Bilbo can view reviews | Viewed the product details page | If there are products reviews, these are displayed. |
| Bilbo can leave a review for a product | left a review as Bilbo | The review and his image appeared after submit. Confirmation toast message received |
| Bilbo can delete his review for a product | clicked on the delete button next to Bilbo's review | The review was removed.Confirmation toast message received |
| Bilbo can only see items in stock | Opened all products, Removed the inventory of a product using the admin panel | The product was removed from the Products view |
| Bilbo can add an item to the basket | Opened a products details page, selected 1 and added to the basket | Item was added to the basket. Confirmation toast message is displayed, with links to basket summary and checkout. basket quantity 1 and subtotal £24.50 appear in the Navbar on the basket icon. |
| Bilbo can amend the quantity in the cart from its product page | After adding 1 to the basket, selected 2 and clicked UPDATE basket quantity | Item quantity was amended to 2 in the basket. Confirmation toast message is displayed, with links to basket summary and checkout. basket quantity 2 and subtotal £49 appear in the Navbar
| Bilbo can remove the product from the cart from its product page | After updating product to 2, now selected 0 and clicked UPDATE basket quantity | Item was removed from the basket. Confirmation toast message is displayed. Basket icon in the Navbar is now empty, clicking on the basket icon show the basket summary with the message the basket is empty.|
| Bilbo shouldn't be able to order more than is in the inventory | Selected the Dinosaur T-Rex and tried to add 5 to the basket, only 2 are available | message that value must be less than or equal to 2 is displayed |
| The inventory is reduced after purchase | I progressed with an order for 1 Dinosaur T-Rex only 2 are available | Order submitted and confirmation toast message is displayed. Emails to site admin and Bilbo are received, Inventory is reduced by 1|
| The inventory is reduced after purchase | I progressed with another order for 1 Dinosaur T-Rex only 1 is available, (site display last one available) | Order submitted and confirmation toast message is displayed. Emails to site admin and Bilbo are received, Inventory is reduced by 1, Product no longer appears in the All Products view, Admin panel confirms: product stock is 0 and Product stock is not available |
| Delivery charge is shown and appropriately charged | Using Bilbo's account an item under £19.99 was added to the basket. | The Confirmation message shows the item is added to the basket, informs that "Spend an additional £5.49 for free delivery: and shows the grand total with delivery |
| Delivery is free when appropriate | Using Bilbo's account a second item to bring the total over £19.99 to the basket. | The Confirmation message shows the item is added to the basket, shows Free Delivery and shows the grand total with free delivery |
| Multiple items can be added to the basket and then manipulated | Using Bilbo's account 4 items are added to the basket, Item quantities are updated, Items are removed, | The adjustment of an items quantity amends the items total and price accordingly, without affecting the quantities or prices of the other items.  |
| THe price is added correctly |Using Bilbo's account 4 items are added to the basket, Item quantities are updated, Items are removed | On updating an item the items quantity and price is amended and added correctly, deleting the item removes the item from the basket. once the subtotal is beneath the free delivery threshold the delivery charge is added |
| Signing Out with items in the basket | Signed in as Bilbo items were added to the basket, I clicked on Sign Out, this opens the modal asking for confirmation and then I logged Bilbo out and logged in as another user | This confirms the log out in a toast message. removing the items from the basket, This is a security feature, the Sign Out clears the basket cookies, helping avoid this being opened up again by another user of the computer |
| Signing In with items in the basket | As a guest items were added to the basket, I clicked on Sign In , this opens the modal to Sign In and I signed in as Bilbo | The items remained in the basket allowing Bilbo to purchase these items |
| Registering with items in the basket | As a guest items were added to the basket, I clicked on Register , this opens the modal to Register and I registered as Peter and confirmed the registration email | The items remained in the basket allowing Peter to purchase these items |
| Purchasing an Item | With items in the basket for Peter, I clicked through to the Checkout, filled in the information, selecting to save the delivery information to the profile. Used the card number 4242 4242 4242 4242 04 24 expiry date 242 CVC and 42424 Postcode.  Clicking confirm payment | Payment is taken, Confirmation message is displayed, and The checkout-success is displayed. |
| Purchasing an Item with incorrect card details | With items in the basket for Peter, I clicked through to the Checkout, filled in the information, selecting to save the delivery information to the profile. Used the card number 5242 4242 4242 4242 04 24 expiry date 242 CVC and 42424 Postcode.  Clicking confirm payment | Payment will not proceed and fails, giving incorrect payment details as the error |
| Print receipts | On the checkout-confirmation view the page is printed | This prints a rerendered version of the view. Items are hidden (such as the navbars etc) and other show to clearly show this as a payment receipt. [link](/readme/assets/site-screenshots/screenshot-dashboard-order-history-details-print-view.png "link"). |
|  | Open the email order confirmation | This gives a full breakdown of the order [link](/readme/assets/site-screenshots/LKM-Creations-Confirmation-for-Order-Number-ED7D0042D57B.jpg "link"). |
| A staff member can add a product through the frontend | Bilbo's user account was changed to Staff Status. Bilbo was then logged in to the main site and the user Dashboard view was opened. No available to Bilbo is another feature in the dashboard menu, being create product. Here All the product details can be added and saved. When the image is selected it is immediately shown in the preview, the details were added and submitted | The product now appears in the product views |
| A staff member can delete review | Logged in to the admin panel, under the reviews selected the review and pressed delete | The Review is deleted, Ideally this needs to happen on the frontend though |
| A staff member can edit a product Frontend | Added staff status to the user Bilbo, browsing to the T-Rex product details view, the edit icon is next to the product name clicking on this opens a revision page. Alterations were made and submitted | The product information was amended |
| A staff member can delete a product Frontend | Added staff status to the user Bilbo, browsing to the T-Rex product details view, the delete icon is next to the product name clicking on this opens a model, This advises the user to use the edit page and set the product as inactive instead, with a direct link to the edit product page. Submit was selected | The product was deleted |
| A staff member can add a product through the backend | Logged in to the admin panel, under the products selected the create product and pressed create | The product was created |
| A staff member can delete a product through the backend | Logged in to the admin panel, under the products selected the delete product and pressed delete | The product was deleted |
| A staff member can edit a product through the backend | Logged in to the admin panel, under the products selected the edit product and pressed edit | The product was edited |
| A staff member can add a review through the backend | Logged in to the admin panel, under the reviews selected the create review and pressed create | The review was created |
| A staff member can delete a review through the backend | Logged in to the admin panel, under the reviews selected the delete review and pressed delete | The review was deleted |
| A staff member can edit a review through the backend | Logged in to the admin panel, under the reviews selected the edit review and pressed edit | The review was edited |
| A staff member can add a category through the backend | Logged in to the admin panel, under the categories selected the create category and pressed create | The category was created |
| A staff member can delete a category through the backend | Logged in to the admin panel, under the categories selected the delete category and pressed delete | The category was deleted |
| A staff member can edit a category through the backend | Logged in to the admin panel, under the categories selected the edit category and pressed edit | The category was edited |

***
[Table of Contents  ⇧](#table-of-contents)

# Lighthouse testing

the following pages were tested on the on the site:
The results varied based on internet connection and the speed of the internet connection. Usually the performance was around 98%.
The Best practices are at 92% as because of the error: "Some third-party scripts may contain known security vulnerabilities that are easily identified and exploited by attackers".
| Page | Performance | Accessibility | Best Practices | SEO | Link |
| -- | -- | -- | -- | -- | -- |
| [Home Page](https://lkm-creations.herokuapp.com/) | 92 | 98 | 92 | 100 | [link](/readme/assets/lighthouse/lighthouse-home-page-report.png "link") |
| [Sale Items](https://lkm-creations.herokuapp.com/store/sale) | 92 | 98 | 92 | 100 | [link](/readme/assets/lighthouse/lighthouse-sales-items-report.png "link") |
| [Category Doll](https://lkm-creations.herokuapp.com/store/category/doll/) | 95 | 98 | 92 | 100 | [link](/readme/assets/lighthouse/lighthouse-categories-report.png "link") |
| [All Products](https://lkm-creations.herokuapp.com/store/products) | 95 | 98 | 92 | 100 | [link](/readme/assets/lighthouse/lighthouse-products-items-report.png "link") |
| [All Products](https://lkm-creations.herokuapp.com/store/Dinosaur-t-rex/) | 91 | 98 | 92 | 100 | [link](/readme/assets/lighthouse/lighthouse-product-details-report.png "link") |
***
[Table of Contents  ⇧](#table-of-contents)
***
[Main Readme](/README.md)
***
