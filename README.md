# V_jewelry_G
This is a project that is a part of Diploma in Full Stack Software Development (E-commerce applications)

V_jewelry_G is an online B2C(Business-to-Consumer)online jewelry store, offering wide range of beautiful jewelry pieces that add elegance and sophistication to every occasion. Our customer centrich approach ensures personalizsed experiences, helping shopers find the perfect piece that complements their unique style and personality. Our consumers has the ability to register  and create a profile, chose from different categories of jewelry, modify their basket content, proceed to checkout in a safely way (allauth authentication) and finish the payment using Stripe, receive a confirmation order/email of purchased items, contact us with any enquires and leave a comment on a product they liked. Note that this website is for educational purposes only and do not enter any personal credit/debit card details when using the site.

The live link can be found here - [Stripe card testing](https://stripe.com/docs/testing#cards)



The live link can be found here - [V_jewelry_G](https://projectportfolio5-a694568fc098.herokuapp.com/)

# Table of Content
* [User Experience (UX)](#user-experience-ux)
* [Design](#design)
* [Features](#features)
* [Technologies](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)

# User Experience (UX)

The costumers of V_jewelry_G would be someone who is interested in Jewelry, Adults who want to buy something luxurious for themselver or as a gift to someone special.

## Project goals 

The primary goal for this project is to create a ecommerce site where costumers can register and create a profile, navigate the site easily, check different products and categories, adding items to basket, modifying (delete, upgrade), proceeding to a secure checkout, filling personal details and making a purchase. After the purchase, receive an confirmation order and email and are able to leave a comment on the product.

## Agile methodoligy

Github projects were used to manage the development process using agile approach, 32 issues were created and implemented using Kanban board.  -> [User stories](https://github.com/users/Vaidots/projects/5/views/1)

# Design

The site has a very simple and minimalistic black and white dominant colour theme. 

## Colour scheme

![](/media/Color-palet.JPG)



## Fonts

font 'Lato' was used throughout the body.

# Features

## Header

![](/media/Navigation%20bar.JPG)

### Navigation bar

* The navigation bar is visible at the top in every page, with links to other pages

### Logo

* This logo is positioned in top left in the vagiation bar, it is linked with home page when pressed, for users to navigate more easily.

### Search Bar

* The search bar is placed above the nav bar
* On smaller screens, this becomes a search icon which drops down the full bar when clicked
* Searched words will match with any text in products title,description and display the results on the products page.

### User Icon

* The User icon navigation link is a drop down menu which includes the Sign up and Log in links.
* After user Signs up the option will change to Log out and My Profile
* If a superuser logs in the drop down menu will include Product Management on top.

### Bag Icon

* When a product is added to the bag it will display a success message and the item and the bag icon will show the total amount 
* Clicking to shopping bag will navigate to shopping bag page which displays the product summary.

![](/media/BagAddItemsg.JPG)

## Footer

![](/media/Footer.JPG)

* The footer appears at the bottom of every page
* Footer section includes links to Facebook, Instagram and Github
* Clicking on icons wil open a new tab with the respective website.
* Newsletter sign up section was made by MailChimp where the user can input their email address to signup to the monthly newseletter. Note Addblock must be turned off to newsletter to appear.
* Copyright message was made for study purpose only

## Home Page

![](/media/CallToAction.JPG)

## Call To Action

* The home page includes a call to action section which encourages the user to shop now.

## User Account pages


## Sign up

![](/media/SignUp.JPG)

## Sign in

![](/media/LogIn.JPG)

## Sign Out

![](/media/Sign_out.JPG)

* Django allauth was installed and used to create all the forms
* Succes messages informs the user if when they logged in/out
* To log in user needs to verify their email address, by clicking on the link the site sent

## Products

![](/media/ProductsPage.JPG)

* Each product card shows an image of the product, title, price, category and rating.
* When users press on a product it will navigate to shopping bag
* Only superusers can edit or delete products
![](/media/EditProduct.JPG)
* superuser can delte the product, note that when pressed delete it will delete straight away.
* Only superusers cann add products
![](/media/Add_ProductManagement.JPG)

# Comment

![](/media/ProductDetail.JPG)

* Users can add a comment by filling the forms and submiting.
* Admin needs to approve the message in order for it to appear on the product.

## Shopping Bag

![](/media/ShoppingBag.JPG)

* Customers can easily review the items,total price in their shopping bag and make changes before proceeding to checkout.
* When users press on a image it opens a full new window with a full view of the product.
* When users are happy to procced Secure checkout button will navigate to secure checkout page.


## Checkout

![](/media/CheckOut.JPG)

* The products details are shown next to the form.
* The checkout process enables customers to complete their jewelry purchase securely.
* The checkout process includes a user-friendly form for entering contact and delivery details.
* Secure payment is created with Stripe payment gateway, ensuring secure and smooth payment transactions.
* For registered users, that updated their profile, the checkout form is conveniently pre-filled with their information.
* After completing the order a success message will pop with order number and will sent an email with order confirmation.

## Order Confirmation

![](/media/OrderConfirmation.JPG)

* During checkout, the orderform validates and esnures the accuracy of customer-provided information.

## Profile

* After purchase, the profile form is prefilled with the information provided in checkout.
* Order history is shown with order number, date, items and how much you spent.

![](/media/MyProfile.JPG)

## Contact Us Form

![](/media/ContactForm.JPG)

* Users are able to contact us by filling the form provided.


