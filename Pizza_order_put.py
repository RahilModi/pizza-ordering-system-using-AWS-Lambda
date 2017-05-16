# -*- coding: utf-8 -*-
import json
import time
import boto3

# function to put the order

def handler(event, context):

    keys = {'input'}
    # Make sure the API is correct
    if all(key in event for key in keys):
        resp = {}
        try:
            # selecting the resource
            _resource = boto3.resource('dynamodb', region_name='us-west-2')
            # selecting order table
            _order_table = _resource.Table('order')
            # selecting menu table
            _menu_table = _resource.Table('menu')

        except Exception as excp:
            # returning if exception occurrs
            return excp.message

        _item = _order_table.get_item(
            Key={'order_id': event['order_id']}).get('Item')  #select the order_id from the table retrieve the order 
        # if order  not foun
        if _item == None:
            resp['Msg'] = "404: order_id not found in the order table"
            return resp

        # get order
        order = _item.get('order')

        # get menu_id
        menu_id = _item.get('menu_id')
        # checking that whether customer has selected any order
        if order.get('selection') == 'empty':
            menuOptions = _menu_table.get_item(Key={'menu_id': menu_id}) #menuOptions for the menu_Id
            choice = menuOptions.get(
                'Item').get('selection')[int(event.get('input')) - 1]
            order['selection'] = choice  # add the choice

            sizes = menuOptions.get('Item').get('size')  # options of the sizes
            for j in range(0, len(sizes)):
                sizes[j] = str(j + 1) + ". " + sizes[j]
            size_str = ", ".join(sizes)
            resp['Msg'] = 'size of the pizza? ' + size_str

        elif order.get('size') == 'empty':
            # if size is not mentioned

            menuItem = _menu_table.get_item(
                Key={'menu_id': menu_id})  # menutItem
            size = menuItem.get('Item').get('size')[int(
                event.get('input')) - 1]  # size of the pizza
            order['size'] = size  # set the size of the order
            rate = menuItem.get('Item').get('price')[int(
                event.get('input')) - 1]  # prise of the pizza
            order['cost'] = rate
            resp['Msg'] = 'Your order costs $ {}' + rate + \
                '. We will email you when the order is ready. Thank you!'

            order['order_time'] = time.strftime(
                "%m-%d-%Y@%H:%M:%S")  # time of the order
        else:
            resp['Msg'] = ''
            return resp

        # updating the order item
        _order_table.update_item(
            Key={'order_id': event['order_id']},
            UpdateExpression="SET #order = :ss",
            ExpressionAttributeNames={'#order': 'order'},
            ExpressionAttributeValues={':ss': order}
        )
        # returning the response
        return resp

    else:
        # returning
        return "Key is not found"
