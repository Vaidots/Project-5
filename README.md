# V_jewelry_G
This is a project that is a part of Diploma in Full Stack Software Development (E-commerce applications)

V_jewelry_G is an online B2C(Business-to-Consumer)online jewelry store, offering wide range of beautiful jewelry pieces that add elegance and sophistication to every occasion. Our customer centrich approach ensures personalizsed experiences, helping shopers find the perfect piece that complements their unique style and personality. Our consumers has the ability to register  and create a profile, chose from different categories of jewelry, modify their basket content, proceed to checkout in a safely way (allauth authentication) and finish the payment using Stripe, receive a confirmation order/email of purchased items, contact us with any enquires and leave a comment on a product they liked. Note that this website is for educational purposes only and do not enter any personal credit/debit card details when using the site.

The live link can be found here - [Stripe card testing](https://stripe.com/docs/testing#cards)

![](/media/IamResponsive.JPG)

The live link can be found here - [Click here](https://projectportfolio5-a694568fc098.herokuapp.com/)

The live link can be found here - [V_jewelry_G](https://projectportfolio5-a694568fc098.herokuapp.com/)

# Table of Contents
1. [User Experience (UX)](#user-experience-ux)
2. [Design](#design)
3. [Features](#features)
   - [Header](#header)
   - [Footer](#footer)
   - [Home Page](#home-page)
   - [User Account Pages](#user-account-pages)
   - [Products](#products)
   - [Comment](#comment)
   - [Shopping Bag](#shopping-bag)
   - [Checkout](#checkout)
   - [Order Confirmation](#order-confirmation)
   - [Profile](#profile)
   - [Contact Us Form](#contact-us-form)
4. [Technologies](#technologies)
   - [Languages](#languages)
   - [Frameworks and Programs](#frameworks-and-programs)
5. [Testing](#testing)
   - [Manual Testing](#manual-testing)
   - [Validator Testing](#validator-testing)
   - [Python Testing](#python-testing)
   - [Lighthouse](#lighthouse)
6. [Deployment](#deployment)
   - [Development Environment](#development-environment)
   - [Deployment to Heroku](#deployment-to-heroku)
   - [Cloning the Repository](#cloning-the-repository)
7. [Future Features](#future-features)
8. [Business Model](#business-model)
9. [Marketing Strategy](#marketing-strategy)
   - [SEO](#seo)
   - [Social Media](#social-media)
   - [Email Marketing](#email-marketing)
10. [Wireframes](#wireframes)
11. [Database Schema](#database-schema)
12. [Credits](#credits)
13. [Acknowledgement](#acknowledgement)


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

## Comment

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


# Database Schema

Two databases were used in creation of this project, during production SQlite was used and then Postgres was used for the deployed Heroku version.

![](/media/DatabaseSchema.JPG)

#Wireframes

<details>

![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.47%20(1).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.47%20(2).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.47%20(3).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.47%20(4).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.47.jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(1).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(2).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(3).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(4).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(5).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(6).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48%20(7).jpeg)
![](/media/WhatsApp%20Image%202023-07-30%20at%2004.07.48.jpeg)

</details> 

## Business Model

V_jewelry_G is a Business to Consumer model (B2C). Products and services are sold directly from the site, to consumers. 

## Marketing Strategy

A number of different strategies have been used to promote V_jewelry_G including SEO, Social media marketing, email marketing.

## SEO 

* Key words were used in meta tags, description and keywords were used to boost the search engine.

* Sitemap was created with a list of important page URLs to ensure that search enginges could understand the site structure and navigate.

* Robott.xt file was created to tell search enginges where they are not allowerd to go on the site.

* Both were created following botique ado modules

## Social Media

For this site, a facebook business page was created to further increase the search engine and users to see the latest deals, information and communication. Also social media icons were created in footer facebook, instagram.


![](/media/FacebookPage.JPG)

## Email Marketing

Customers can sign up to the newsletter which is in the footer, add their email and press subscribe, to receive all the news. Mail chimp was used to create this. Note addblock has to be disabled for the newsletter form to appear.

## Testing

### manual testing
| Feature                          | Test Description                             | Expected Result                                             | Actual Result |
|----------------------------------|----------------------------------------------|-------------------------------------------------------------|---------------|
| V_jewelry_G                      | Selecting logo on homepage                  | Directs the user back to the homepage                       | Pass          |
| Search                           | Using the search box                        | Entering a search returns the expected result               | Pass          |
| Search no results                | No search                                   | Entering a no results search returns an error message and shows all products | Pass |
| Navigation Links                 | Selecting navigation links                  | Directs the user to relevant pages                          | Pass          |
| All products                     | Selecting all products                      | Directs the user to all products                            | Pass          |
| Back to top                      | Back to top arrow                           | Selecting the arrow box on the products page brings the user back to the top of the page | Pass |
| Sort By                          | Selecting the filter Sort                   | Successfully sorts by price, name, and category options     | Pass          |
| Shop Now button                  | Selecting Shop Now button                   | Directs the user to all products page                       | Pass          |
| Sign up for our newsletter       | Selecting Sign up for our newsletter        | Directs the user to the Sign up for our newsletter page     | Pass          |
| Contact                          | Selecting Contact                           | Directs the user to the Contact Us page                     | Pass          |
| Contact form submission          | Submitting the contact form                 | Successfully sends the submitted form and can be seen in the admin panel | Pass |
| Leave a Comment when signed in   | Submitting a comment on a product           | Successfully submits and displays the comment               | Pass          |
| As Admin Delete Comment          | Deleting a comment                          | Successfully removes the comment                             | Pass          |
| My account                       | Selecting my account as admin               | Displays a dropdown menu unique to admin, apart from profile and logout options | Pass |
| Register                         | Register for an account                     | Selecting Register in my account directs the user to the signup page | Pass |
| Register                         | Registering as a new user                   | The registration form for new users works correctly         | Pass          |
| Login                            | Login to an account                         | Selecting Login in my account directs the user to the Login page | Pass |
| Login                            | Login to an account                         | The login form for new users works correctly                | Pass |
| Login as admin                   | Login as admin                              | Logging in as an admin gives access to blog and product management | Pass |
| Logout                           | Message shown                               | The logout message is shown after successful logout         | Pass          |
| Add product to bag               | Adding a product to the shopping bag        | Successfully adds the product to the shopping bag           | Pass          |
| Proceed securely to checkout     | Proceeding to checkout securely             | Successfully navigates to the checkout page                  | Pass          |
| Payment with Stripe              | Making a payment using Stripe               | Payment is processed successfully                            | Pass          |
| Add, Update, Delete products     | Managing products as a superuser            | Superusers can add, update, and delete products              | Pass          |
| Receive confirmation email       | After payment, check email for confirmation | A confirmation email is received after payment               | Pass          |
| Confirmation of order            | After payment, check order status           | Order is confirmed and visible in the user's account         | Pass          |

## Validator testing

### W3 html validator was used to check all the pages of the project.

![](/media/HTMLvalidator.JPG)

* The error in the code, was created by mailchimp, therefore I did not want to make any more errors on top.

### CC3 W3 Validator

![](/media/BaseCSS.JPG)

* This file didnt present any errors or warnings for base,profile,checkout css.

### JShint

* Only a few semicolon warnings was shown.

### Python testing

* Used flask8 in the terminal to check and fix the issues, majority of the errors were from formatting, automatically generated files, code was cleaned as much as possible

## Lighthouse

### Dekstop

![](/media/DekstopLighthouse.JPG)


### Mobile

![](/media/MobiLighthouse.JPG)

* Mobile scores goes lower in other pages, due to picture sizes.


# Future features

* I  have the self-reported rating in the product model (like in the Boutique Ado project). And i would like to implement computed average from user comments would be to have a model method that does it.
* implement a wishlist, blog, time tracker, delivery tracker
* improve the website overall with appropriate size of images.
* Createa a json file for database, as products were uploaded manually.
* Implement more style and function, add react for fron end, to look more visually appealing as this is quite basic.

# Technologies

## Lanugages

* HTML
* CSS
* Javascript
* Pytho

## Frameworks, programs


- [Django](https://www.djangoproject.com/): A high-level Python web framework for rapid development.
- [Bootstrap 4](https://getbootstrap.com/): A CSS framework for responsive and mobile-first design.
- [Gitpod](https://www.gitpod.io/): An online Integrated Development Environment (IDE) used during development.
- [GitHub](https://github.com/): Version control and code repository hosting for the project.
- [Heroku](https://www.heroku.com/): A cloud platform service used for deploying and hosting the project.
- [ElephantSQL](https://www.elephantsql.com/): A cloud-based database service used to store project data.
- [Font Awesome](https://fontawesome.com/): A library of icons used for social media links.
- [PEP8ci](https://pep8online.com/): A tool used to validate Python code against PEP 8 style guidelines.
- [dbdiagram](https://dbdiagram.io/): An online tool used to create the database schema.
- [Stripe](https://stripe.com/): A payment processing platform used for checkout functionality and online payments.
- [AWS](https://aws.amazon.com/): Used for object storage through a web service interface.
- [Unsplash](https://unsplash.com/): Source of images used in the project.
- [Pexels](https://www.pexels.com/): Source of images used in the project.


# Deployment

## Development Environment

This site was developed using **Gitpod** as the Integrated Development Environment (IDE) and **git** for version control.

## Deployment to Heroku

To deploy the site on Heroku, follow these steps:

1. **Log in to Heroku** or create an account if you don't have one.

2. Click **New** and then **Create New App**.

3. Select **Europe** as the region and click the **Create App** button.

4. Create a **database** to connect to the newly created app.

   - **Login to ElephantSQL**, or create an account if needed.
   - Create a new instance and select the **Tiny Turtle free plan**.
   - Choose a region for the data center (e.g., EU-West-1 in Ireland) and click **Create instance**.
   - Click on the database instance name in the ElephantSQL dashboard, and copy the **database URL** from the URL section.

5. Go back to **Heroku**, open your created app, and navigate to **Settings**.

6. Add a **config var** with the key `DATABASE_URL`, and paste the copied database URL from ElephantSQL as the value (without quotation marks).

7. In Gitpod, install **dj-database-url** and **psycopg2** to connect to the external database. Update the `requirements.txt` file with `pip freeze > requirements.txt`.

8. In the Django settings, **import `dj_database_url`** and update the database configuration.

9. **Migrate** your database to the Heroku server.

10. Create a new **superuser** for your database, but be cautious not to commit any sensitive information to GitHub.

11. Install **Gunicorn** (a WSGI HTTP server) and freeze it into the `requirements.txt` file.

12. Create a **Procfile** in the root directory and add `web: gunicorn V_Jewelry_G.wsgi` to it.

13. Run `DISABLE_COLLECTSTATIC=1` to prevent collecting static files during deployment.

14. Commit and push your changes to **GitHub**.

15. On your Heroku app dashboard, go to **Deploy**, connect it to your GitHub repository, and click **Connect**.

16. Choose either **automatic** or **manual deploy**, then click **deploy branch**.

17. When the deployment is complete, click **View** to open the deployed app.

## Cloning the Repository

To clone the repository from GitHub, follow these steps:

### Forking

1. Open the GitHub page that hosts the repository you wish to fork.

2. Find the '**Fork**' button at the top right of the page and click it to fork the repository into your account.

### Cloning

1. Go to the repository page on GitHub.

2. Click on the green button that says "**Code**".

3. Copy the URL under the **HTTPS** tab if you wish to clone using HTTPS.

4. Open a new terminal window, navigate to the directory where you want to store the cloned repository, and type:


# Credits

* Big thank to tutor support for helping me with the issues I faced.
* stackoverflow for code fixing help
* slack community

# Acknowledgement

I would like to thank my Mentor Brian Macharia, for reviewing the code and providing feedback and resources. 
