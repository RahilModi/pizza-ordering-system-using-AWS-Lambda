# -*- coding: utf-8 -*-
import json
import boto3

# function to get order by id


def handler(event, context):
    # requested order
    keys = {'order_id'}

    # Make sure the API is correct
    if all(key in event for key in keys):
        try:
            # select resource
            _resource = boto3.resource(
                'dynamodb', region_name='us-west-2')

            # select order table
            _table = _resource.Table('order')

        except Exception as e:
            return e.message

        # select item from the order table based on the order_it
        _item = _table.get_item(
            Key={'order_id': event['order_id']}).get('Item')

        # returning thr item
        return _item
    else:
        # returnin the message
        return "404 : order_id not found in the order table"
