import random

# Constants
header = "="*70
status = None


class Domino:
    def __init__(self):
        self.__pieces = [[x, y] for x in range(7) for y in range(x, 7)]
        self.__turn = None
        self.__snake = []
        self.__stock_pieces = []
        self.__player_pieces = []
        self.__ai_pieces = []

    @property
    def turn(self):
        return self.__turn

    @property
    def snake(self):
        return self.__snake

    @property
    def stock_pieces(self):
        return self.__stock_pieces

    @property
    def player_pieces(self):
        return self.__player_pieces

    @property
    def ai_pieces(self):
        return self.__ai_pieces

    def shuffle_pieces(self):
        # Subsample 7 pieces for the player and 7 for the AI, the rest goes into stock
        self.__stock_pieces = self.__pieces.copy()
        sample = random.sample(range(len(self.__pieces)), 14)
        for i in sample[:7]:
            self.__player_pieces.append(self.__stock_pieces[i])
        for i in sample[7:]:
            self.__ai_pieces.append(self.__stock_pieces[i])
        self.__stock_pieces = [i for j, i in enumerate(self.__stock_pieces) if j not in sample]
        self.__turn = None

    def start_game(self):
        # check the highest double on player deck of AI deck
        for i in range(6, -1, -1):
            double = [i, i]
            if double in self.__player_pieces:
                self.__snake.append(double)
                self.__player_pieces.remove(double)
                self.__turn = "computer"
                break
            elif double in self.__ai_pieces:
                self.__snake.append(double)
                self.__ai_pieces.remove(double)
                self.__turn = "player"
                break
        if len(self.__snake) == 0:
            return "Double not found on player's or AI pieces. Shuffle again.\n"
        return "Game started correctly.\n"

    def next_move(self):
        if self.__turn == "computer":
            return "Status: Computer is about to make a move. Press Enter to continue...\n"
        elif self.__turn == "player":
            return "Status: It's your turn to make a move. Enter your command.\n"
        return "Status: game not started\n"

    def switch_turn(self):
        if self.__turn == "computer":
            self.__turn = "player"
        elif self.__turn == "player":
            self.__turn = "computer"

    def add_piece(self, side: str, piece: list[int]) -> bool:
        if side == "R" and self.__snake[-1][1] in piece:
            self.__snake.append(piece)
            if self.__snake[-2][1] != self.__snake[-1][0]:
                self.__snake[-1].reverse()
            return True
        elif side == "L" and self.__snake[0][0] in piece:
            self.__snake.insert(0, piece)
            if self.__snake[0][1] != self.__snake[1][0]:
                self.__snake[0].reverse()
            return True
        return False

    def move(self, player: str, piece_loc: int, side: str) -> str:
        # takes the piece to input (by index) and append it to the snake
        # if cannot do return message
        # switches the turn
        if player == "player":
            move_piece = self.__player_pieces[piece_loc]
            del self.__player_pieces[piece_loc]
        elif player == "computer":
            move_piece = self.__ai_pieces[piece_loc]
            del self.__ai_pieces[piece_loc]

        # Make the move
        add_response = self.add_piece(side, move_piece)

        # If the piece was added, return good message and switch turn
        if add_response:
            self.switch_turn()
            return f"Correctly added {move_piece} to the domino snake"
        # If the move cannot be made put back the piece and return bad message
        if player == "player":
            self.__player_pieces.append(move_piece)
        elif player == "computer":
            self.__ai_pieces.append(move_piece)

        return "The move cannot be made. Check the parameters inputted."

    def stalemate(self) -> bool:
        is_stalemate = True
        # If a move can be made, there is no stalemate
        for piece in self.__ai_pieces:
            if self.add_piece("R", piece) or self.add_piece("L", piece):
                return False
        for piece in self.__player_pieces:
            if self.add_piece("R", piece) or self.add_piece("L", piece):
                return False

        return is_stalemate


def game_status(domino: Domino) -> str:
    global header
    ans = f"{header}\nStock size: {len(domino.stock_pieces)}\nComputer pieces: {domino.ai_pieces}\n\n"
    snake = ",".join(f"{x}" for x in domino.snake)
    ans += f"{snake}\n\n"
    player_pieces = domino.player_pieces
    ans += "Your pieces:\n"
    for i, piece in enumerate(player_pieces):
        ans += f"{i+1}:{piece}\n"

    ans += f"\n{domino.next_move()}"
    return ans


def make_move(domino: Domino):
    move = input("Enter the piece number of the stack and the direction e.g. 6R (piece 6 right side):\n")
    piece_loc = int(move[0]) - 1
    piece_side = move[1]
    player = domino.turn

    resp = domino.move(player, piece_loc, piece_side)

    return resp


if __name__ == "__main__":
    domino_game = Domino()
    domino_game.shuffle_pieces()
    response = domino_game.start_game()
    print(response)
    turn = domino_game.turn
    game = True
    while game:
        response = game_status(domino_game)
        print(response)

        game = False


# !TODO Create an function that returns True if the game is in a stalemate
# !TODO If the game is not on a stalemate continue the game
# !TODO function to take user input and make the move
