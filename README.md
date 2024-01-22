**NikeThrift Store**
**Introduction**
NikeThrift Store is a Django-based E-Commerce project developed by Stephen Mc Govern. This project encompasses various apps that collectively create a dynamic and functional online thrift store. Each app plays a specific role in managing different aspects of the E-Commerce platform, providing features for users, sellers, and administrators.

**Project Structure**
The project consists of several apps, each serving a distinct purpose:

1. **Carts App**
   
**Models:**
ShoppingCart: Represents a shopping cart with user, price, and creation date.




CartItem: Represents an item in the shopping cart, linking to the Product model.



**------------------------**


**Views**:
add_to_cart: Adds a product to the user's shopping cart.




cart: Displays the user's shopping cart.




delete_from_cart: Deletes an item from the shopping cart.




**------------------------**





**Utilities:**
is_ajax: Helper function to check if the request is an AJAX request.





**------------------------**




**3. comments App**




**Models:**
Comment: Represents a comment with text, seller, buyer, and posting date.





**------------------------**




**Views:**
add_comment: Adds comments.



edit_comment: Edit comments.




delete_comment: Update comments.




**------------------------**




**5. Feeds App**




Models:
Feed: Represents a feed item with a user, verb, target, and creation date.




**------------------------**




**7. Mysite (main app)**
This app includes the main project settings and configurations.




**------------------------**




**9. Orders App**



**Models:**
Order: Represents an order with a user, price, and creation date.




OrderItem: Represents an item in an order, linking to the Product model.




**------------------------**




**11. Static (base.css)**
Contains the base styles for the project.




**------------------------**




**13. Templates (base.html)**_
Contains the base HTML structure for the project.




**------------------------**





**15. Thrifts App**




**Models**:
Product: Represents a product with name, price, image, description, seller, category, user, posting date, and sold status.




**------------------------**




**Views:**
home: Displays a list of products based on the user's role.




list: Displays a list of products with optional sorting, category filtering, and search functionality.




detail: Displays detailed information about a specific product.




edit: Allows editing of a product's details.




delete: Deletes a product (Ajax request).




sell: Handles the addition of a new product.




seller: Displays information about a seller.




**------------------------**





**17. Users App**




**Models:**
Details: Represents additional details for a user, including role and birthdate.




Signals:
create_user_details: Signal to create Details instance when a new User is created.




**------------------------**




**How to Run**
Install Python and Django.





Clone this repository.





Run **pip install -r requirements.txt** to install dependencies.




Run **python manage.py migrate** to apply database migrations.





Run **python manage.py createsuperuser** to create an admin user.




Run **python manage.py runserver** to start the development server.




Visit **http://127.0.0.1:8000/** to access the project.





**------------------------**





**Media**
Images and media sources used in the project.



**------------------------**




Code
Third-party libraries, frameworks, and resources used.





**Acknowledgements**
Special thanks or credits to individuals or organizations that contributed to the project.




**------------------------**





_**Future Features To Develop**_
Social media login



Social media share buttons



Paypal Payment Option



Wishlist




Sort by price functionality




Dark Mode



Shopping Cart
