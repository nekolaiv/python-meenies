import os
from time import sleep, perf_counter


def delay(time):
    sleep(time)
   

def clear():
    os.system("clear")
    

class Table:
    def __init__(self, table, size, speed:float=0.005) -> None:
        self.table = table
        self.size = size
        self.speed = speed
        
    
    def direct_print(self) -> None:
        print("MAGIC SQUARE SOLVER\n")
        for y in range(self.size):
            print('+---' * self.size, end='+\n')
            for x in range(self.size):
                print('|' + self.table[y][x], end='')
            print('|')
        print('+---' * self.size, end='+\n')
    
    
    def gradual_print(self) -> None:
        speed = self.speed
        for y in range(self.size):
            for x in range(self.size):
                print('+', end='', flush=True)
                sleep(speed)
                for z in range(3):
                    print('-', end='', flush=True)
                    sleep(speed)
            print('+')
            for x in range(self.size):
                print('|', end='', flush=True)
                sleep(speed)
                print(self.table[y][x], end='', flush=True)
                sleep(speed)
            print('|')
            sleep(speed)
        for y in range(self.size):
            print('+', end='', flush=True)
            sleep(speed)
            for x in range(3):
                print('-', end='', flush=True)
                sleep(speed)
        print('+')
        

class Bot:
    def __init__(self):
        self.running = "@=@"
        self.checking = "~=~"
        self.available = "^=^"
        self.occupied = "x=x"


class MagicSquareSolver: 

    bot:Bot = Bot()
    
    def __init__(self, size = 3, speed=0.005) -> None:
        self.table = []
        self.size = size
        self.speed = speed
        
        
    def insert_number(self, x, y, size, count):
        for i in range(size):
            element = [" ", " ", " "]
            for j in range(size):
                number = str(count)
                if count < 10:
                    element[1] = number[0]
                elif count < 100:
                    number = str(count)
                    element[1] = number[0]
                    element[2] = number[1]
                elif count < 1000:
                    element[0] = number[0]
                    element[1] = number[1]
                    element[2] = number[2]
                number = ''.join(element)
                self.table[y][x] = number
                
    
    def update(self, x, y, size, bot_display, status, movement) -> None: 
        move = movement
        print_table:Table = Table(self.table, self.size)
        speed = self.speed
        
        temp = self.table[y][x]
        self.table[y][x] = bot_display
        print_table.direct_print()
        self.table[y][x] = temp
         
        print('  move: ', end='')
        if move == 'up':
            print(move)
        elif move == 'right':
            print(move)
        elif move == 'left':
            print(move)
        elif move == 'down':
            print(move)
        elif move == 'stop':
            print(move)
        
        if status in('checking', 'running', 'printing'):
            print("  status:", status, end='')
            for i in range(3):
                print('.', end='', flush=True)
                sleep(speed)
        else:
            print("  status:", status)
            sleep(speed)
        clear()
    
    def set_number(self) -> None:
        for i in range(self.size):
            element = [" ", " ", " "]
            row = []
            for j in range(self.size):
                number = ''.join(element)
                row.append(number)
            self.table.append(row)
        
    
    def get_user_input(self) -> None:
        while True:
            try:
                self.size = int(input('Table Size(squared): '))
                if self.size % 2 == 0:
                    print("Input Odd numbers only")
                    continue
                break
            except ValueError:
                print("Invalid Input")
        
       
        while True:
            try:
                self.speed = float(input("Speed(seconds): "))
                break
            except ValueError:
                print("Invalid Input")

        
    
    def get_user_choice(self) -> int:
        print("Choose Solving Method:\n1. Manual\n2. Automatic(Unavailable)")
        
        while True:
            try:
                user_choice = int(input("=> "))
                if 1 <= user_choice <= 2:
                    clear()
                    return user_choice
                print("Out of range!")
                continue
            except ValueError:
                print("Invalid Input")
        
        
    def run(self) -> None:
        user_choice = self.get_user_choice()
        if user_choice == 1:
            self.get_user_input()
            
        self.set_number()
        
        table: Table = Table(self.table, self.size)
        table.gradual_print()
        clear()
        
        start_time = perf_counter()
        
        size = self.size
        
        bot:Bot = Bot()
        
        r = 'running'
        c = 'checking'
        a = 'available'
        p = 'printing'
        o = 'occupied'
        
        left = 'left'
        right = 'right'
        up = 'up'
        down = 'down'
        stop = 'stop'
        
        count = 1
        
        x = size // 2
        y = 0
        
        self.update(x, y, size, bot.running, c, stop)
        self.update(x, y, size, bot.available, a, stop)
        self.insert_number(x, y, size, count)
        count += 1
        
        flag = True
        gate = 1
        
        while gate < size * size:
            if flag:
                y = (y - 1) % size
                self.update(x, y, size, bot.running, r, up)
                x = (x + 1) % size
                self.update(x, y, size, bot.checking, c, right)
            else:  
                x = (x - 1) % size
                self.update(x, y, size, bot.running, r, left)
                y = (y + 1) % size
                self.update(x, y, size, bot.running, r, down)
                y = (y + 1) % size
                self.update(x, y, size, bot.checking, c, down)
     
            if self.table[y][x] != '   ':
                self.update(x, y, size, bot.occupied, o, stop)
                flag = False
            else:
                self.update(x, y, size, bot.available, a, stop)
                self.insert_number(x, y, size, count)
                count += 1
                flag = True
                gate += 1
                
        table.direct_print()
        print("\n  status: Done")
        print(f"  total boxes filled: {size*size}")
        
        end_time = perf_counter()
    
        time = end_time - start_time
        runtime = round(time, 5)
        print(f"  solving runtime: {runtime}s")
        

def main() -> None:
    solver:MagicSquareSolver = MagicSquareSolver()
    solver.run()
    
if __name__ == '__main__':
    main()