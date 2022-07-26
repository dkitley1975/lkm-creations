[![David's GitHub Banner](/documents/assets/logos/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations <!-- omit in toc -->

[![LKM Creations](/documents/readme-documents/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This is the documentation regarding the creation of an e-commerce website for LKM-Creations.
This is my 5th and final Portfolio Project for the Code Institute's Diploma in Full Stack Development.
The projects purpose:
To build a Full-Stack site based on business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service..

# Table Of Contents

- [Table Of Contents](#table-of-contents)
  - [UX (User Experience)](#ux-user-experience)
    - [User Stories/Epics](#user-storiesepics)
      - [Epic 1 - Core Functionality:](#epic-1---core-functionality)
      - [Epic 2 - Products:](#epic-2---products)
      - [Epic 3 - Orders/Basket:](#epic-3---ordersbasket)
      - [Epic 4 - User Account:](#epic-4---user-account)
      - [Epic 5 - Contact:](#epic-5---contact)
      - [Epic 6 - Reviews:](#epic-6---reviews)
      - [Epic 7 - Admin Functionality:](#epic-7---admin-functionality)
      - [Epic 8 - Marketing:](#epic-8---marketing)
      - [Epic 9: Terms and Policy](#epic-9-terms-and-policy)
- [Project Boards](#project-boards)
  - [*Project Board*](#project-board)
    - [Github Project Board - Issues listed by bug and epics](#github-project-board---issues-listed-by-bug-and-epics)
    - [Github Project Board](#github-project-board)
- [Design](#design)
  - [Database](#database)
  - [Mobile Wireframes](#mobile-wireframes)
  - [Fonts](#fonts)
  - [Colors](#colors)
    - [*Main Colour Pallet*](#main-colour-pallet)
    - [**Shades of the Brand Colours**](#shades-of-the-brand-colours)
- [Languages](#languages)
- [Frameworks and Tools](#frameworks-and-tools)
- [CRUD Functionality](#crud-functionality)
  - [General User](#general-user)
  - [General - Registered User](#general---registered-user)
  - [Staff - Registered User](#staff---registered-user)
- [Site Features](#site-features)
  - [Home Page](#home-page)
    - [Navigation bar](#navigation-bar)
    - [Browse Products](#browse-products)
    - [Product Details](#product-details)

[Testing Documentation](/README_TESTING.md)

## UX (User Experience)

A visitor to LKM Creations! would be someone who is most likely an adult who is either intrested in Armigurumi, or interested in buying custom hand crafted gifts for their loved ones.

### User Stories/Epics

After logging the original user stories these were split in to groups releated to the functionality and features for the site.
I have listed these below.

#### [Epic 1 - Core Functionality:](https://github.com/dkitley1975/lkm-creations/issues/7)

- [x] [#16](https://github.com/dkitley1975/lkm-creations/issues/16) As a user I can intuitively navigate through the site so that I can find the desired content.
- [x] [#17](https://github.com/dkitley1975/lkm-creations/issues/17) As a user  I can find a navigation bar, so I can  easily find important links, such as home, products, the basket, sign in/out, register and my profile.
- [x] [#18](https://github.com/dkitley1975/lkm-creations/issues/18) As a user I can find a footer so that I can find any contact information and any social media links
- [x] [#19](https://github.com/dkitley1975/lkm-creations/issues/19) As a user I can ascertain the purpose of the site from the landing page.
- [x] [#20](https://github.com/dkitley1975/lkm-creations/issues/20) As a user I want to be notified about any changes made, whilst using the site, so I have a clear understanding of what has been completed/updated/failed, such as items added to the basket, updates to my profile, payment confirmation.
- [x] [#21](https://github.com/dkitley1975/lkm-creations/issues/21) As a user I can access the website on both mobile and desktop so that I can view the information regardless of my location.

#### [Epic 2 - Products:](https://github.com/dkitley1975/lkm-creations/issues/8)

- [x] [#22](https://github.com/dkitley1975/lkm-creations/issues/22) As a user I can view all products that are in stock and available to purchase.
- [x] [#23](https://github.com/dkitley1975/lkm-creations/issues/23) As a user I can easily find all of the relevant information about the products so that I can make informed decisions before purchasing.
- [x] [#24](https://github.com/dkitley1975/lkm-creations/issues/24) As a user I can filter the products by categories, alphabetically or by rating, so that i can have more control over what I'm viewing.
- [ ] [#25](https://github.com/dkitley1975/lkm-creations/issues/25) As a user I can choose where relevant the colour as well as the quantity of the products to add to the basket.

#### [Epic 3 - Orders/Basket:](https://github.com/dkitley1975/lkm-creations/issues/9)

- [x] [#26](https://github.com/dkitley1975/lkm-creations/issues/26) As a user I can easily add items to my shopping basket.
- [x] [#27](https://github.com/dkitley1975/lkm-creations/issues/27) As a user I can view a breakdown of my basket so that I can make changes if required.
- [x] [#28](https://github.com/dkitley1975/lkm-creations/issues/28) As a user I can only add items to the cart that are currently in stock.
- [x] [#29](https://github.com/dkitley1975/lkm-creations/issues/29)As a user I am able to process orders by making a card payment.
- [x] [#30](https://github.com/dkitley1975/lkm-creations/issues/30)As a user I want to receive order confirmations to be sure my order has been processed.

#### [Epic 4 - User Account:](https://github.com/dkitley1975/lkm-creations/issues/10)

- [x] [#31](https://github.com/dkitley1975/lkm-creations/issues/31) As a user I can register & log in so that I can view my orders.
- [x] [#32](https://github.com/dkitley1975/lkm-creations/issues/32) As a user I can clearly see if I am signed in, with links to log in or log out.
- [x] [#33](https://github.com/dkitley1975/lkm-creations/issues/33) As a user I am able to reset my account password if required.
- [x] [#34](https://github.com/dkitley1975/lkm-creations/issues/34) As a user I am prompted to register for an account so that I can create an account and receive the benefits of having a profile.
- [x] [#35](https://github.com/dkitley1975/lkm-creations/issues/35) As a user I can log in so that forms can auto-populate with my profile information on the site.
- [x] [#36](https://github.com/dkitley1975/lkm-creations/issues/36) As a user I can save/edit my default billing/shipping details so that I can save time making my next purchase.
- [x] [#37](https://github.com/dkitley1975/lkm-creations/issues/37) As a user I am able to view my previous orders.
- [x] [#38](https://github.com/dkitley1975/lkm-creations/issues/38) As a user I am able to delete my account if required.

#### [Epic 5 - Contact:](https://github.com/dkitley1975/lkm-creations/issues/11)

- [x] [#39](https://github.com/dkitley1975/lkm-creations/issues/39) As a user I can find ways of contacting the site owners, either by email or social media.

#### [Epic 6 - Reviews:](https://github.com/dkitley1975/lkm-creations/issues/12)

- [x] [#41](https://github.com/dkitley1975/lkm-creations/issues/41) As a user I can view reviews of a product, so that the information can help guide me into a purchasing decision.
- [x] [#42](https://github.com/dkitley1975/lkm-creations/issues/42) As a user I can write a review of a product, so that the information can help guide others into a purchasing decision.
- [x] [#43](https://github.com/dkitley1975/lkm-creations/issues/43) As a user I can edit/delete my review of a product, so it is removed if I no longer wish my review to be there.

#### [Epic 7 - Admin Functionality:](https://github.com/dkitley1975/lkm-creations/issues/13)

- [x] [#43](https://github.com/dkitley1975/lkm-creations/issues/43) As an admin user I can log in with administration privileges so that I can access the site's backend.
- [x] [#44](https://github.com/dkitley1975/lkm-creations/issues/44) As an admin user I can access a product management area so that I can make changes in the front end.
- [x] [#45](https://github.com/dkitley1975/lkm-creations/issues/46) As an admin user I can add/edit/remove items from the product list so that I can make sure the website is up to date and accurately reflects what is being sold.
- [x] [#46](https://github.com/dkitley1975/lkm-creations/issues/46) As an admin user I can update the stock levels for the products so that customers are only able to purchase items in stock.
- [x] [#47](https://github.com/dkitley1975/lkm-creations/issues/47) As an admin user I can receive an email from a user that fills in a contact form, so that I can answer any questions they may have

#### [Epic 8 - Marketing:](https://github.com/dkitley1975/lkm-creations/issues/14)

- [x] [#48](https://github.com/dkitley1975/lkm-creations/issues/48) As a user I can sign up to a newsletter so I can  be kept up to date with information regarding new items for sale.
- [x] [#49](https://github.com/dkitley1975/lkm-creations/issues/49) As an admin user  I can implemented SEO keywords to increase traction to my website.
- [x] [#50](https://github.com/dkitley1975/lkm-creations/issues/50) As an admin user I can link the created Facebook shop page to my site so the I can increase traction to my website.

#### [Epic 9: Terms and Policy](https://github.com/dkitley1975/lkm-creations/issues/15)

- [x] [#51](https://github.com/dkitley1975/lkm-creations/issues/51) As a user, I can view the Terms and Conditions document via a link in the footer of the site.
- [x] [#52](https://github.com/dkitley1975/lkm-creations/issues/52) As a user, view a privacy policy document via a link in the footer of the site

[Table of Contents  ⇧](#table-of-contents)

***

# Project Boards

I Used Github's Project board to plan the project and Github Issue's for User Stories and Tasks

## *Project Board*

### [Github Project Board - Issues listed by bug and epics](https://github.com/users/dkitley1975/projects/12/views/1)

![Project Board - Issues listed by bug and epics](/documents/readme-documents/projectboard/LKM-CREATIONS-project-boards-issues-list.jpg)

### [Github Project Board](https://github.com/users/dkitley1975/projects/12/views/3?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Labels)

![Project Board](/documents/readme-documents/projectboard/LKM-CREATIONS-Project-board.jpg)

[Table of Contents  ⇧](#table-of-contents)

***

# Design

## Database

Image showing the database Scheme for LKM-CREATIONS
![LKM-Creations Database Scheme](/documents/readme-documents/schema/LKM-CREATIONS-database-schema.jpg)

## Mobile Wireframes

![MOBILE](/)

***

## Fonts

The default Sans-Serif is used as the main font. I was unnecessary to change the default font type as this is an easy font to read and displays well throughout the site.

The Logo is pre-designed and uses Caveat from Google
![image](/documents/readme-documents/logo/LKM-CREATIONS-logo.png)
***

## Colors

I have used these prexisting existing brand colours throughout the site.

### *Main Colour Pallet*

  ![Brand Primary Colour #e27c7c](https://via.placeholder.com/30/e27c7c/e27c7c.png) `Brand Primary Colour #e27c7c`

![Brand Secondary Colour #FFD9C0](https://via.placeholder.com/30/FFD9C0/FFD9C0.png) `Brand Secondary Colour #FFD9C0`

  ![Brand Tertiary Colour #FAF0D7](https://via.placeholder.com/30/FAF0D7/FAF0D7.png) `Brand Tertiary Colour #FAF0D7`

### **Shades of the Brand Colours**

*These are the shades of the brand colours used throughout the site.
These were needed as there isn't enough contrast between the brand colours.*

![Brand Primary Lightest Colour #fcf4f47a](https://via.placeholder.com/30/fcf4f47a/fcf4f47a.png) `Brand Primary Lightest Colour #fcf4f47a`

![Brand Primary light Colour #ffe0e0](https://via.placeholder.com/30/ffe0e0/ffe0e0.png) `Brand Primary light Colour #ffe0e0`

![Brand Primary Darker Colour #ce7b7b](https://via.placeholder.com/30/ce7b7b/ce7b7b.png) `Brand Primary Darker Colour #ce7b7b`

![Brand Primary Darkest Colour #751818](https://via.placeholder.com/30/751818/751818.png) `Brand Primary Darkest Colour #751818`

![Brand Secondary Darker Colour #fabd95](https://via.placeholder.com/30/fabd95/fabd95.png) `Brand Secondary Darker Colour #fabd95`

[Table of Contents  ⇧](#table-of-contents)
***

# Languages

- HTML
- CSS
- JavaScript
- Python
- Django

[Table of Contents  ⇧](#table-of-contents)
***

# Frameworks and Tools

- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Django](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com/home)
- [Postgres](https://www.postgresql.org/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [W3C HTML Validation](https://validator.w3.org/)
- [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
- [pep8online](http://pep8online.com/)
- [color.a11y.com](https://color.a11y.com/Contrast/)
- [Pixabay](https://pixabay.com/)
- [TinyPNG](https://tinypng.com/)

[Table of Contents  ⇧](#table-of-contents)
***

# CRUD Functionality

## General User

As a **General User** of the site, I am able to browse and read the website, the pages I read have data pulled from tables in a remote database.

## General - Registered User

As a **General Registered User** browser of the site, I am able do the same as the **General User**. In addition I am able to create *Reviews* for products, uploading a supporting image.
I can also *Delete* a *Review* I made previously.
I also have access to *My Account* menu item which allows me access to a User DASHBOARD area. Here I  *Update* my *Password*,  *Update* my *User Profile Details*, *Update* my *My default delivery Address* and *Delete* my *Account*.

## Staff - Registered User

As a Staff Registered User, I can do all that the **General - Registered User** can do, I have access to a *Create Product* menu within the User DASHBOARD.
This links to a *Create Product* page, where I can *Create* a new *Product*.
There is a message recommending that I use the Admin panel for this though and supplies a link to the Admin panel Add Product section.

When viewing a Product I also see a link to *Update* the Product, and *Delete* the Product.
Clicking the link to edit a Product, I am able to *Update* the Product, updating information and replacing the image, which displays a preview immediately.
There is a message recommending that I use the Admin panel for this though and supplies a direct link for this products edit section in the Admin Panel.

Clicking on the Delete link I am able to *Delete* the Product.
Again there is a message recommending that I use the Admin panel for this though and instead set the product to inactive instead and supplies a direct link for this products edit section in the Admin Panel.

I can also *Delete* any *Review*.

I have access to the Admin panel where I can Create, Read, Update and Delete all the information.
Creating, Editing, Updating and Deleting the *Products*, *Categories*, *Reviews*, *Users*, *Addresses*, *Orders*, *Payments*

[Table of Contents  ⇧](#table-of-contents)
***

# Site Features

The website has the following features:

## Home Page

### Navigation bar

- The navigation bar is present at the top of every page and houses all links to the various other pages.
- The active page will be shown to have a bolder font helping users understand what page they're on.
- Hovering over the links will lighten the font slightly.
- The options to Register or Log in change to the option to log out once a user has logged in.
- Once a user has signed in, The 'My Account' become available.
- A search bar is nested in the navbar to search for items on the site.
- There is a Newsletter sign up form on the navbar. This opens a modal, using Mailchimp as its provider.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes small.

Desktop Navbar Signed Out
![Navbar](/documents/readme-documents/site-screenshots/desktop/navigation-bar.png)

Desktop Navbar Signed In
![Navbar Signed In](/documents/readme-documents/site-screenshots/desktop/navigation-bar-signed-in.png)

Mobile Navbar Signed Out

![Navbar](/documents/readme-documents/site-screenshots/mobile/navigation-bar.png)

Mobile Navbar Signed In

![Navbar Signed In](/documents/readme-documents/site-screenshots/mobile/navigation-bar-signed-in.png)

Mobile Navbar Collapsed

![Navbar Signed In](/documents/readme-documents/site-screenshots/mobile/navigation-bar-collapsed.png)

### Browse Products

- Browsing the products, You can view the products by, Sale Items, All Products and Category.
- The active page will be shown to have a bolder font helping users understand what page they're on.
- The total amount of products in the view is shown on screen.
- There is the ability to sort the products by name or price. Either assending or descending order.
- A search bar is nested in the navbar to search for items on the site.
- Each product cards displays the product name, image, price, sale price, rating if any, category and inventory.
- The page is fully responsive, reducing the amount of product cards on each row dependant on the screen size.
- The product cards are clickable and will take you to the product page.
- The product card images are in WEBP format, this is to reduce the amount of data being sent to the browser. But there are fallback jpg images for when the browser does not support webp.

[Table of Contents  ⇧](#table-of-contents)

Desktop Products list
![Navbar](/documents/readme-documents/site-screenshots/desktop/products-view.png)

Mobile Products list

![Navbar](/documents/readme-documents/site-screenshots/mobile/products-view.png)

### Product Details

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



Desktop Product Details
![Navbar](/documents/readme-documents/site-screenshots/desktop/product-details.png)

Mobile Product Details - Signed In

![Navbar](/documents/readme-documents/site-screenshots/mobile/product-details.png)

Product Review

![Navbar](/documents/readme-documents/site-screenshots/desktop/product-review.png)

[Table of Contents  ⇧](#table-of-contents)