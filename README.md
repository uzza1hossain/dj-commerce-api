# dj-commerce-api
Fully featured E-Commerce API using Django and Django Rest Framework


| Feature                                  | Endpoint                            | Methods                   | Permission             | Implemented |
| ---------------------------------------- | ----------------------------------- | ------------------------- | ---------------------- | ----------- |
| **Authentication**                       |                                     |                           |                        |             |
| - Login                                  | /api/v1/auth/login                  | POST                      | Public                 | &#9989;     |
| - Logout                                 | /api/v1/auth/logout                 | POST                      | Public                 | &#9989;     |
| - Change Password                        | /api/v1/auth/password/change        | POST                      | Authenticated          | &#9989;     |
| - Password Reset                         | /api/v1/auth/password/reset         | POST                      | Public                 | &#9989;     |
| - Password Reset Confirm                 | /api/v1/auth/password/reset/confirm | POST                      | Public                 | &#9989;     |
| - Resend Verification email              | /api/v1/auth/signup/email-resend    | POST                      | Public                 | &#9989;     |
| - Verify Email                           | /api/v1/auth/signup/email-verify    | POST                      | Public                 | &#9989;     |
| - Seller Signup                          | /api/v1/auth/signup/seller          | POST                      | Public                 | &#9989;     |
| - User Signup                            | /api/v1/auth/signup/user            | POST                      | Public                 | &#9989;     |
| - Refresh Token                          | /api/v1/auth/token/refresh          | POST                      | Public                 | &#9989;     |
| - Verify Token                           | /api/v1/auth/token/verify           | POST                      | Public                 | &#9989;     |
| **Address**                              |                                     |                           |                        |             |
| - Add Address or Get All Addresses       | /api/v1/addresses                   | [GET, POST]               | [Authenticated, Owner] | &#9989;     |
| - Get, Update, Delete Address            | /api/v1/addresses/:id               | [GET, PUT, PATCH, DELETE] | Owner                  | &#9989;     |
| **User**                                 |                                     |                           |                        |             |
| - Create New User                        | /api/users/create                   | POST                      | Admin                  | &#10060;    |
| - Get All Users                          | /api/users                          | GET                       | Public                 | &#10060;    |
| - Get User Data Using Its ID             | /api/users/:id                      | GET                       | Public                 | &#10060;    |
| - Update User Details Using Its ID       | /api/users/:id/update               | PUT                       | User                   | &#10060;    |
| - Update User Profile Image Using Its ID | /api/users/:id/update-profile-image | PUT                       | User                   | &#10060;    |
| - Delete My Account                      | /api/users/delete-my-account        | DELETE                    | User                   | &#10060;    |
| - Delete User Using Its ID               | /api/users/:id/delete               | DELETE                    | Admin                  | &#10060;    |
| **Cart Services**                        |                                     |                           |                        |             |
| - Add Product To Cart                    | /api/cart/add                       | POST                      | User                   | &#10060;    |
| - Reduce Product Quantity By One         | /api/cart/reduce                    | PUT                       | User                   | &#10060;    |
| - Increase Product Quantity By One       | /api/cart/increase                  | PUT                       | User                   | &#10060;    |
| - Get Cart                               | /api/cart                           | GET                       | User                   | &#10060;    |
| - Delete Cart Item                       | /api/cart/delete                    | DELETE                    | User                   | &#10060;    |
| - Delete Cart                            | /api/cart/delete-cart               | DELETE                    | User                   | &#10060;    |
| **Review Services**                      |                                     |                           |                        |             |
| - Create New Review                      | /api/review/create                  | POST                      | User                   | &#10060;    |
| - Query All Reviews                      | /api/review                         | GET                       | Public                 | &#10060;    |
| - Query Review Using Its ID              | /api/review/:id                     | GET                       | Public                 | &#10060;    |
| - Update Review Using Its ID             | /api/review/:id/update              | PUT                       | User                   | &#10060;    |
| - Delete Review Using Its ID             | /api/review/:id/delete              | DELETE                    | User                   | &#10060;    |
| **Product Services**                     |                                     |                           |                        |             |
| - Query products                         | /api/products                       | GET                       | Public                 | &#10060;    |
| - Query Product Using Its ID             | /api/products/:id                   | GET                       | Public                 | &#10060;    |
| - Create new product                     | /api/products/create                | POST                      | Seller                 | &#10060;    |
| - Update Product Details                 | /api/products/:id/update            | PUT                       | Seller                 | &#10060;    |
| - Update Product Main Image              | /api/products/:id/update-main-image | PUT                       | Seller                 | &#10060;    |
| - Update Product Images                  | /api/products/:id/update-images     | PUT                       | Seller                 | &#10060;    |
| - Delete Product Using Its ID            | /api/products/:id/delete            | DELETE                    | User                   | &#10060;    |
| - Get Products Statics                   | /api/products/statics               | GET                       | Admin                  | &#10060;    |
| - Top 5 Cheapest Products                | /api/products/cheap                 | GET                       | Public                 | &#10060;    |
| - Add Product Color                      | /api/products/:id/add-color         | PUT                       | Seller                 | &#10060;    |
| - Add Product Size                       | /api/products/:id/add-size          | PUT                       | Seller                 | &#10060;    |
| - Delete Product Color                   | /api/products/:id/delete-color      | DELETE                    | Seller                 | &#10060;    |
| - Delete Product Size                    | /api/products/:id/delete-size       | DELETE                    | Seller                 | &#10060;    |
| **Favorite Services**                    |                                     |                           |                        |             |
| - Get Favorite Products List             | /api/favorites                      | GET                       | User                   | &#10060;    |
| - Add Product to Favorite List           | /api/favorites/add                  | POST                      | User                   | &#10060;    |
| - Delete Product From Favorite List      | /api/favorites/delete               | DELETE                    | User                   | &#10060;    |
| - Check If Product In Favorite List      | /api/favorites/check                | GET                       | User                   | &#10060;    |
| **Discount Services**                    |                                     |                           |                        |             |
| - Generate Discount Code                 | Admin                               | /api/discounts/generate   | POST                   | &#10060;    |
| - GetAllDiscountCodes                    | /api/discount                       | GET                       | Admin                  | &#10060;    |
| - Verify Discount Code                   | /api/discount/verify                | POST                      | User                   | &#10060;    |
| - Delete Discount Code                   | /api/discount/delete/:code          | DELETE                    | Admin                  | &#10060;    |
| - Cancel Discount Code                   | /api/discount/cancel/:code          | POST                      | User                   | &#10060;    |
| **Order Services**                       |                                     |                           |                        |             |
| - Create New Order                       | /api/order/create                   | POST                      | User                   | &#10060;    |
| - Query Orders                           | /api/order                          | GET                       | User                   | &#10060;    |
| - Query Order Using Its ID               | /api/order/:id                      | GET                       | User                   | &#10060;    |
| - Cancel Order                           | /api/order/:id/cancel               | POST                      | User                   | &#10060;    |
| - Update Order Status                    | /api/order/:id/update-status        | PUT                       | Admin                  | &#10060;    |
| **Category Services**                    |                                     |                           |                        |             |
| - Create New Category                    | /api/category/create                | POST                      | User/Seller/Admin      | &#10060;    |
| - Query Categories                       | /api/category                       | GET                       | Public                 | &#10060;    |
| - Query Category Using Its ID            | /api/category/:id                   | GET                       | Public                 | &#10060;    |
| - Update Category Details                | /api/category/:id/update            | PUT                       | Seller/Admin           | &#10060;    |
| - Update Category Image                  | /api/category/:id/update-image      | PUT                       | Seller/Admin           | &#10060;    |
| - Delete Category                        | /api/category/:id/delete            | DELETE                    | Admin                  | &#10060;    |
| **Multi-Language Support**               |                                     |                           |                        |             |
| - Support multiple languages             |                                     |                           |                        | &#10060;    |