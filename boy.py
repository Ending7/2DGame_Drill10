from pico2d import load_image


class Idle:
    @staticmethod #데코레이터 장식자, #객체 생성 용도가 아니다. # 함수를 그룹으로 모아 놓는 행위
    def enter():
        print('IDLE Entered')
        pass

    @staticmethod
    def exit():
        print('IDLE Exit')
        pass
    
    @staticmethod
    def do():
        print('IDLE Do')
        pass

class stateMachine: #상태 변화 관리
    def __init__(self):
        self.cur_state = Idle #객체 생성이 아님
        pass
    def start(self):
        self.cur_state.enter()
        pass

    def update(self):
        self.cur_state.do()
        pass

    def draw(self):
        pass





class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = stateMachine()
        self.state_machine.start()

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()