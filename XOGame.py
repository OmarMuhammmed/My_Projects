import os 

def clear_screen():
    os.system("cls")

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name 
                break
            print("Invalid name, please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, please choose your symbol (single letters): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol, please use a single letter.")

class Menu:
    def display_main_menu(self):
        print("Welcome to My X-O game!")            
        user_choice = input(""" 1 ==> Start game \n 2 ==> Quit game \n""")
        return user_choice 
    
    def display_end_game_menu(self):
        menu_text = input("""
        Game over! 
        1 ==> Restart Game 
        2 ==> Quit Game 
        Enter your choice (1 or 2): 
        """)
        return menu_text 

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for x in range(0, 10, 3):
            print("|".join(self.board[x:x+3]))
            if x < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol 
            return True 
        return False
    
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit() 
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0 
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()    

    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f"Player {index}, Enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_end_game_menu()
                if choice == "1":
                    self.restart_game() 
                else:
                    self.quit_game()
                    break     

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0 
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 8], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False     

    def check_draw(self):
        return all(not pos.isdigit() for pos in self.board.board)

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                user_choice = int(input("Choose the position from (1:9): "))
                if 1 <= user_choice <= 9 and self.board.update_board(user_choice, player.symbol):
                    break  
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number from 1 to 9")  
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for playing!")

game = Game()
game.start_game()
