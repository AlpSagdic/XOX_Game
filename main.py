from data import logo, board, p1_chart, p2_chart, game_chart

should_cont = True
player1_turn = True
round_num = 0
print(logo)
while should_cont:
    print("[-=-][-=-][-=-][-=-][-=-][-=-]")
    game_chart()

    #Winning probabilities based on XOX game dynamics.
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
            board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] \
            or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:

        #If it is player 1's turn after the move, player 2 win.
        if player1_turn:
            print("Player 2 win!")
            should_cont = False
            player1_turn = False

        #If it is player 2's turn after the move, player 1 win.
        else:
            print("Player 1 win!")
            should_cont = False
            player1_turn = False

    #If the whole table is full before someone wins.
    elif round_num == 9:
        print("Draw!")
        should_cont = False
        player1_turn = False

    elif player1_turn:
        p1_choice = int(input("Your turn player 1\n Which number do you want to choose (1 to 9)? "))

        #If the place of the selected number is empty.
        if p1_choice in board:
            p1_chart.append(p1_choice)
            board[p1_choice-1] = "X"
            round_num += 1
            player1_turn = False
        else:

            #If the selected number is full.
            if board[p1_choice-1] == "O" or board[p1_choice-1] == "X":
                print("Already Full Try Again!")

            #If a number other than 1 to 9 (or letter etc.)
            else:
                print("Please choose a number from 1 to 9!")

    else:
        p2_choice = int(input("Your turn player 2\n Which number do you want to choose (1 to 9)? "))

        #If the place of the selected number is empty.
        if p2_choice in board:
            p2_chart.append(p2_choice)
            board[p2_choice-1] = "O"
            round_num += 1
            player1_turn = True
        else:

            #If the selected number is full.
            if board[p2_choice-1] == "X" or board[p2_choice-1] == "O":
                print("Already Full Try Again!")

            #If a number other than 1 to 9 (or letter etc.)
            else:
                print("Please choose a number from 1 to 9!")
