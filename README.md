# dj-commerce-api
Fully featured E-Commerce API using Django and Django Rest Framework


| Feature                                  | Endpoint                            | Methods                 | Permission        | Implemented |
| ---------------------------------------- | ----------------------------------- | ----------------------- | ----------------- | ----------- |
| **Authentication**                       |                                     |                         |                   |             |
| - Login                                  | /api/auth/login                     | POST                    | Public            | &#9989;     |
| - SignUp                                 | /api/auth/signup                    | POST                    | Public            | &#10060;    |
| - Logout                                 | /api/auth/logout                    | POST                    | User              | &#10060;    |
| - Tokens                                 | /api/auth/tokens                    | POST                    | User              | &#10060;    |
| **Password Management**                  |                                     |                         |                   |             |
| - Change Password                        | /api/password/change                | POST                    | User              | &#10060;    |
| - Forgot Password                        | /api/password/forgot                | POST                    | Public            | &#10060;    |
| - Reset Password                         | /api/password/reset                 | POST                    | Public            | &#10060;    |
| **Email Management**                     |                                     |                         |                   |             |
| - Send Email Verification                | /api/email/send-verification        | POST                    | User              | &#10060;    |
| **User**                                 |                                     |                         |                   |             |
| - Create New User                        | /api/users/create                   | POST                    | Admin             | &#10060;    |
| - Get All Users                          | /api/users                          | GET                     | Public            | &#10060;    |
| - Get User Data Using Its ID             | /api/users/:id                      | GET                     | Public            | &#10060;    |
| - Update User Details Using Its ID       | /api/users/:id/update               | PUT                     | User              | &#10060;    |
| - Update User Profile Image Using Its ID | /api/users/:id/update-profile-image | PUT                     | User              | &#10060;    |
| - Delete My Account                      | /api/users/delete-my-account        | DELETE                  | User              | &#10060;    |
| - Delete User Using Its ID               | /api/users/:id/delete               | DELETE                  | Admin             | &#10060;    |
| **Cart Services**                        |                                     |                         |                   |             |
| - Add Product To Cart                    | /api/cart/add                       | POST                    | User              | &#10060;    |
| - Reduce Product Quantity By One         | /api/cart/reduce                    | PUT                     | User              | &#10060;    |
| - Increase Product Quantity By One       | /api/cart/increase                  | PUT                     | User              | &#10060;    |
| - Get Cart                               | /api/cart                           | GET                     | User              | &#10060;    |
| - Delete Cart Item                       | /api/cart/delete                    | DELETE                  | User              | &#10060;    |
| - Delete Cart                            | /api/cart/delete-cart               | DELETE                  | User              | &#10060;    |
| **Review Services**                      |                                     |                         |                   |             |
| - Create New Review                      | /api/review/create                  | POST                    | User              | &#10060;    |
| - Query All Reviews                      | /api/review                         | GET                     | Public            | &#10060;    |
| - Query Review Using Its ID              | /api/review/:id                     | GET                     | Public            | &#10060;    |
| - Update Review Using Its ID             | /api/review/:id/update              | PUT                     | User              | &#10060;    |
| - Delete Review Using Its ID             | /api/review/:id/delete              | DELETE                  | User              | &#10060;    |
| **Product Services**                     |                                     |                         |                   |             |
| - Query products                         | /api/products                       | GET                     | Public            | &#10060;    |
| - Query Product Using Its ID             | /api/products/:id                   | GET                     | Public            | &#10060;    |
| - Create new product                     | /api/products/create                | POST                    | Seller            | &#10060;    |
| - Update Product Details                 | /api/products/:id/update            | PUT                     | Seller            | &#10060;    |
| - Update Product Main Image              | /api/products/:id/update-main-image | PUT                     | Seller            | &#10060;    |
| - Update Product Images                  | /api/products/:id/update-images     | PUT                     | Seller            | &#10060;    |
| - Delete Product Using Its ID            | /api/products/:id/delete            | DELETE                  | User              | &#10060;    |
| - Get Products Statics                   | /api/products/statics               | GET                     | Admin             | &#10060;    |
| - Top 5 Cheapest Products                | /api/products/cheap                 | GET                     | Public            | &#10060;    |
| - Add Product Color                      | /api/products/:id/add-color         | PUT                     | Seller            | &#10060;    |
| - Add Product Size                       | /api/products/:id/add-size          | PUT                     | Seller            | &#10060;    |
| - Delete Product Color                   | /api/products/:id/delete-color      | DELETE                  | Seller            | &#10060;    |
| - Delete Product Size                    | /api/products/:id/delete-size       | DELETE                  | Seller            | &#10060;    |
| **Favorite Services**                    |                                     |                         |                   |             |
| - Get Favorite Products List             | /api/favorites                      | GET                     | User              | &#10060;    |
| - Add Product to Favorite List           | /api/favorites/add                  | POST                    | User              | &#10060;    |
| - Delete Product From Favorite List      | /api/favorites/delete               | DELETE                  | User              | &#10060;    |
| - Check If Product In Favorite List      | /api/favorites/check                | GET                     | User              | &#10060;    |
| **Discount Services**                    |                                     |                         |                   |             |
| - Generate Discount Code                 | Admin                               | /api/discounts/generate | POST              | &#10060;    |
| - GetAllDiscountCodes                    | /api/discount                       | GET                     | Admin             | &#10060;    |
| - Verify Discount Code                   | /api/discount/verify                | POST                    | User              | &#10060;    |
| - Delete Discount Code                   | /api/discount/delete/:code          | DELETE                  | Admin             | &#10060;    |
| - Cancel Discount Code                   | /api/discount/cancel/:code          | POST                    | User              | &#10060;    |
| **Order Services**                       |                                     |                         |                   |             |
| - Create New Order                       | /api/order/create                   | POST                    | User              | &#10060;    |
| - Query Orders                           | /api/order                          | GET                     | User              | &#10060;    |
| - Query Order Using Its ID               | /api/order/:id                      | GET                     | User              | &#10060;    |
| - Cancel Order                           | /api/order/:id/cancel               | POST                    | User              | &#10060;    |
| - Update Order Status                    | /api/order/:id/update-status        | PUT                     | Admin             | &#10060;    |
| **Category Services**                    |                                     |                         |                   |             |
| - Create New Category                    | /api/category/create                | POST                    | User/Seller/Admin | &#10060;    |
| - Query Categories                       | /api/category                       | GET                     | Public            | &#10060;    |
| - Query Category Using Its ID            | /api/category/:id                   | GET                     | Public            | &#10060;    |
| - Update Category Details                | /api/category/:id/update            | PUT                     | Seller/Admin      | &#10060;    |
| - Update Category Image                  | /api/category/:id/update-image      | PUT                     | Seller/Admin      | &#10060;    |
| - Delete Category                        | /api/category/:id/delete            | DELETE                  | Admin             | &#10060;    |
| **Multi-Language Support**               |                                     |                         |                   |             |
| - Support multiple languages             |                                     |                         |                   | &#10060;    |