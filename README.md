# dj-commerce-api
Fully featured E-Commerce API using Django and Django Rest Framework


| Feature                                  | Permissions | API Endpoint                        | Implemented |
| ---------------------------------------- | ----------- | ----------------------------------- | ----------- |
| **Authentication**                       |             |                                     |             |
| - Login                                  | Public      | /api/auth/login                     | &#9989;     |
| - SignUp                                 | Public      | /api/auth/signup                    | &#10060;    |
| - Logout                                 | User        | /api/auth/logout                    | &#10060;    |
| - Tokens                                 | User        | /api/auth/tokens                    | &#10060;    |
| **Password Management**                  |             |                                     |             |
| - Change Password                        | User        | /api/password/change                | &#10060;    |
| - Forgot Password                        | Public      | /api/password/forgot                | &#10060;    |
| - Reset Password                         | Public      | /api/password/reset                 | &#10060;    |
| **Email Management**                     |             |                                     |             |
| - Send Email Verification                | User        | /api/email/send-verification        | &#10060;    |
| **User**                                 |             |                                     |             |
| - Create New User                        | Admin       | /api/users/create                   | &#10060;    |
| - Get All Users                          | Public      | /api/users                          | &#10060;    |
| - Get User Data Using Its ID             | Public      | /api/users/:id                      | &#10060;    |
| - Update User Details Using Its ID       | User        | /api/users/:id/update               | &#10060;    |
| - Update User Profile Image Using Its ID | User        | /api/users/:id/update-profile-image | &#10060;    |
| - Delete My Account                      | User        | /api/users/delete-my-account        | &#10060;    |
| - Delete User Using Its ID               | Admin       | /api/users/:id/delete               | &#10060;    |
| **Cart Services**                        |             |                                     |             |
| - Add Product To Cart                    | User        | /api/cart/add                       | &#10060;    |
| - Reduce Product Quantity By One         | User        | /api/cart/reduce/:productId         | &#10060;    |
| - Increase Product Quantity By One       | User        | /api/cart/increase/:productId       | &#10060;    |
| - Get Cart                               | User        | /api/cart                           | &#10060;    |
| - Delete Cart Item                       | User        | /api/cart/delete-item/:productId    | &#10060;    |
| - Delete Cart                            | User        | /api/cart/delete                    | &#10060;    |
| **Review Services**                      |             |                                     |             |
| - Create New Review                      | User        | /api/reviews/create                 | &#10060;    |
| - Query All Reviews                      | Public      | /api/reviews                        | &#10060;    |
| - Query Review Using Its ID              | Public      | /api/reviews/:id                    | &#10060;    |
| - Update Review Using Its ID             | User        | /api/reviews/:id/update             | &#10060;    |
| - Delete Review Using Its ID             | User        | /api/reviews/:id/delete             | &#10060;    |
| **Product Services**                     |             |                                     |             |
| - Query Products                         | Public      | /api/products                       | &#10060;    |
| - Query Product Using Its ID             | Public      | /api/products/:id                   | &#10060;    |
| - Create New Product                     | Seller      | /api/products/create                | &#10060;    |
| - Update Product Details                 | Seller      | /api/products/:id/update-details    | &#10060;    |
| - Update Product Main Image              | Seller      | /api/products/:id/update-main-image | &#10060;    |
| - Update Product Images                  | Seller      | /api/products/:id/update-images     | &#10060;    |
| - Delete Product Using Its ID            | User        | /api/products/:id/delete            | &#10060;    |
| - Get Products Statistics                | Admin       | /api/products/stat                  |
| - Top 5 Cheapest Products                | Public      | /api/products/top-cheapest          | &#10060;    |
| - Add Product Color                      | Seller      | /api/products/:id/add-color         | &#10060;    |
| - Add Product Size                       | Seller      | /api/products/:id/add-size          | &#10060;    |
| - Delete Product Color                   | Seller      | /api/products/:id/delete-color      | &#10060;    |
| - Delete Product Size                    | Seller      | /api/products/:id/delete-size       | &#10060;    |
| **Favorite Services**                    |             |                                     |             |
| - Get Favorite Products List             | User        | /api/favorites                      | &#10060;    |
| - Add Product to Favorite List           | User        | /api/favorites/add/:productId       | &#10060;    |
| - Delete Product From Favorite List      | User        | /api/favorites/delete/:productId    | &#10060;    |
| - Check If Product In Favorite List      | User        | /api/favorites/check/:productId     | &#10060;    |
| **Discount Services**                    |             |                                     |             |
| - Generate Discount Code                 | Admin       | /api/discounts/generate             | &#10060;    |
| - Get Discount Amount                    | User        | /api/discounts/:code                | &#10060;    |
| - Get All Discount Codes                 | Admin       | /api/discounts                      | &#10060;    |
| - Verify Discount Code                   | User        | /api/discounts/verify/:code         | &#10060;    |
| - Delete Discount Code                   | Admin       | /api/discounts/:code/delete         | &#10060;    |
| - Cancel Discount Code                   | User        | /api/discounts/:code/cancel         | &#10060;    |
| **Order Services**                       |             |                                     |             |
| - Create New Order                       | User        | /api/orders/create                  | &#10060;    |
| - Query Orders                           | User        | /api/orders                         | &#10060;    |
| - Query Order Using Its ID               | User        | /api/orders/:id                     | &#10060;    |
| - Cancel Order                           | User        | /api/orders/:id/cancel              | &#10060;    |
| - Update Order Status                    | Admin       | /api/orders/:id/update-status       | &#10060;    |
| **Category Services**                    |             |                                     |             |
| - Create New Category                    | User        | /api/categories/create              | &#10060;    |
| - Query Categories                       | Public      | /api/categories                     | &#10060;    |
| - Query Category Using Its ID            | Public      | /api/categories/:id                 | &#10060;    |
| - Update Category Details                | Admin       | /api/categories/:id/update-details  | &#10060;    |
| - Update Category Image                  | Admin       | /api/categories/:id/update-image    | &#10060;    |
| - Delete Category                        | Admin       | /api/categories/:id/delete          | &#10060;    |
| Multi-Language Support                   |             |                                     |             |

