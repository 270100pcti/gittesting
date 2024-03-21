import pygame
import requests

pygame.init()
pygame.display.set_mode((1920,1080))
requests.post("https://8430699b-dd4a-453c-a428-cf272b51e8b1-00-38p10de3sgv1h.worf.replit.dev/",headers={"type":"join"})
requests.post("https://8430699b-dd4a-453c-a428-cf272b51e8b1-00-38p10de3sgv1h.worf.replit.dev/",headers={"type":"leave"})


requests.post("https://8430699b-dd4a-453c-a428-cf272b51e8b1-00-38p10de3sgv1h.worf.replit.dev/",headers={"type":"update","playerId":"1"},data={"posx":"0","posy":"0","heading":"0"})

input('ok')