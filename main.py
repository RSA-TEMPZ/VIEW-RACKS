#imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#variables
#these variables will be
#changed by the input funcation
Timer = 3
link = ''
views = 10

print('''____________________________________________________
|,---.        ) ALT.PEEVES of USENET (          ,---.|
|) 1 (        `====---    _   ---===='          ) 1 (|
| \ /                    | |                     \ / |
|  V      ,-.            |-|                      V  |
|        ( D )          _|-|_          Youtbe        |
|         `-'         _(_) (_)          Views        |
|                    (_) | | L_.         RSA         |
|      M21141815E    '      (_  \                    |
| / \               (        /  /                / \ |
|( 1 )                                          ( 1 )|
| \ / ---==<         Youtube Views       >==---  \ / |
|____________________________________________________|''')
print("Made by [✞]RSA[✞]汞Tempz汞#3332")
print("Timer stays on 3seconds")

#These are the input funcations
LK = input("Link For Video:")
link = LK
VS = input("How many views:")
views = VS

#This will tell the chromedriver where to go
browser = webdriver.Chrome()
browser.get(link)

#this tells the chromedriver what to do
for i in range(views):
    time.sleep(Timer)
    browser.refresh()
#==============
#Skid info
#==============
#if you skid this and that means only changing the ascii art and shit 
#then kys. cuz i spent time on that and this does not mean your a coder if you do this
#just use it to make your own or make a better one