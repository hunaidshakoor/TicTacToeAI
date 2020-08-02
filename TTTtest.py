import unittest
from TicTacToe import *

class MyTestCase(unittest.TestCase):

    def create_boards(self):
        #Creates boards for later use
        self.empty_board = initial_state()
        self.x_wins = [['X', 'X', 'X'],
                       ['O', 'O', None],
                       [None, None, None]]

        self.o_wins = [['O', 'O', 'O'],
                       ['X', 'X', None],
                       [None, None, None]]

        self.board_o_next = [['X', 'X', None],
                             ['O', 'O', None],
                             ['X', None, None]]

        self.board_x_next = [['X', None, 'X'],
                             ['O', 'O', None],
                             [None, None, None]]

        self.x_wins_d1 = [['X', None, 'O'],
                          ['O', 'X', None],
                          [None, None, 'X']]

        self.x_wins_d2 = [[None, None, 'X'],
                          ['O', 'X', None],
                          ['X', None, 'O']]

        self.o_wins_d1 = [['O', None, 'X'],
                          ['X', 'O', None],
                          [None, None, 'O']]

        self.o_wins_d2 = [['X', None, 'O'],
                          ['X', 'O', None],
                          ['O', None, 'X']]
        self.x_wins_c =  [['X', None, 'O'],
                          ['X', 'O', None],
                          ['X', None, 'X']]
        self.o_wins_c =  [['O', None, 'X'],
                          ['O', 'X', None],
                          ['O', None, 'X']]
        self.full_board = [['O', 'O', 'X'],
                          ['X', 'X', 'O'],
                          ['O', 'X', 'X']]


    def testplayer(self):
        #checks if returns correct player for different scenarios
        self.create_boards()
        player_ans = player(self.empty_board)
        self.assertEqual(player_ans, 'X')

        self.assertEqual(player(self.board_o_next), 'O')
        self.assertEqual(player(self.board_x_next), 'X')

    def testwinner(self):
        self.create_boards()
        #check row wins
        self.assertEqual(winner(self.x_wins), 'X')
        self.assertEqual(winner(self.o_wins), 'O')
        #check diagonal wins
        self.assertEqual(winner(self.x_wins_d1), 'X')
        self.assertEqual(winner(self.x_wins_d2), 'X')
        self.assertEqual(winner(self.o_wins_d1), 'O')
        self.assertEqual(winner(self.o_wins_d2), 'O')
        #check Column wins
        self.assertEqual(winner(self.o_wins_c), 'O')
        self.assertEqual(winner(self.x_wins_c), 'X')
        #check no winner
        self.assertEqual(winner(self.board_x_next), None)

    def testactions(self):
        #test all moves
        all_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.create_boards()
        self.assertEqual(actions(self.empty_board), all_moves)

        #test one another board
        #self.o_wins_C
        moves =[(0,1), (1, 2), (2, 1)]
        self.assertEqual(actions(self.o_wins_c), moves)

    def testterminal(self):
        self.create_boards()
        #test full board no winner
        self.assertEqual(terminal(self.full_board), True)
        #test board with winner
        self.assertEqual(terminal(self.x_wins_d1), True)
        #test board with spaces and no winner
        self.assertEqual(terminal(self.board_x_next), False)

    def testresults(self):
        self.create_boards()

        #test if action works
        one_spot_board = [['X', None, None],
                          [None, None, None],
                          [None, None, None]]
        result_board = result(self.empty_board, (0, 0))

        self.assertEqual(result_board, one_spot_board)

        #test if error works
        with self.assertRaises(Exception):
            result(result_board, (0,0))




if __name__ == '__main__':
    unittest.main()
