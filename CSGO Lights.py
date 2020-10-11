from __future__ import print_function
from magichome import MagicHomeApi
import socket
import datetime
import server

server = server.GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
controller1 = MagicHomeApi('192.168.1.112', 0)
server.start_server()

RGB=[]
currentHealth=100
while True:
    a = server.get_info("player.state")
    
    
    if(server.get_info("player.team") == "T"):
        RGB =[255,165,0]
    else:
        RGB=[0,0,255]
        
    state = (server.get_info("round"))['bomb']
    #print(state)
    if(state=='planted'):
        controller1.update_device(255, 0, 0)
        time.sleep(30)
        
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        controller1.update_device(0, 0,0)
        time.sleep(0.5)
        controller1.update_device(255, 0,0)
        time.sleep(0.5)
        
        
        controller1.update_device(255, 255, 255)
        time.sleep(4)
        
    newHealth = a['health']
    #print(newHealth)
    if(newHealth<currentHealth):
        controller1.update_device(255, 255, 255)
        time.sleep(0.1)
        controller1.update_device(RGB[0], RGB[1], RGB[2])
        currentHealth = newHealth
       
        
    #print(RGB)
    controller1.update_device(RGB[0], RGB[1], RGB[2])
    
    
    time.sleep(0.1)
    
    
    
    
    