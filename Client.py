import requests
import json


#Defining the API url
API_URL='http://127.0.0.1:5000/products'

#Defining  a function to add a new product
def add_product(name,description,price):
    product_data={
        'name':name,
        'description':description,
        'price':price,
    }
    response=requests.post(API_URL, json=product_data)

    if response.status_code==201:
        print(f"Product '{name}'created successfully!")
    elif response.status_code==400:
        print("Error: Invalid input data!")
    else:
        print("Error:",response.json())

  #Defining a function to get all products
def get_products  ():
    response=requests.get(API_URL)

    if response.status_code==200:
        products=response.json() 
        print("Product List:")   
        for product in products:
            print(f"Name: {product['name']},Description:{product['description']},Price: {product['price']}")
    else:
        print("Error:",response.json())


if _name== 'main_':

    #Add new products
    add_product("Laptop","High-performance and good storage",25000)
    add_product("Smartwatch","monitors heartrate,monitors walking steps",3000)


 #Retrieve and display products
get_products()