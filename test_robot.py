import unittest
from robot import *

class TestRobot(unittest.TestCase):

    def test_do_help(self):
        self.assertTrue(do_help(), """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD STEPS - Move forward by STEPS
BACK STEPS    - Move backward by STEPS
RIGHT         - Turn right 90 degrees
LEFT          - Turn left 90 degrees
SPRINT STEPS  - Sprint forward by STEPS (multiple steps)
""")


if __name__ == "__main__":
    unittest.main()