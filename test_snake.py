# test_snake.py

import unittest
from snake import move_snake, place_food, check_collision

class TestSnakeLogic(unittest.TestCase):
    def test_move_without_grow(self):
        s = [(1,1),(0,1)]
        s2 = move_snake(s, (1,0), grow=False)
        self.assertEqual(s2, [(2,1),(1,1)])

    def test_move_with_grow(self):
        s = [(1,1),(0,1)]
        s2 = move_snake(s, (0,1), grow=True)
        self.assertEqual(s2, [(1,2),(1,1),(0,1)])

    def test_place_food_not_on_snake(self):
        snake = [(x,0) for x in range(5)]
        food = place_food(snake, (5,5))
        self.assertNotIn(food, snake)
        self.assertTrue(0 <= food[0] < 5 and 0 <= food[1] < 5)

    def test_check_collision_wall(self):
        self.assertTrue(check_collision([( -1,0)], (10,10)))
        self.assertTrue(check_collision([(10,0)], (10,10)))

    def test_check_collision_self(self):
        s = [(2,2),(2,3),(2,2)]
        self.assertTrue(check_collision(s, (10,10)))

    def test_no_collision(self):
        self.assertFalse(check_collision([(3,3),(3,4)], (10,10)))

if __name__ == "__main__":
    unittest.main()
