# -*- coding: utf-8 -*-
import json
import boto3


# delete the menu_id
def handler(event, context):
    try:

        # select the resource based on the region
        _resource = boto3.resource('dynamodb', region_name='us-west-2')
        # Select the table named menu
        _menu_table = _resource.Table('menu')
        # delete the menu_id from the table
        _menu_table.delete_item(Key={'menu_id': event['menu_id']})

        res = "200: OK"
        return res

    except Exception as excep:
        return excep.message
