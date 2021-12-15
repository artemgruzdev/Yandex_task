class Robot:

    def __init__(self, x_0_y_0):
        global step
        self.x_0, self.y_0 = x_0_y_0
        step = [(self.x_0, self.y_0)]

    def move(self, str_path):

        str_path.split()
        x_end = self.x_0
        y_end = self.y_0

        for i in str_path:
            if i == 'N':
                y_end += 1
                step.append((x_end, y_end))
            elif i == 'S':
                y_end -= 1
                step.append((x_end, y_end))
            elif i == 'W':
                x_end -= 1
                step.append((x_end, y_end))
            elif i == 'E':
                x_end += 1
                step.append((x_end, y_end))
        return x_end, y_end

    def path(self):
        return step


r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())
