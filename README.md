# assignment2-CMPE273
Abstract

You will be building a pizza ordering system using AWS Lambda for handling business logic, API Gateway for REST interface, and DynamoDB for data persistence.

Requirements

I. Pizza Menu CRUD APIs

You need to implement these REST endpoints to manage menu for any pizza store.

POST /menu
Request

{
    "menu_id": "UUID-generated-by-client",
    "store_name": "Pizza Hut",
    "selection": [
        "Cheese",
        "Pepperoni"
    ],
    "size": [
        "Slide", "Small", "Medium", "Large", "X-Large"
    ],
    "price": [
        "3.50", "7.00", "10.00", "15.00", "20.00"
    ],
    "store_hours": {
        "Mon": "10am-10pm",
        "Tue": "10am-10pm",
        "Wed": "10am-10pm",
        "Thu": "10am-10pm",
        "Fri": "10am-10pm",
        "Sat": "11am-12pm",
        "Sun": "11am-12pm"
    }
}
Response

200 OK
DELETE /menu/{menu-id}
Response

200 OK
GET /menu/{menu-id}
Response

{
    "menu_id": "xxxxxxxxx",
    "store_name": "Pizza Hut",
    "selection": [ 
        "Cheese",
        "Pepperoni"
    ],
    "size": [
        "Slide", "Small", "Medium", "Large", "X-Large"
    ],
    "sequence": [
        "selection",
        "size"
    ],
    "price": [
        "3.50", "7.00", "10.00", "15.00", "20.00"
    ],
    "store_hours": {
        "Mon": "10am-10pm",
        "Tue": "10am-10pm",
        "Wed": "10am-10pm",
        "Thu": "10am-10pm",
        "Fri": "10am-10pm",
        "Sat": "11am-12pm",
        "Sun": "11am-12pm"
    }
}
PUT /menu/{menu-id}
Update the existing menu to add the "Vegetable" option.

Response

{
    "menu_id": "xxxxxxxxx",
    "selection": { 
        "Cheese",
        "Pepperoni",
        "Vegetable"
    }   
}
Response

200 OK
II. Pizza Order Processing APIs

In this part II, you need to implement these REST endpoints to take orders from customers.

NOTE: customer management feature is not required.
POST /order
Request

{   
    "menu_id": "xxxxxxxx",
    "order_id": "uuid_generated_by_client",
    "customer_name": "John Smith",
    "customer_email": "foobar@gmail.com"
}
Response

200 OK

{
    "Message": "Hi {customer_name}, please choose one of these selection:  1. Cheese, 2. Pepperoni, 3.Vegetable"
}
PUT /order/{order_id}
Request

{   
    "input": "1",
}
Response

200 OK

{
    "Message": "Which size do you want? 1. Slide, 2. Small, 3. Medium, 4. Large, 5. X-Large"
}
PUT /order/{order_id}
Request

{   
    "input": "4",
}
Response

200 OK

{
    "Message": "Your order costs $15.00. We will email you when the order is ready. Thank you!"
}

3. GET /order/{order-id}

_Request_

```sh
{   
    "menu_id": "xxxxxxxx",
    "order_id": "uuid_generated_by_client",
    "customer_name": "John Smith",
    "customer_email": "foobar@gmail.com"
    "order_status": "processing"
    "order": {
        "selection": "Cheese",
        "size": "Large",
        "costs": "15.00",
        "order_time": "mm-dd-yyyy@hh:mm:ss"
    }
}
