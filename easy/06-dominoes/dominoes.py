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
    def status(self):
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

    def add_piece(self, side: str, piece: list[int]) -> str:
        if side == "R":
            self.__snake
        return ""

    def move(self, player: str, piece: int, side: str) -> str:
        # takes the piece to input (by index) and append it to the snake
        # if cannot do return message
        # switches the turn
        check_number = self.__snake[0][0] if side == "L" else self.__snake[-1][-1]
        if player == "player":
            move_piece = self.__player_pieces[piece]
            del self.__player_pieces[piece]
        elif player == "computer":
            move_piece = self.__ai_pieces[piece]
            del self.__ai_pieces[piece]

        # Check if the move is possible
        if check_number in move_piece:

            self.__snake.insert(0, move_piece) if side == "L" else self.__snake.append(move_piece)

        # switch turn
        return ""


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


if __name__ == "__main__":
    domino_game = Domino()
    domino_game.shuffle_pieces()
    response = domino_game.start_game()
    print(response)
    game = True
    while game:
        response = game_status(domino_game)
        print(response)
        game = False
