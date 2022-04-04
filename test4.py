

import tensorflow as tf
import sys
import numpy as np
import os
import time
import asyncio
one_step_model = tf.saved_model.load('bibleai')



states = None
next_char = ''
a = 1
oldstring = ''
line = ''
print('ready', flush=True)
for line in sys.stdin:
        print('ready', flush=True)
        if line.rstrip() != '': 

        

            next_char = next_char + line.rstrip() +'  '
            
            inp2 = tf.constant([next_char])
            result = [inp2]
            start = time.time()
            for n in range(25):
                inp2, states = one_step_model.generate_one_step(inp2, states=states)
                result.append(inp2)
            result = tf.strings.join(result)
            result2 = result[0].numpy().decode('utf-8')
            result2 = result2.replace(oldstring, '')
            result3 = result2.split('  ')
            next_char = next_char +'  ' + result3[1]
            end = time.time()
            oldstring = next_char
            
            print(result3[1], flush=True)

