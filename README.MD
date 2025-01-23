# Project: Project: cashregAPP
The aim of this application is to simulate the backend of a cash register application.

The archtecture of the application looks like this:

<img src="https://content.pstmn.io/178eadd5-627a-49a0-99bb-4a3bb438a54c/U2NyZWVuc2hvdCAyMDI1LTAxLTIzIGF0IDIyLjE1LjM3LnBuZw==">

- NOTE: This repository does not contain front end react application
    

# How to Run the app:

## Step 1 Database:

Configure a local or hosted MySQL Database. In my case I am using the AWS RDS Service.

## Step 2 Application:

One way you can run the appication is by cloning or downloading the repo as a zip.

Install the requirements:

``` bash
pip install -r requirements.txt

 ```

Configure the following environment variable inside the config.py file:

``` bash
export DB_USERNAME=
export DB_PASSWORD=
export MYSQL_DB_URL=

 ```

Run the application inside the cashapp_python folder.

``` bash
python3 app.py

 ```

Another way to run the application is to pull the Docker image that is build with the CI in this repo.

``` bash
docker pull dominikwawak/cashier_app:latest

 ```

Then run the application

``` bash
docker run -p 5000:5000  --network host -e DB_USERNAME={YOUR USERNAME HERE} -e DB_PASSWORD={YOUR PASSWORD HERE} -e MYSQL_DB_URL={YOUR URL HERE}  dominikwawak/cashier_app:latest

 ```

# Testing

To test the application you can navigate to the test folder and inside run:

``` bash
pytest test_app.py

 ```

<img src="https://content.pstmn.io/18c93525-a7ce-455c-9387-541845903e1b/U2NyZWVuc2hvdCAyMDI1LTAxLTIzIGF0IDIzLjExLjI5LnBuZw==">

# API Overview

## End-point: Buy Products Query
Request and response example when buying selected products.
### Method: GET
>```
>http://127.0.0.1:5000/products/buy?product_codes=SR1,SR1,GR1,SR1
>```
### Query Params

|Param|value|
|---|---|
|product_codes|SR1,SR1,GR1,SR1|


### Response: 500
```json
{
    "message": "Failed to fetch products",
    "status": "error"
}
```

### Response: 200
```json
{
    "status": "success",
    "total_price": 30.57
}
```

### Response: 200
```json
{
    "status": "success",
    "total_price": 3.11
}
```

### Response: 200
```json
{
    "status": "success",
    "total_price": 16.61
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Products
Request and response example when gettign a list of products.
### Method: GET
>```
>http://127.0.0.1:5000/product
>```
### Response: 200
```json
{
    "products": [
        {
            "product_code": "123",
            "product_name": "tea",
            "product_price": "1.23"
        },
        {
            "product_code": "CF1",
            "product_name": "Coffee",
            "product_price": "11.23"
        },
        {
            "product_code": "GR1",
            "product_name": "Green Tea",
            "product_price": "3.11"
        },
        {
            "product_code": "SR1",
            "product_name": "Strawberries",
            "product_price": "5.00"
        }
    ],
    "status": "success"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get product by code
Request and response example for getting a single product by its product_code
### Method: GET
>```
>http://127.0.0.1:5000/product/SR1
>```
### Response: 200
```json
{
    "product": {
        "product_code": "SR1",
        "product_name": "Strawberries",
        "product_price": "5.00"
    },
    "status": "success"
}
```

### Response: 200
```json
{
    "product": {
        "product_code": "SR1",
        "product_name": "Strawberries",
        "product_price": "5.00"
    },
    "status": "success"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
