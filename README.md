[![David's GitHub Banner](/documents/assets/logos/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

# LKM-Creations <!-- omit in toc -->

[![Leannes Learners](/documents/assets/screenshots/responsive-showcase-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This is the documentation regarding the creation of an e-commerce website for LKM-Creations.
This is my 5th and final Portfolio Project for the Code Institute's Diploma in Full Stack Development.
The projects purpose:
To build a Full-Stack site based on business logic used to control a centrally-owned dataset. Including an authentication mechanism and providing role-based access to the site's data or other activities based on the dataset.

# Table Of Contents

- [Table Of Contents](#table-of-contents)
  - [UX (User Experience)](#ux-user-experience)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
  - [User Persona Summary !User Persona Summary](#user-persona-summary-)
- [Project Boards](#project-boards)
- [Design](#design)
  - [Database](#database)
  - [Mobile Wireframes](#mobile-wireframes)
  - [Fonts](#fonts)
  - [Colors](#colors)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Frameworks and Tools](#frameworks-and-tools)
- [CRUD](#crud)
  - [General User](#general-user)
  - [General - Registered User](#general---registered-user)
  - [Pupil - Registered User (Pupil)](#pupil---registered-user-pupil)
  - [Staff - Registered User (Pupil)](#staff---registered-user-pupil)
    - [I able to Create, Update and Delete](#i-able-to-create-update-and-delete)
- [Features](#features)
  - [Navigation bar](#navigation-bar)
  - [Small Screen Screenshots](#small-screen-screenshots)
  - [Large Screen Screenshots](#large-screen-screenshots)
    - [Home](#home)
    - [About Us](#about-us)
    - [Pass Plus](#pass-plus)
    - [Prices](#prices)
    - [Contact Us](#contact-us)
      - [Contact Form](#contact-form)
    - [Local Traffic Report](#local-traffic-report)
    - [Terms and Conditions](#terms-and-conditions)
    - [Login](#login)
    - [Registration](#registration)
    - [Blog/Posts Section](#blogposts-section)
      - [Blog](#blog)
      - [Post](#post)
      - [Post Logged in as Staff](#post-logged-in-as-staff)
        - [Post Delete](#post-delete)
        - [Post Edit](#post-edit)
      - [Commenting](#commenting)
  - [Password reset](#password-reset)
- [Admin](#admin)
- [Error Pages](#error-pages)
  - [Error 400](#error-400)
  - [Error 403](#error-403)
  - [Error 404](#error-404)
  - [Error 500](#error-500)
- [Deployment](#deployment)
- [Cloning](#cloning)
- [Credits](#credits)

[Testing Documentation](/README_TESTING.md)

## UX (User Experience)

### User Stories

**As a User**

- [x] I want to know where Leanne's Learners operate
- [x] I want to see the service's Leanne's Learners offer.
- [x] I want to be able to see the prices.
- [x] I want to know about the company.
- [x] I want to be able to contact the company.
- [x] I want to be able engage with the site and with others.
- [x] I want the ability to comment on a post.
- [x] I want the ability to remove my comment, if I later decide.
- [x] I want to be able to like both a blog posts content and comments
- [ ] I want to book my lesson
- [ ] I want to see my booked lessons
- [ ] I want to cancel my lesson

### Site Owner Goals

*As a Site User*

- [x] I want to show where Leanne's Learners operates.
- [x] I want to show our prices.
- [x] I want to let people see the services we offer
- [x] I want to let people easily contact us either by email or phone.

#### I want to be able to engage with site users. <!-- omit in toc -->

- [x] I want to be able to have a blog section.
  - [x] I want to be able to allow selected people to login to the site and easily add, delete and amend Posts.
  - [x] I want to be able to allow registered users to be able to post comments on the posts.
  - [x] I want to be able to allow users to reply to comments.
  - [x] I want to be able to allow Leanne's Learners Staff to delete any comments posted.
  - [x] I want to be able to allow Leanne's Learners Staff to create/delete/edit Posts.
  - [x] I want the originator of a comment to be able to delete their comments and it's child comments.

#### I want to be able to update information, without the need to ask the site developer.<!-- omit in toc -->

- [x] Our Services and Prices

- Our Contact Details
  - [x] Contact Number
  - [x] Email Address
  - [x] Social Media Accounts
    - [x] Facebook
    - [x] Twitter
    - [x] Whatsapp
- [x] Add New Instructors and update information for current Instructors
- [x] Update our operating hours

#### Items discussed and wanted for the next interation of the site. <!-- omit in toc -->

- [ ] I want to make it easy for pupils to book lessons.
- [ ] I want to get an email when a pupil requests to make or cancel a lesson.
- [ ] I want to be able to confirm a pupils requests to make or cancel a lesson.
- [ ] I want to be able to cancel pupils lessons.
- [x] I want to be able to place registered users in to a Pupil Group.
- [x] I want to be able to get email from site users through a contact form

## User Persona Summary ![User Persona Summary](/documents/assets/UserPersonaSummary.jpg)

*The item's  left in this section of the document and marked as incomplete are left intentionally, as these are items discussed previously with the client. Although I could of removed these from the documentation and make it appear the site is completed, I believe it is important to leave these items showing as incomplete. Because the site isn't fully completed and is only through its first iteration, with plans for further development.*

[Table of Contents](#table-of-contents)

***

# Project Boards

I Used Github's Project board to plan the project and Github Issue's for User Stories and Tasks

*Project Board listed by Status*
![Project Board listed by Status](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_List_By_Status.png)

*Project Board listed by Milestone*
![Project Board listed by Milestone](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_List_By_Milestones.png)

*First Milestone with Tasks added*
![Milestone with tasks added](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_Milestone_Description_And_Adding_Tasks.png)

*User Story with Tasks added*
![User Story with tasks added](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_User_Story_and_Added_Tasks.png)

*Project Board Kanban, with Automation*
![Project Board Kanban, with Automation](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board.png)

*Project Board in progress*
![Project Board Kanban, with Automation](/documents/assets/screenshots/GitHub_Project_Board_Screen_Shots/Leannes_Learners_Project_Board_finish.png)

[Table of Contents](#table-of-contents)
***

# Design

## Database

Image showing the database for Leanne's Learners - main site area
![Leannes Learners](/documents/assets/database/leannes_learners_data.png)

Image showing the database for Leanne's Learners - Blog Post and User site area
![Blog and Users](/documents/assets/database/blog_and_users.png)

## Mobile Wireframes

![MOBILE](/documents/assets/Wireframes/wireframe-mobile.png)

## Fonts

The default Sans-Serif is used as the main font. I was unnecessary to change the default font type as this is an easy font to read and displays well throughout the site.

For the headings I have used Pushster from Google
![image](/documents/assets/screenshots/font/our_latest_blog_post.png)
![image](/documents/assets/screenshots/font/our_latest_testimonials.png)

## Colors

These are the main images used throughout the site.
![Main Colour Pallet](/documents/assets/colour-pallets/main-colour-palette.png)

- clr-brand-primary: rgb(116, 36, 29) - used for the navigation bar and footer.
- clr-brand-secondary: rgba(255, 239, 148, 0.742)  - used in the navigation bar.
- clr-brand-tertiary: rgb(156, 207, 153)  - used as the hover state - to indicate GO.
- clr-brand-tertiary-darker: rgb(68, 126, 65)  Used for the Like button.
- clr-brand-quaternary: rgb(208, 0, 0)  - used as the hover state on some buttons - to indicate STOP/DANGER and the Dislike button.

These light greys are used through out the site to highlite areas and as shadow areas.

- clr-background-light: rgb(238, 238, 238)
- clr-background-grey: rgb(153, 158, 164)
- clr-border-grey: rgb(222, 226, 230)
- clr-box-shadow: rgb(153, 153, 153)
- clr-link-dark: rgb(68, 82, 97)
- clr-quotation-mark: rgb(51, 51, 51)

[Table of Contents](#table-of-contents)
***

# Technologies

## Languages

- HTML
- CSS
- Python
- Django

## Frameworks and Tools

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

[Table of Contents](#table-of-contents)
***

# CRUD

## General User

As a **General User** of the site, I am able to browse and read the website, the pages I read have data pulled from tables in a remote database.

## General - Registered User

As a **General Registered User** browser of the site, I am able do the same as the **General User**. In addition I am able to create *Comments* on Blog Posts, I can also *Like* and *Dislike* Posts and *Comments*. I can also *Delete* a *Comment* I made previously.
I also have access to a new menu item which allows me to *Update* my *Registered Details* and *Update* my *User Profile*.

## Pupil - Registered User (Pupil)

As a **Registered User** who is marked a being a **Pupil**, I can do all that the **General Registered User** can do, I have access to a *Member's Area* menu item which allows me to view the Terms and Conditions I have entered into.

## Staff - Registered User (Pupil)

As a Staff Registered User, I can do all that the **Pupil Registered Users** can do, I have access to a *Staff Area* menu which gives me access to the Admin Area and to a link to *create* a new Blog Post.
When viewing a Post I also a link to *Update* the post, and *Delete* a Post.
I can also *Delete* all Comments.
I have to the Admin panel where I can Create, Read, Update and Delete all the information.

### I able to Create, Update and Delete

- About Us, I can Create, Read, Update and Delete page information.
- Carousel on the Home Page, I can Create, Read, Update and Delete Slides.
- Company Contact and Social Medial Information, I can Create, Read, Update and Delete.
- Driving Instructors, I can Create, Read, Update and Delete instructors information.
- Pass Plus Page, I can Create, Read, Update and Delete page information.
- Service Description,  I can Create, Read, Update and Delete the Services Provided and the prices by leannes Learners.
- Teaching Hours, I can Create, Read, Update and Delete the teaching hours information.
- Terms and Contitions, I can Create, Read, Update and Delete Terms and Conditions information
- Testimonials, I can Create, Read, Update and Delete Testimonials
- Categories, I can Create, Read, Update and Delete Categories.
- Comments, I can Create, Read, Update and Delete Comments.
- Posts, I can Create, Read, Update and Delete Posts.
- User Profiles, I can Create, Read, Update and Delete Users and their profiles.

# Features

The website has the following features:

## Navigation bar

These are the navigation bars for site users currently not logged in, just displaying the register and login options:
Desktop
![image](/documents/assets/screenshots/navbar/navbar_desktop.png)
Small Screen
![image](/documents/assets/screenshots/navbar/navbar_small_screen.png)

These are the navigation bars for site members logged in, displaying the menu bar selection for members with profile and detail edit optons. and now with logout replacing login and register options:

Desktop
![image](/documents/assets/screenshots/navbar/navbar_member_desktop.png)

Small Screen
![image](/documents/assets/screenshots/navbar/navbar_member_small_screen.png)

These are the navigation bars for site members who are pupils and logged in, displaying the menu bar selection for members with profile edit, details edit and the Terms and Conditions optons. This is to be expanded on when the lesson booking functionality is added on the next iteration:

Desktop
![image](/documents/assets/screenshots/navbar/navbar_pupil_desktop.png)
Small Screen
![image](/documents/assets/screenshots/navbar/navbar_pupil_small_screen.png)

These are the navigation bars for site Staff logged in, displaying the menu bar selection for staff with Login into admin and create a blog post optons.:

Desktop
![image](/documents/assets/screenshots/navbar/navbar_staff_desktop.png)

Small Screen
![image](/documents/assets/screenshots/navbar/navbar_staff_small_screen.png)

## Small Screen Screenshots

Small Screen page designs
![image](/documents/assets/screenshots/main_pages/leannes_learners_small_screen.png)

## Large Screen Screenshots

The rest of the screenshots used for the pages will use the Desktop View for clarity

### Home

![image](/documents/assets/screenshots/main_pages/home_desktop.png)

### About Us

![image](/documents/assets/screenshots/main_pages/about_us_desktop.png)

### Pass Plus

![image](/documents/assets/screenshots/main_pages/pass_plus_desktop.png)

### Prices

![image](/documents/assets/screenshots/main_pages/prices_desktop.png)

### Contact Us

![image](/documents/assets/screenshots/main_pages/contact_us_desktop.png)

#### Contact Form

This is the contact form filled in
![image](/documents/assets/screenshots/contactform/contact-form.png)
After submission:
the user is redirected to this page
![image](/documents/assets/screenshots/contactform/contact-success.png)
and receives an email
![image](/documents/assets/screenshots/contactform/contact-result-email-for-originator.png)
the owner reveives this email
![image](/documents/assets/screenshots/contactform/contact-result-email-for-staff.png)
During debug:
the contact test results are shown in the console:
![image](/documents/assets/screenshots/contactform/contact-test-result-email-for-staff.png)
![image](/documents/assets/screenshots/contactform/contact-test-result-email-for-originator.png)

### Local Traffic Report

![image](/documents/assets/screenshots/main_pages/local_traffic_desktop.png)

### Terms and Conditions

Available to Users within the Pupil Group only
![image](/documents/assets/screenshots/main_pages/terms_and_conditions_desktop.png)

### Login

![image](/documents/assets/screenshots/main_pages/login_desktop.png)

### Registration

![image](/documents/assets/screenshots/main_pages/registration_desktop.png)

### Blog/Posts Section

#### Blog

![image](/documents/assets/screenshots/main_pages/blog_posts_desktop.png)

#### Post

![image](/documents/assets/screenshots/main_pages/post_desktop.png)

#### Post Logged in as Staff

![image](/documents/assets/screenshots/main_pages/post_desktop_staff.png)
Logged in as a Staff Member adds an edit post and delete post icons next to Author and Date.

##### Post Delete

![image](/documents/assets/screenshots/main_pages/post_delete_desktop.png)
Delete a Blog Post shows a preview of the post that is about to be deleted and shows warning that this will also delete the comments etc.

##### Post Edit

![image](/documents/assets/screenshots/main_pages/post_edit_desktop.png)

#### Commenting

Comment Modal
![image](/documents/assets/screenshots/main_pages/comment_to_the_post.png)
Comment Modal for replying to a comment - As indicated against oliphant_watcher's previous comment there is a delete icon to remove her comment, this only appears to the originator of the comment (in this case oliphant_watcher) or if the user is a authenticated staff member.
![image](/documents/assets/screenshots/main_pages/comment_to_the_comment.png)
Showing the Comments, with likes and dislikes added.
This also shows a delete comment icon which only shows when the user is the originator of the comment (in this case oliphant_watcher) or if the user is a authenticated staff member.
![image](/documents/assets/screenshots/main_pages/comments.png)

## Password reset

When a user forgets their password, they are able to reset their password, on the login screen there is a 'forgotton your password link.
![image](documents/assets/screenshots/password_reset/0-login-screen-forgotten)
This opens the Forgot Password page which asks for the users email address.
![image](documents/assets/screenshots/password_reset/1-forgot-password.png)

A confirmation page informs the user that an email has been sent to the given email address.
![image](documents/assets/screenshots/password_reset/2-forgot-password-email-sent-confirmation.png)

An email is sent to the users email address with a link to reset their password.
![image](documents/assets/screenshots/password_reset/3-forgot-password-email.png)

The link goes  opens up the Change password page, allowing the user to change their password.
![image](documents/assets/screenshots/password_reset/4-forgot-password-revise-password.png)

If the password do not match an error is displayed.
![image](documents/assets/screenshots/password_reset/password-not-match.png)

If the password do match a confirmation page is displayed with a login link.
![image](documents/assets/screenshots/password_reset/5-forgot-password-completed.png)

[Table of Contents](#table-of-contents)
***

# Admin

I have used brand colors for the Admin Section.

![image](/documents/assets/screenshots/main_pages/admin_not_authorised_desktop.png)
![image](/documents/assets/screenshots/main_pages/admin_desktop.png)

[Table of Contents](#table-of-contents)
***

# Error Pages

I have created the following custom error pages for the site.

## Error 400

![image](/documents/assets/screenshots/error_pages/400_error.png)

## Error 403

![image](/documents/assets/screenshots/error_pages/403_error.png)

## Error 404

![image](/documents/assets/screenshots/error_pages/404_error.png)

## Error 500

![image](/documents/assets/screenshots/error_pages/500_error.png)

  [Table of Contents](#table-of-contents)
  ***

# Deployment

1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser

The program is set to be deployed automatically after each push from gitpod.

I also set up a Postgres database with Heroku.

1. Click on Resources in your Heroku app.
2. In the add-ons field search for Heroku Postgres and press submit.

# Cloning

How to clone this repository.

- On GitHub go to the main page of the Repository.
- Above the list of files click the code button with the drop-down arrow.
- To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
- Open the Git Bash terminal.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier from step 3.
- Press Enter to create your local clone.

# Credits

[Email sending: Using Forms and Class based views instead of Function based views](https://www.sitepoint.com/django-send-email/)

Social Sharing Links [Crunchify](https://crunchify.com/list-of-all-social-sharing-urls-for-handy-reference-social-media-sharing-buttons-without-javascript/)

[Social Sharing Tutorial](https://www.youtube.com/watch?v=OfLvQ8KtW2g)
