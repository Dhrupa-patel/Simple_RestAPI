# Simple_RestAPI
RestAPI is created which can perform CRUD operations using flask framework.

## How to test RestAPI
Following are the steps to be followed to make API calls.

1. Download the code using clone/Download button from source repository
2. install all necessary libraries using requirements.txt file
3. run app.py file
4. I have tested my RestAPI using [reqbin](https://reqbin.com/)

Following are the four queries can be performed.
1. [Create_cart](http://127.0.0.1:5000/create_cart): This will create new collection in database. I have stored my data in Mongodb Database.
2. [Add Item](http://127.0.0.1:5000/add_item/1): This call will add data to cart_1 as '1' is passed in link. User need to send json object using reqbin tool.
For example, 
```
{
  "Name":"Chestnuts",
  "Price":120,
  "Quantity":"1"
}

```
3. [Delete Item](http://127.0.0.1:5000/add_item/1): This call will delete matching data from cart_1 as '1' is passed in link. 
```
{
  "Name":"Maggie"
}
```
4. [Get Items](http://127.0.0.1:5000/get_item/1): This call will list all items present in cart_1 as '1' is passed in link. Same way any cart details can be accessed by changing the number in link.

