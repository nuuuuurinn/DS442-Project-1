# DS442-Project-1
Project 1: Solve the River Crossing Puzzle

### Project Description
The River Crossing Puzzle is a classic AI problem. In this puzzle, you must transport a group of characters across a river using a boat, subject to rules and constraints.

Scenario (Missionaries & Cannibals variant):
• There are 3 missionaries and 3 cannibals on the left bank of the river.
• The boat can carry at most 2 people at a time, and has to carry at least one person at a time.
• At no point on either bank should cannibals outnumber missionaries (if missionaries are present).

The goal state is to move all missionaries and cannibals to the right bank without breaking the rules by implementing search algorithms (DFS, BFS, UCS, A*) in Python 3.9 to solve this problem under different conditions.

The program must read from input.txt, which specifies the initial state of the puzzle
• The state will be represented as: M_left, C_left, M_right, C_right, Boat
where M_left and M_right and C_right and Boat is either L (left) or C_left are the number of missionaries and cannibals on the left bank, are the number of missionaries and cannibals on the right bank, R (right).
• Example initial state in which all three missionaries and cannibals are on the left bank, and the boat is standing on the left bank as well: 3, 3, 0, 0, L
As the solution of this project, the code for each question should print: 
(i) the sequence of actions your algorithm finds
(ii) total cost associated with this sequence of actions (if applicable)
(iii) number of node expansions that occur in your tree search
