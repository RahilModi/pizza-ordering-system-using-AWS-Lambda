# -*- coding: utf-8 -*-
import boto3

# to get the menu based on the menu_id


def handler(event, context):
    try:
        # select resource
        _resource = boto3.resource('dynamodb', region_name='us-west-2')

        # select menu table
        _table = _resource.Table('menu')

        # get item mentioned based on the menu_id
        _itemsInTable = _table.get_item(Key={'menu_id': event['menu_id']})

        _item = _itemsInTable.get('Item')
        # checks whether item is available or not

        if _item == None:
            res = "404 :  menu_id is not found in the menu table"
            return res
        else:
            return _item  # returning the retrieved item

    except Exception as excep:
        return excep.message
