from pyglet import *
from pyglet.window import key
from RectangleCollision import *
window = window.Window(width=800,height=600)
window.set_caption('rectangle collision example with pyglet')
keys = key.KeyStateHandler()
window.push_handlers(keys)
class player():
    px = 400
    py = 300
    pw = 101
    ph = 101
    pixels = 5
    dir = '0'
    pimage = image.load('white.png')
class block1():
    bx = 400
    by = 100
    bw = 101
    bh = 101
    ximage = image.load('light green.png')
@window.event
def on_draw():
     window.clear()
     class player_draw():
        player.pimage.blit(player.px,player.py)
     class block_draw():
        block1.ximage.blit(block1.bx,block1.by)

def update(dt):
    class colison_stuff():
      if collision.rectangle(player.px,player.py,block1.bx,block1.by,player.pw,player.ph,block1.bw,block1.bh):
        if player.dir == 'left':
          player.px += player.pixels
        if player.dir == 'right':
          player.px -= player.pixels
        if player.dir == 'up':
          player.py -= player.pixels
        if player.dir == 'down':
          player.py += player.pixels
    class player_stuff():
     if player.px >= 700:
         player.px -= player.pixels
     if player.px <= -15:
         player.px += player.pixels
     if player.py >= 510:
         player.py -= player.pixels
     if player.py <= -15:
         player.py += player.pixels
     class player_keys():
         if keys[key.D]:
            player.px += player.pixels
            player.dir = 'right'
         elif keys[key.A]:
            player.px -= player.pixels
            player.dir = 'left'
         elif keys[key.W]:
            player.py += player.pixels
            player.dir = 'up'
         elif keys[key.S]:
            player.py -= player.pixels
            player.dir = 'down'
clock.schedule_interval(update, 1/120)
app.run()
