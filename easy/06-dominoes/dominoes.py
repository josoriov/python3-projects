import random

# Constants
header = "="*70
status = None


class Domino:
    def __init__(self):
        self.__pieces: list[list[int]] = [[x, y] for x in range(7) for y in range(x, 7)]
        self.__player_turn: bool = False
        self.__ledger: list[list[int]] = []
        self.__stock_pieces: list[list[int]] = []
        self.__player_pieces: list[list[int]] = []
        self.__ai_pieces: list[list[int]] = []
        self.__game_started: bool = False
        self.__consecutive_pass: int = 0

    @property
    def player_turn(self) -> bool:
        """Returns the status of the player turn
        True if the current turn if from the player"""
        return self.__player_turn

    @player_turn.setter
    def player_turn(self, value: bool) -> None:
        self.__player_turn = value

    @property
    def ledger(self):
        """Return the ledger's pieces"""
        return self.__ledger

    @property
    def stock_pieces(self):
        """Returns the stock's pieces"""
        return self.__stock_pieces

    @property
    def player_pieces(self):
        """Returns the player's pieces"""
        return self.__player_pieces

    @property
    def ai_pieces(self):
        """Returns the AI's pieces"""
        return self.__ai_pieces

    @property
    def game_started(self):
        """Returns if the game has started or not"""
        return self.__game_started

    @property
    def consecutive_pass(self) -> int:
        """Returns the status of the player turn
        True if the current turn if from the player"""
        return self.__consecutive_pass

    @consecutive_pass.setter
    def consecutive_pass(self, value: bool) -> None:
        self.__consecutive_pass = value

    def shuffle_pieces(self):
        """Shuffle the pieces """
        # Subsample 7 pieces for the player and 7 for the AI, the rest goes into stock
        self.__stock_pieces = self.__pieces.copy()
        sample = random.sample(range(len(self.__pieces)), 14)
        for i in sample[:7]:
            self.__player_pieces.append(self.__stock_pieces[i])
        for i in sample[7:]:
            self.__ai_pieces.append(self.__stock_pieces[i])
        self.__stock_pieces = [i for j, i in enumerate(self.__stock_pieces) if j not in sample]
        self.__player_turn = False

    def add_piece(self, side: str, piece: list[int]) -> bool:
        """
        Takes a piece and a side and add it to the ledger
        If the piece cannot be added, it returns False
        :param side: side in which to add the piece L or R
        :param piece: A piece too ad to the ledger
        :return: bool on whether the piece could be added or not
        """
        if side == "R" and self.__ledger[-1][1] in piece:
            self.__ledger.append(piece)
            if self.__ledger[-2][1] != self.__ledger[-1][0]:
                self.__ledger[-1].reverse()
            return True
        elif side == "L" and self.__ledger[0][0] in piece:
            self.__ledger.insert(0, piece)
            if self.__ledger[0][1] != self.__ledger[1][0]:
                self.__ledger[0].reverse()
            return True
        return False

    def remove_player_piece(self, piece: list[int]) -> bool:
        """
        Try to removes the parameter piece from the player's ledger
        :param piece: the piece to remove
        :return: bool on whether the piece was removed or not
        """
        try:
            self.__player_pieces.remove(piece)
            return True
        except ValueError:
            print(f"Piece {piece} was not found on the player's ledger")
            return False

    def remove_ai_piece(self, piece: list[int]) -> bool:
        """
        Try to removes the parameter piece from the AI's ledger
        :param piece: the piece to remove
        :return: bool on whether the piece was removed or not
        """
        try:
            self.__ai_pieces.remove(piece)
            return True
        except ValueError:
            print(f"Piece {piece} was not found on the AI's ledger")
            return False

    def start_game(self) -> bool:
        """
        Initialize the game by putting the first piece on the ledger
        and assigning the correspondent turn to the player or the AI

        :return: bool on whether the game could be started or not
        """
        while not self.__game_started:
            self.shuffle_pieces()
            # Finding highest double in player of AI pieces
            for i in range(6, -1, -1):
                if [i, i] in self.__player_pieces:
                    self.__player_pieces.remove([i, i])
                    self.__ledger.append([i, i])
                    self.__player_turn = False
                    self.__game_started = True
                    return True
                elif [i, i] in self.__ai_pieces:
                    self.__ai_pieces.remove([i, i])
                    self.__ledger.append([i, i])
                    self.__player_turn = True
                    self.__game_started = True
                    return True
        return False


def game_status(domino: Domino) -> None:
    """
    Print useful information on the current state of the game}

    :param domino: instance of the main class
    :return None
    """
    print(header)
    print(f"Stock pieces: {domino.stock_pieces}")
    print(f"Player's pieces: {domino.player_pieces}")
    print(f"AI's pieces: {domino.ai_pieces}")
    print(f"Ledger: {domino.ledger}")
    print(f"Player's turn: {domino.player_turn}")
    print(f"Consecutive pass(es): {domino.consecutive_pass}")


def player_move(domino: Domino) -> bool:
    """
    Process the move the player is making
    :param domino: instance of the main class
    :return: bool on whether the move was able to be finished or not
    """
    player_pieces = domino.player_pieces
    for i, piece in enumerate(player_pieces):
        print(f"{i}: {piece}")

    move_index = int(input("Choose the piece you want to add (type -1 to pass):\n"))

    if move_index != -1:
        move_side = input("Choose the side (L or R):\n")
        was_added = domino.add_piece(move_side, player_pieces[move_index])
        if was_added:
            domino.player_turn = False
            domino.remove_player_piece(player_pieces[move_index])
            return True
        else:
            print("The chosen move was not possible, please try again!\n")
    else:
        print("You decided to pass on your turn!")
        domino.player_turn = False
        domino.consecutive_pass += 1
        return True
    return False


def ai_move(domino: Domino) -> bool:
    """
    Makes the move fot eh AI on a simple set of statistical rules

    :param domino: instance of the main class
    :return: bool on whether the ai could made the move or not
    """
    domino.player_turn = True
    ledger = domino.ledger
    ai_pieces = domino.ai_pieces

    num_counts = {}
    scores = {}
    # get scores for each digit
    for piece in ledger + ai_pieces:
        for num in piece:
            num_counts[num] = num_counts.get(num, 0) + 1
    # get scores for each piece
    for i, piece in enumerate(ai_pieces):
        scores[i] = num_counts.get(piece[0], 0) + num_counts.get(piece[1], 0)
    # sorting the dictionary of scores
    scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    # Trying moves with the highest ranked dominoes first
    for move_index, _ in scores.items():
        move_piece = ai_pieces[move_index]
        if domino.add_piece("R", move_piece):
            print(f"The AI move was {move_piece}, right side")
            domino.remove_ai_piece(move_piece)
            domino.consecutive_pass = 0
            return True
        elif domino.add_piece("L", move_piece):
            print(f"The AI move was {move_piece}, left side")
            domino.remove_ai_piece(move_piece)
            domino.consecutive_pass = 0
            return True

    print("No move could be made, passing the turn!")
    domino.consecutive_pass += 1
    return False


if __name__ == "__main__":
    domino_game = Domino()
    domino_game.start_game()
    game_status(domino_game)
    player_turn = domino_game.player_turn
    game_finished = False
    while not game_finished:
        if player_turn:
            move_finished = False
            while not move_finished:
                game_status(domino_game)
                move_finished = player_move(domino_game)
        else:
            ai_move(domino_game)
        game_status(domino_game)
        game_finished = True


# !TODO If there are two consecutive passes, check for stalemate and end the game if true
# !TODO function to end the game
