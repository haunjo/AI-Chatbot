import queue

class State:
    def __init__(self, board, player, move = 0):
        self.board = board
        self.move = move
        self.player = player
        
    def show(self):
        display = ''.join(self.board)
        return display[0:3]+"\n"+\
                display[3:6]+"\n"+\
                display[6:9]+"\n"
    
    def place(self, location):
        if self.player== AI:
            self.board[location]= "X"
            self.player = Human
        elif self.player == Human:
            self.board[location]= "O"
            self.player = AI
        
    def isGameEnd(self):
        display = self.board
        checklist = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
        if 'ㅡ' not in display:
            for i in checklist:
                if (display[i[0]] == display[i[1]] and display[i[0]] == display[i[2]]):
                    if display[i[0]] == 'X':
                        return 1 
                    elif display[i[0]] == 'O':
                        return -1
            else:
                return 0
        else:
            return 3
        
    def minmax(self):
        pass
    
    def AIChoice(self):
        bestscore = -800
        bestMove = 0
        
        for i in range(len(self.board)):

            if self.board[i] == "ㅡ":
                self.board[i] = AI
                score = self.minmax(0, False)
                self.board[i] = "ㅡ"
                print(score, bestscore)
                if(score > bestscore):
                    bestscore = score
                    bestMove = i
        place(bestMove)
                
    def minmax(self, depth, isMaximizing):
        if self.isGameEnd() !=3:
            print(self.isGameEnd())
            return self.isGameEnd()
        if (isMaximizing):
            bestscore = -800
            for i in range(len(self.board)):
                if self.board[i] == "ㅡ":
                    self.board[i] == AI
                    score = self.minmax(depth + 1, False)
                    self.board[i] = "ㅡ"
                    if(score > bestscore):
                        bestscore = score
            return bestscore
        else:
            bestscore = 800
            for i in range(len(self.board)):
                if(self.board[i] == "ㅡ"):
                    self.board[i] = Human
                    score = self.minmax(depth + 1, True)
                    self.board[i] = "ㅡ"
                    if(score < bestscore):
                        bestscore = score
            return bestscore  
            
    
    
start_board = ['ㅡ','ㅡ','ㅡ',
               'ㅡ','ㅡ','ㅡ',
               'ㅡ','ㅡ','ㅡ']
AI = "X"
Human = "O"
goal = ["OOO", "XXX"]

game = State(start_board, AI)

print(game.show())

while game.isGameEnd()==3:
    game.AIChoice()
    print("AI이동")
    print(game.show())
    game.Place(int(input("입력하시오 1~9"))-1)
    print(game.show())
    print("플레이어 이동")
if game.isGameEnd()==1:
    print("AI 승")
elif game.isGameEnd()==-1:
    print("플레이어 승")
elif game.isGameEnd()==0:
    print("무승부")
    
    