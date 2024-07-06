class tictaetoe:
    
    #constructor initialization
    def __init__(self, minimum = 1, maximum = 100, draw_length = 5):
        self.minimum = minimum
        self.maximum = maximum
        self.draw_length = draw_length
        
        self.ttt = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }

        self.mode = 1
        
    def print_tile(self):
        ttt = self.ttt
        
        print(ttt['top-l'], '|', ttt['top-c'], '|', ttt['top-r']) 
        print('- + - + -') 
        print(ttt['mid-l'], '|', ttt['mid-c'], '|', ttt['mid-r']) 
        print('- + - + -') 
        print(ttt['bot-l'], '|', ttt['bot-c'], '|', ttt['bot-r']) 

    def move(self, position):
        if position in self.ttt and self.ttt[position] == ' ':
            self.ttt[position] = self.turn
            self.print_tile()
            self.mode *= -1

            # horizontal
            if self.ttt['top-l'] != ' ' and (self.ttt['top-l'] == self.ttt['top-c'] == self.ttt['top-r']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif self.ttt['mid-l'] != ' ' and (self.ttt['mid-l'] == self.ttt['mid-c'] == self.ttt['mid-r']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif self.ttt['bot-l'] != ' ' and (self.ttt['bot-l'] == self.ttt['bot-c'] == self.ttt['bot-r']):
                print("Congratulations! " + self.turn + " won!")
                return True
            # vertical
            elif self.ttt['top-l'] != ' ' and (self.ttt['top-l'] == self.ttt['mid-l'] == self.ttt['bot-l']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif self.ttt['top-c'] != ' ' and (self.ttt['top-c'] == self.ttt['mid-c'] == self.ttt['bot-c']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif self.ttt['top-r'] != ' ' and (self.ttt['top-r'] == self.ttt['mid-r'] == self.ttt['bot-r']):
                print("Congratulations! " + self.turn + " won!")
                return True
            # diagonal
            elif self.ttt['top-l'] != ' ' and (self.ttt['top-l'] == self.ttt['mid-c'] == self.ttt['bot-r']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif self.ttt['top-r'] != ' ' and (self.ttt['top-r'] == self.ttt['mid-c'] == self.ttt['bot-l']):
                print("Congratulations! " + self.turn + " won!")
                return True
            elif ' ' not in self.ttt.values():
                print("Draw!")
                return True
            else:
                return False     
                
    def play(self):
        while True:
            
            if (self.mode == 1):
                self.turn = 'X'
            else:
                self.turn = 'O'
            
            print("Turn for " + self.turn + ". Move to which space?")
            position = input()

            if (position == ''):
                self.print_tile()
                print("Do not leave blank. Enter again.")
                continue
            elif position not in self.ttt:
                self.print_tile()
                print("This space is invalid! Enter again.")
                continue
            elif self.ttt[position] != ' ':
                self.print_tile()
                print("This space occupied! Enter again.")
                continue
            else:
                if self.move(position):
                    break
                