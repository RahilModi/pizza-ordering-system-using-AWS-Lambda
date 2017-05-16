# -*- coding: utf-8 -*-
import json
import boto3
import time
from time import strftime


def handler(event, context):
    try:
        # select the resource
        _resource = boto3.resource('dynamodb', region_name='us-west-2')
        # select the order table
        _table = _resource.Table('order')

        # attribute of the ordes
        atrs = {'menu_id', 'order_id', 'customer_name', 'customer_email'}

        if all(key in event for key in atrs):

            # change the status to processing
            event['order_status'] = 'processing'
            current_time = strftime("%m-%d-%Y@%H:%M:%S", time.localtime())
            order = {}
            order['selection'] = 'empty'
            order['size'] = 'empty'
            order['cost'] = 'empty'
            order['order_time'] = current_time
            event['order'] = order

            # adding the new order to the table
            _table.put_item(Item=event)

            # select the menu table
            menu_table = _resource.Table('menu')

            # retrieve selection based on the menu_id
            selection = menu_table.get_item(Key={'menu_id': event['menu_id']})

            selectedItem = selection.get('Item').get('selection')

            for i in range(0, len(selectedItem)):
                selectedItem[i] = str(i + 1) + ". " + selectedItem[i]
            selection_str = ", ".join(selectedItem)
            # create response message
            resp = {}
            resp['Msg'] = 'Hi ' + event.get(
                'customer_name') + ', please choose one of these selection:  ' + selection_str
            return resp

        else:
            # key is missing
            return "404: key not found in the table"

    except Exception as excep:
        return excep.message
