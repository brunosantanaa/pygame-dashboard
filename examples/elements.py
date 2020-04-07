import pygame, sys
import Dashboard
import dashdraw
# stup pygame
pygame.init()

# window
ws = pygame.display.set_mode((800, 600))

# backgournd
background = (33, 33, 33)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

lamp1 = Dashboard.Lamp(ws, (300, 300), name="Nandin")
def teste(obj):
  lamp1.set_state(obj)  

bt = Dashboard.ButtonONOFF(ws, (100, 300), callback=teste)
raio = 60
x = 2 * raio + 5
g1 = Dashboard.Gauge(ws, (x, 100), raio)
g2 = Dashboard.Gauge(ws, (2*x, 100), raio, display=Dashboard.Gauge.ARROW)
g2.set_max(300)

g3 = Dashboard.Gauge(ws, (3*x, 100), raio, color=(0, 200, 0), display=Dashboard.Gauge.ARROW, thickness= 10)
g3.set_max(270)

g4 = Dashboard.Gauge(ws, (4*x, 100), raio, color=(200, 20, 0), display=Dashboard.Gauge.ARROW, thickness = 2)
g4.set_max(180)

g5 = Dashboard.Gauge(ws, (5*x, 100), raio, color=(200, 20, 200), display=Dashboard.Gauge.BAR)

def call_sld(clickup, pos):
  if clickup: 
    print pos
    g1.set_value(pos)

sld = Dashboard.Slide(ws, (100, 400), callback = call_sld)

ev = Dashboard.Event()

sld.draw(0.7)


while not done:

  # This limits the while loop to a max of 10 times per second.
  # Leave this out and we will use all CPU we can.
  clock.tick(10)
  for event in pygame.event.get(): # User did something
    ev.active(event, [bt.click, sld.click])
    if event.type == pygame.QUIT: # If user clicked close
      done=True # Flag that we are done so we exit this loop
  
  ws.fill(background)


  bt.draw()
  g1.draw(sld.get_pos())
  g2.draw(sld.get_pos())
  g3.draw(sld.get_pos())
  g4.draw(sld.get_pos())
  g5.draw(sld.get_pos())
  sld.draw()

  lamp1.draw()

  r = pygame.Rect(10, 10, 100, 40)


  # Go ahead and update the screen with what we've drawn.
  # This MUST happen after all the other drawing commands.
  pygame.display.flip()

# Be IDLE friendly
pygame.quit()