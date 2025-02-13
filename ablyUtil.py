import asyncio
import os
import time
from ably import AblyRealtime

from zoom import automate_zoom, close_zoom, hide_zoom, open_zoom

laptopName = os.getenv('LAPTOP_NAME')

async def Ably(key, channel):
  ably = AblyRealtime(key)
  await ably.connection.once_async('connected')
  print("Connected to Ably")
  
  channel = ably.channels.get(channel)
  
  await channel.subscribe(on_message)
  
  await asyncio.Event().wait()
    
def on_message(message):
  print("Received message: ", message.id, message.data.decode('utf-8'))
  command = str(message.data.decode('utf-8'))
  inputs = command.split(" ") # Command Type {command} {laptopName} {args}
  
  if len(inputs) >= 2:
    if inputs[1] != laptopName:
      return
    
    if inputs[0] == "connect":
      if len(inputs) >= 4:
        close_zoom()
        time.sleep(5)
        open_zoom(inputs[2], inputs[3])
        automate_zoom()
    elif inputs[0] == "hide":
      hide_zoom()    
  