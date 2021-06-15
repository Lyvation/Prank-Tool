from bs4 import BeautifulSoup
import subprocess
import urllib.request
import time
import webbrowser
import random
#import rotatescreen
#screen = rotatescreen.get_primary_display()
#screen.rotate_to(0)

print("Made by Lyvation#6969")
print("Join my discord https://discord.gg/h7m5FTDsSJ")

while True:
    html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
    soup = BeautifulSoup(html,"html.parser")
    insult_text = soup.find('h1')
    print(insult_text.text)
    time.sleep(1)
    links = ["https://youtube.com/brogamerz", "https://discord.gg/h7m5FTDsSJ"] # put in any link/s u want!
    webbrowser.open(random.choice(links))