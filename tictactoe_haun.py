

class State:
    def __init__(self, board, move = 0):
        self.board = board
        self.move = move
        
    def show(self):
        display = ''.join(self.board)
        return display[0]+'_'+display[1]+'_'+display[2]+"\n"+\
                display[3]+'_'+display[4]+'_'+display[5]+"\n"+\
                display[6]+'_'+display[7]+'_'+display[8]+"\n"
                
    def place(self, player ,location):
        if player == AI:
            self.board[location] = AI
        elif player == Human:
            if self.board[location] != '_':
                    self.place( Human ,int(input("빈 공간에 다시 입력하시오 (1~9) : "))-1)
            else:
                self.board[location] = Human   
            
    def isGameEnd(self):
        display = self.board
        #print(self.show())
        checklist = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
        for i in checklist:
            if (display[i[0]] == display[i[1]] and display[i[0]] == display[i[2]] and display[i[0]] != 'ㅡ'):
                if display[i[0]] == 'X':
                    return 1 
                elif display[i[0]] == 'O':
                    return -1
        if display.count('_') == 0:
            return 0
        else:
            return 3
        
    
    def AIChoice(self):
        bestscore = -50
        bestMove = 0
        
        for i in range(len(self.board)):
            if self.board[i] == "_":
                self.board[i] = AI
                score = self.minmax(0, False)
                self.board[i] = "_"
                #print(score, bestscore)
                if(score > bestscore):
                    bestscore = score
                    bestMove = i
        self.place(AI , bestMove)
                
    def minmax(self, depth, isMaximizing):
        if (self.isGameEnd()) !=3:
            return self.isGameEnd()
        if (isMaximizing):
            bestscore = -50
            for i in range(len(self.board)):
                if self.board[i] == '_':
                    self.board[i] = AI
                    score = self.minmax(depth + 1, False)
                    self.board[i] = '_'
                    if(score > bestscore):
                        bestscore = score
            return bestscore
        else:
            bestscore = 50
            for i in range(len(self.board)):
                if(self.board[i] == "_"):
                    self.board[i] = Human
                    score = self.minmax(depth + 1, True)
                    self.board[i] = "_"
                    if(score < bestscore):
                        bestscore = score
            return bestscore  
            
    
    
start_board = ['_','_','_',
               '_','_','_',
               '_','_','_']
AI = "X"
Human = "O"

game = State(start_board, AI)

print(game.show())

while (game.isGameEnd())==3:
    game.AIChoice()
    print("AI이동")
    print(game.show())
    if (game.isGameEnd()) !=3:
        break
    game.place( Human ,int(input("입력하시오 (1~9) : "))-1)
    print("플레이어 차례")
    print(game.show())
    
if game.isGameEnd()==1:
    print("AI 차례")
elif game.isGameEnd()==-1:
    print("플레이어 승")
elif game.isGameEnd()==0:
    print("무승부")
    
    