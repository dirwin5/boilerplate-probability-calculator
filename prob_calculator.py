import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.ball_d = kwargs
        self.get_contents()
        
        
    def get_contents(self):
        self.contents = []
        for k, v in self.ball_d.items():
            for v in range(v):
                self.contents.append(k)
        self.contents_org = copy.copy(self.contents)
                
    def draw(self, num):
        self.contents = copy.copy(self.contents_org)
        balls_drawn = []
        if num > len(self.contents):
            return self.contents
        for n in range(num):
            ball_to_draw = random.randint(0, len(self.contents) - 1)
            ball_drawn = self.contents.pop(ball_to_draw)
            balls_drawn.append(ball_drawn)
        return balls_drawn
        
            
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for experiment in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        m = True
        for k, v in expected_balls.items():
            count = drawn.count(k)
            if count < v:
                m = False
        if m is True:
            M += 1
    
    prob = M / num_experiments
    return prob
