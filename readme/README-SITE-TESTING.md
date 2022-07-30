[![David's GitHub Banner](//homepage.png/logo/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations <!-- omit in toc -->

[![LKM Creations](//homepage.png/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This document contains a breakdown of the testing preformed on the LKM-Creations website.

# Table Of Contents

- [Table Of Contents](#table-of-contents)
	- [Code Validation](#code-validation)
		- [HTML](#html)



## Code Validation
### HTML
To Check the html code for errors, each page was opened in a browser and the view page source command was used.
This code was copied and pasted in to [validator.w3.org](https://validator.w3.org/nu/#textarea "link") This issued a warning that the html code was not valid. The warning was fixed by performing any alterations required and the page code was tested again.
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

[Main Readme](/README.md)

***
