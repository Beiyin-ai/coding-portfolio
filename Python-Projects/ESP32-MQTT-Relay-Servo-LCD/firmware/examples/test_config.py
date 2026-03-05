#! /opt/conda/bin/python

# python test_get_conf.py 改過 config.json 之後，要測一下

import json 

myconf = {}
with open( 'config.json' ) as f:
    myconf = json.load(f)
    

print( type( myconf ) )
print( myconf )
print( 'mqtt_broker:', myconf['mqtt_broker'] )
print( 'mqtt_port:', myconf['mqtt_port'] )
print( 'topic_head:', myconf['topic_head'] )
print( 'topic_servo:', myconf['topic_servo'] )
print( 'topic_lcd:', myconf['topic_lcd'] )
print( 'topic_relay:', myconf['topic_relay'] )
print( 'comment:', myconf['comment'] )