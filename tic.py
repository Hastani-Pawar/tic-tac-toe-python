def print_board(board):
    print()
    for row in board:
        print("|" .join(row))
        print("_" * 9)

def check_winner(board,player):
    for i in range(3):

        if all(board[i][j] == player for j in range(3)):
            return True
        
        if all(board[j][i] == player for j in range(3)):
            return True
        
        if all(board[i][i] == player for i in range(3)):
            return True
        
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row )
def play_game():
  board=[[" " for _ in range(3)] for _ in range(3)]
  current_player="X"
  print(" Tic Tac Toe Game")
  print("Player X vs Player O")
  print(" Enter row and column numbers (0,1,2)")

  while True:
    print_board(board)
    print(f"player {current_player} turns")
    try:
       row, col=map(int, input( "enter row and column").split())

       if board[row][col]!= " ":
           print("cell already taken")
           continue
       
    except(ValueError,IndexError):
        print(" invalid input , enter two numbers between 0 and 2")
        continue

    board[row][col]=current_player
    
    if check_winner(board,current_player):
        print_board(board)
        print(f" Player {current_player} wins")
        break
     
    if is_draw(board):
        print_board(board)
        print("it's draw")
        break
    current_player="O" if current_player=="X" else "X"

play_game()        

     