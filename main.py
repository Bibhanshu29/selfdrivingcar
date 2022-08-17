import pygame

pygame.init() # initializing pygame modules
window = pygame.display.set_mode((1200, 400)) # window size 1200,400
track = pygame.image.load('track5.png') # loading track1 in track variable

car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30,60))
car_x = 150
car_y = 300
clock = pygame.time.Clock()
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
drive = True
direction = 'up'
while drive:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        drive = False
    clock.tick(60)
    cam_x = car_x +cam_x_offset+ 15
    cam_y = car_y + cam_y_offset+ 15
    up_px = window.get_at((cam_x, cam_y-focal_dis))[0]#detecting pixel in front
    down_px = window.get_at((cam_x, cam_y+focal_dis))[0]
    right_px = window.get_at((cam_x+focal_dis, cam_y))[0]
  #change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
      direction = 'right'
      cam_x_offset = 30
      car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
      direction = 'down'
      car_x = car_x + 30
      cam_x_offset = 0
      cam_y_offset = 30
      car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
      direction = 'right'
      car_y = car_y + 30
      cam_y_offset = 0
      cam_x_offset = 30
      car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
      direction = 'up'
      car_x = car_x + 30
      cam_x_offset = 0
      car = pygame.transform.rotate(car, 90)
  # drive
    if direction=='up' and up_px == 255:
      car_y = car_y-2
    elif direction == 'right'and right_px==255:
      car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
      car_y = car_y +2
    window.blit(track, (0,0)) # block Image transfer given track and origin
    window.blit(car, (car_x,car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5) # 5 is radius and 5 is width
    pygame.display.update()