from pico2d import *
import random


# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    image = None #클래스 변수. 클래스 객체가 공유하는 하나의 공간을 만들어서 변수를 저장한다. 클래스 자체에 할당되는 변수
    #재사용 할 수 있는 리소스는 재활용 하자.

    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = 0
        if Boy.image == None: #None = Null이라고 생각하자.
            Boy.image = load_image('run_animation.png') #class이름.변수


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(1000)]
    world += team


def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code
close_canvas()
