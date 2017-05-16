
# -*- coding: utf-8 -*-
import json
import boto3

#to post new menu
def handler(event, context):
  try:

     # select resource
    _resource = boto3.resource('dynamodb', region_name='us-west-2')
    # select table
    _table = _resource.Table('menu')

    seq = '["selection", "size"]'
    menu_item = {
               'menu_id':event['menu_id'],
               'store_name':event['store_name'],
               'selection':event['selection'],
               'size':event['size'],
               'price':event['price'],
               'store_hours':event['store_hours'],
               'sequence' : json.loads(seq)
       }
    
    #add the item in the table
    _table.put_item(Item=menu_item)
    
    res = "200 : OK" 
    return res

  except Exception as excep:
    return excep.message
