# -*- coding: utf-8 -*-

import boto3

# function to update the menu_id


def handler(event, context):
    try:

        # select the resource
        _resource = boto3.resource('dynamodb', region_name='us-west-2')

        # select the menu table
        _table = _resource.Table('menu')

        # update the menu_id item
        _table.update_item(
            Key={'menu_id': event['menu_id']},
            UpdateExpression="SET selection = :a",
            ExpressionAttributeValues={':a': event['selection']}
        )

        res = "200: OK"
        return res

    except Exception as excep:
        return excep.message
