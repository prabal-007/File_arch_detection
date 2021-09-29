import os
import struct

dir = ''   //file directory path
x_64, x_32, x_x = 0
for filename in os.listdir(dir):
  f = os.path.join(dir, filename)
  
  if os.path.isfile(f):
    vr = struct.calcsize('f') * 8
    if vr == 64:
      x_64 +=1
    elif vr == 32:
      x_32 += 1
    else: x_x += 1
