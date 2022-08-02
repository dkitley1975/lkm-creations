[![David's GitHub Banner](/readme/assets/logo/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations <!-- omit in toc -->

[![LKM Creations](/readme/assets/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
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
- [Marketing](#marketing)
- [Design](#design)
  - [Database](#database)
  - [Wireframes](#wireframes)
  - [Fonts](#fonts)
  - [Colors](#colors)
    - [*Main Colour Pallet*](#main-colour-pallet)
    - [**Shades of the Brand Colours**](#shades-of-the-brand-colours)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Libraries, Frameworks and Tools](#libraries-frameworks-and-tools)
- [CRUD Functionality](#crud-functionality)
  - [General User](#general-user)
  - [General - Registered User](#general---registered-user)
  - [Staff - Registered User](#staff---registered-user)
  - [SEO](#seo)
- [Site Features](#site-features)
- [Site Testing](#site-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
    - [AWS](#aws)
    - [GitHub](#github)
      - [Forking](#forking)
    - [Set up your Workspace](#set-up-your-workspace)
    - [Deployment via Heroku](#deployment-via-heroku)
    - [Stripe](#stripe)
    - [Email setup](#email-setup)
- [Credits](#credits)
- [My Thoughts](#my-thoughts)

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

![Project Board - Issues listed by bug and epics](/readme/assets/projectboard/LKM-CREATIONS-project-boards-issues-list.jpg)

### [Github Project Board](https://github.com/users/dkitley1975/projects/12/views/3?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Labels)

![Project Board](/readme/assets/projectboard/LKM-CREATIONS-Project-board.jpg)

[Table of Contents  ⇧](#table-of-contents)

***
# Marketing

[LKM Creations Facebook page](https://www.facebook.com/lkmcreations)

Along with Mailchimp for newsletter signup, we are using Facebook for product promotions.
The idea is to run a facebook post for each of the products in store.
Give each one a name and a profile description.
Keeping it like an adopt a pet idea.
The page has an image of one of the creations in the cover page and one as the profile image.
There are links to the main website, with details about the store, opening hours and contact details.

As a user:
  - They can see the posts and see the likes and comments.
  - They can share and like the posts,
  - and they can comment on the posts.

With each post to contain the link to the site, it is hoped that the post will be shared on facebook, and hopefully create interest in the products.
As some of the proceeds of each sale of these items are going to the local Preschool charity, the aim is in the future to target facebook adverts towards people in the area.
Targeting people who have liked the Preschool charity page and the nursery and infants sschools, as these are people who are most likely to be interested in the Preschool Charity and the products may be of interest as gifts for their children.

![image](/readme/assets/site-screenshots/facebook_com_lkmcreations.png)

[Table of Contents  ⇧](#table-of-contents)

# Design

## Database

Image showing the database Scheme for LKM-CREATIONS
![LKM-Creations Database Scheme](/readme/assets/schema/LKM-CREATIONS-database-schema.jpg)

## Wireframes

| Wireframe Description | Link |
| -- | -- |
| Desktop Wireframe of the Homepage | [link](/readme/assets/wireframes/wireframe-desktop-home.png "link") |
| Desktop Wireframe of the Newsletter Signup Modal | [link](/readme/assets/wireframes/wireframe-desktop-newsletter.png "link") |
| Desktop Wireframe of the Products View | [link](/readme/assets/wireframes/wireframe-desktop-products.png "link") |
| Desktop Wireframe of the Product Details | [link](/readme/assets/wireframes/wireframe-desktop-product-details.png "link") |
| Mobile Wireframe of the Homepage | [link](/readme/assets/wireframes/wireframe-mobile-home.png "link") |
| Mobile Wireframe of the Contact-Us Page | [link](/readme/assets/wireframes/wireframe-mobile-contact-us.png "link") |
| Mobile Wireframe of the Newsletter Signup Modal | [link](/readme/assets/wireframes/wireframe-mobile-newsletter.png "link") |
| Mobile Wireframe of the Products View | [link](/readme/assets/wireframes/wireframe-mobile-products.png "link") |
| Mobile Wireframe of the Product Details | [link](/readme/assets/wireframes/wireframe-mobile-product-details.png "link") |

I planed a limited number of wireframes for the project, Partly because I did not have the time to finish all of them, but also after designing the initial pages I knew what I wanted to see from the each page. If I was having to submit a client I would of spent more time initially laying out the frames for signoff before beginning to design the pages. As I was designing the pages I was also planning on using the basic set of wireframes to help me understand the design and how to implement it into the project. But as I only had to answer to myself I wasn't constrained to the wireframes I had planned and felt free to amend the layout and colour scheme as I needed.

***

## Fonts

The default Sans-Serif is used as the main font. I was unnecessary to change the default font type as this is an easy font to read and displays well throughout the site.

The Logo is pre-designed and uses Caveat from Google
![image](/readme/assets/logo/LKM-CREATIONS-logo.png)
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

# Technologies used

## Languages

| Languages | Link |
|--|--|
|HTML|[HTML](https://en.wikipedia.org/wiki/HTML5 "HTML")
|CSS|[CSS](https://en.wikipedia.org/wiki/CSS "CSS")
|JavaScript|[JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS")
|jQuery|[jQuery](https://jquery.com/ "jQuery")
|Python|[Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")
|Markdown|[Markdown](https://en.wikipedia.org/wiki/Markdown)

## Libraries, Frameworks and Tools

| Libraries / Frameworks / Tools| Description | Link |
|--|--|--|
|Django|Database Driven Framework| [django](https://en.wikipedia.org/wiki/Django_(web_framework) "django")|
|gunicorn|HTTP Interface Server|[gunicorn](https://en.wikipedia.org/wiki/Gunicorn "gunicorn")|
|psycopg2| Database adaptor | [psycopg2](https://wiki.postgresql.org/wiki/Psycopg "psycogg2")
|cloudinary |Image management|[cloudinary](https://cloudinary.com/ "cloudinary")|
|django auth|User authentication|[auth](https://readme.djangoproject.com/en/3.2/topics/auth/ "auth")|
| Postgres | Database| [Postgres sql](https://www.postgresql.org/)
| django crispy forms | Styling forms | [crispy-forms](https://django-crispy-forms.readthereadme.io/en/latest/ "crispy-forms")|
|Site mockup| Mockup of site on different screen sizes|[Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php "Mockup Generator")
|HTML Validation| Validating HTML|[w3.org](https://validator.w3.org/ "W3C")
|CSS Validation| Validating CSS|[w3.org](https://jigsaw.w3.org/css-validator/ "W3C")
|JS Validation|Validating JS & jQuery|[jshint](https://jshint.com/ "JSHint")
|PEP8|Validating python|[PEP8](http://pep8online.com/ "PEP8")
| LOADING.IO | Spin Loader | [loading.io](https://loading.io/ "loading.io")
| Unsplash | Images |[Unsplash](https://unsplash.com/ "Unsplash")
| GitPod | Development environment |[Gitpod](https://www.gitpod.io/ "Gitpod")
| Balsamic | Wireframes |[Balsamic](https://balsamiq.com/wireframes/ "Balsamic")
| Bootstrap | Responsive design |[Bootstrap](https://getbootstrap.com "Bootstrap")
| Font Awesome | Icons |[Font Awesome library](https://fontawesome.com/ "Font Awesome")
| Django Secret Key Generator | Secret Key |[Secret Key Generator](https://django-secret-key-generator.netlify.app/ "django-secret-key-generator")
| Colours|Colour pallet| [coolors](https://coolors.co/ "coolors")|
| Google Fonts| Fonts |[Google Fonts](https://fonts.google.com/ "Fonts")|
| WebAIM| Colour contrast checks |[WebAIM](https://webaim.org/resources/contrastchecker/ "WebAIM")|
|Pillow| Image processing tool | [Pillow](https://pillow.readthereadme.io/en/stable/ "Pillow")
|termly.io|Privacy Policy Generator| [Generate Privacy Policy](https://www.termly.io/)
|Stripe| online payments| [Stripe](https://stripe.com/en-gb "Stripe")
|favicon.io| Create the favicon| [favicon.io](https://favicon.io/ "favicon.io")
|AWS| Storage of the Static Files| [AWS](https://aws.amazon.com/ "aws.amazon.com")

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

I have access to the Admin panel where I can Create, Read, Update and Delete all the information.
Creating, Editing, Updating and Deleting the *Products*, *Categories*, *Reviews*, *Users*, *Addresses*, *Orders*, *Payments*

## SEO

The sites key words are added in the *Meta Tags* section of the *Head* section of the *HTML* document. These are taken from the Siteadmin *SEO* store_description.
Pages such as the product pages use

``Purchase as a gift our {{ product.name|title}} -
{{ product.description|title|striptags|safe|truncatechars:100 }}``
for a dynamic description.

Keywords were researched and the following were used:
"Handmade, Gifts, Amigurumi Stuffed Animals, Amigurumi Toys, Amigurumi Gifts, Dolls, Stuffed Animals, Toys, Crochet Dolls, Crochet Toys, Crochet Gifts"
These are entered in to the siteadmin-siteinfo *SEO* store_keywords. and are called in to the more static pages.
There are also product Keywords which are dynamic and are called in to the product pages.

[Table of Contents  ⇧](#table-of-contents)
***

# Site Features

The site features documentation can be found here, this includes the details regarding the pages and the features of the site with supporting images.

[Site Features Documentation](/readme/README-SITE-FEATURES.md)

[Table of Contents  ⇧](#table-of-contents)
***

# Site Testing

The site testing documentation can be found here, this includes the details regarding the testing of the site.

[Testing Documentation](readme/README-SITE-TESTING.md)

[Table of Contents  ⇧](#table-of-contents)
***

# Bugs

This area lists the bugs which left me frustrated for a long time of just haven't as yet been solved..

[Bugs Documentation](readme/README-BUGS.md)

[Table of Contents  ⇧](#table-of-contents)
***

# Deployment

This project was created using GitHub and the code was written VSCode.
Branches were created to work on sections of the site.  This project is also deployed to Heroku

heroku login -i

Email: **enter_heroku_account_email**
Password: **enter_heroku_account_password**

heroku git:remote -a __your *heroku_app_name*_

git push heroku main

The live link to the application can be found [here](https://lkm-creations.herokuapp.com// "Link")

## Local Deployment

As Visual Studio Code was the IDE that was used to create the project, the following local deployment steps are specific to my enviroment.

### AWS

- Visit AWS by following this [link](https://aws.amazon.com/ "Link")
- Click on the *Create an AWS Account* button
- When the account is created, you will need to setup a S3 Bucket.
 [amazon-s3-cheat-sheet](https://www.zuar.com/blog/amazon-s3-cheat-sheet// "How to create an AWS S3 Bucket") You will need the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID

### GitHub

- Visit Github by following this [link](https://github.com/ "Link")
- Create an account or log in

#### Forking

- Navigate to the repository by following this [link](https://github.com/dkitley1975/lkm-creations "Link")
- Click on the *Fork* button in the top right of the screen

### Set up your Workspace

When you have your version of the original repository,

- In the terminal run

``
pip3 install -r requirements.txt
``

- In the root directory create a file called **.env** and add the two following blocks of content, the content of these, must match the Config Vars in the Heroku deployment section

This First Section is used for my the local deployment
I have issues using psycopg2 when using the live server,
So I am unable to use the live database from my local machine. So setting up a local database is required.
When Debug is set to False I can choose to use the remote static files rather than the local static files, by using the USE_AWS.
LOCAL_DB and USE_AWS are not required to be copied to Heroku Vars

``DEBUG=True
LOCAL_DB=True
USE_AWS=False``

``SECRET_KEY=YourSecretKey
DATABASE_URL=YourPostgreslink
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=YourPassword
EMAIL_PORT=587
EMAIL_HOST_USER=yourname@gmail.com
SITE_EMAIL=SitesEmailAddress
ALLOWED_HOSTS=127.0.0.1, localhost
AWS_ACCESS_KEY_ID=YourKey
AWS_SECRET_ACCESS_KEY=YourKey
STRIPE_PUBLIC_KEY=pk_test_YourKey
STRIPE_SECRET_KEY=sk_test_YourKey
STRIPE_WH_SECRET=whsec_YourKey
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_FROM_ADDRESS=DefaultEmailAddress``

- Add the .env file to the .gitignore file to ensure that its contents are not made public

- Migrate the database models with the following command in the terminal

``
python3 manage.py migrate
``

- Create a superuser and set up the credentials with the following command

``
python3 manage.py createsuperuser
``

- Run the application locally with the command

``
python3 manage.py runserver
``

- To access the admin page using the superuser details just created, add /admin to the end of the URL.

### Deployment via Heroku

- Visit [heroku.com](https://www.heroku.com/home "Heroku")
- Create a new account or sign in
- From the dashboard, select **New** and then **Create new app**
- Enter an individual app name into the text box, select a region from the dropdown and then press **Create app**
- A Heroku app has now been created and the **Deploy** tab is opened.
- Open the *Resources* tab and in the search bar for *Add-ons* type *Postgres*
- Select *Heroku Postgres*, on the popup, ensure the dropdown is set to *Hobby Dev - Free* and then *Submit Order Form*
- Open the *Settings* tab and then click on the *Reveal Config Vars* button and the database_url should be populated.
- Fill out the rest of the config vars with the content of the table below by filling out the *Key* and *Value* and clicking on *Add* for each entry

| Key | Value |
| --- | --- |
| ALLOWED_HOSTS | The domain name of the site |
| SECRET_KEY | The secret key for the site [Create one here](https://miniwebtool.com/django-secret-key-generator/") |
| AWS_ACCESS_KEY_ID | From the AWS section |
| AWS_SECRET_ACCESS_KEY | From the AWS section |
| DATABASE_URL | This should already be filled in, copy the setting back to the local .env file |
| DEFAULT_RECIPIENT_ADDRESS | DEFAULT_RECIPIENT_ADDRESS |
| EMAIL_FROM_ADDRESS | DEFAULT_FROM_ADDRESS (ie:no-reply) |
| SITE_EMAIL | DEFAULT_SITE_ADDRESS |
| EMAIL_HOST | smtp.gmail.com |
| EMAIL_HOST_PASSWORD | YourPassword |
| EMAIL_HOST_USER | EMAIL_HOST_USER_EMAIL_ADDRESS |
| EMAIL_PORT | 587 |
| STRIPE_PUBLIC_KEY | pk_test_YourKey |
| STRIPE_SECRET_KEY | sk_test_YourKey |
| STRIPE_WH_SECRET | whsec_YourKey |

- In the buildpacks section of the settings tab, click on **Add Buildpack**, select **python** and then save changes
- Open the **Deploy** tab
- In the deployment method section, select **GitHub** and confirm the connection.
- Enter the repo name into the text box and click **Search**. When the correct repo appears below, click **Connect**
- Return to the Gitpod workspace and in the root directory create a file called *Procfile*
- In the *Procfile* enter the following line including your project name

``python
web: gunicorn YOUR_PROJECT_NAME.wsgi``

- Add and commit to GitHub

```Python
git add .
git commit -m "commit message goes here"
git push
```


- Return to Heroku
- To complete the process click on the **Deploy Brach** button in the Manual deploy section, this will take a few seconds to complete while Heroku builds the app
- A message will appear informing you that the app was successfully deployed and a **View** button will bring you to the live site

### Stripe

- Visit Stripe by following this [link](https://dashboard.stripe.com/register "Stirpe")
- And register for an account, for this project as it is only set up for test payments the *activate payments* section can be skipped.
- From the dashboard, click on the *Developers* and then on the lefthand side, *Webhooks*.
- Click on the *Add endpoint button* and paste in the Heroku URL with `/checkout/wh/` included on the end, for example, this project would be `https://lkm-creations.herokuapp.com/checkout/wh/`
- Add an optional description if required
- Click the *Select events* button and mark the checkbox for *Select all events*, then click *
Add events*.
- Scroll to the very bottom of the page and then click *Add endpoint*
- From the webhook page under the URL, reveal the Signing secret, this will need to be added to Heroku config vars as STRIPE_WH_SECRET.
- Still in the developer's section of Stripe, click on the *API keys* link on the left, the *Publishable key* (STRIPE_PUBLIC_KEY) and *Secret key* (STRIPE_SECRET_KEY) will also be needed to be added to Heroku config vars.

### Email setup

This project is using Gmail as its email provider. Other providers can be used but the setup will differ slightly.

- Create a Gmail account, or log in if you already have an account
- At the top right waffle menu select *Account*, then on the left of the screen select *Security*
- In the *Signing into Google* section turn on 2-step verification and then click *Get started*
- Enter your password and select a verification method
- Go back to the security page and under the 2-step verification there is a new option called *App passwords*, click it.
- In the select app dropdown, select *Mail*
- In the select device dropdown, select *Other* and type in *Django*
- The app password will be shown, copy this and add it to the Heroku config vars and the local .env as EMAIL_HOST_PASS.

[Table of Contents  ⇧](#table-of-contents)
***

# Credits

- [Code Institute's Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/) for the initial walkthrough and for the inspiration for this project.
- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") for advice and direction.
- [Code Institute's Student Support](https://learn.codeinstitute.net/ "codeinstitute.net") for help with why my stripe webhooks were failing and why my emails stopped working, How to debug the issue and find the error (blank line in the email subject text file).
- My Wife for her patience, understanding and occupying the children.


[Table of Contents  ⇧](#table-of-contents)
***

# My Thoughts

This is my final project and the completion of the Code Insitute's Diploma in Full Stack Software Development.

I happy with the way the site works and the way it looks.
I'm happy with the progress I have made from my initial project to this one.
I'm deeply aware of the knowledge gaps, but I'm happy with the knowledge I have gained, and I know whats possible and more importantly, what I have to google to help me progress and how to implement this knowledge in to the project.
There are a few enhancements I would like to of added to the site, such as having a single product but having multiple colours and sizes. But as this site currently doesn't require this it was felt unimportant to add it as a feature.

Overall, a very enjoyable project!

[Table of Contents  ⇧](#table-of-contents)
***
