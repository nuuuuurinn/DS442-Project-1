# Project 1: Solve the River Crossing Puzzle with search algorithms (DFS, BFS, UCS, A*)

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

#### Question-1 DFS and BFS for the River Crossing Puzzle
DFS:

• Implement DFS algorithm that works with starting state that is read in from an input file called
input.txt. The format of the state should be the same as what we mention above.

• Output: path of states returned, total cost (where cost is defined in terms of number of
actions),and number of node expansions.

BFS:

• Implement a BFS that works with starting state that is read in from an input file called input.txt.
The format of the state should be the same as what we mention above.

• Output: path of states returned, total cost (where cost is defined in terms of number of actions),
and number of node expansions.

#### Questions-2 Uniform Cost Search (UCS) with Non-Uniform Action Costs
We now extend the river crossing puzzle to include non-uniform action costs, so that path cost may
differ from path length. UCS should always return a least-cost solution.

State format remains:
M_left, C_left, M_right, C_right, Boat

UCS: 

Implement Uniform Cost Search in solution_q2.py

• Output: path of states returned, total cost, and number of node expansions.

• Your program must support two different cost models:

A. Cost Model A — Cost by Passenger Type

Story Motivation: Missionaries carry heavy books and supplies, while cannibals travel light. Every
missionary on the boat adds more rowing effort. Hence, it is twice as costly to carry a missionary as
compared to a cannibal.

Cost = 2 units per missionary + 1 unit per cannibal.

Examples:

• Move {M, M} → cost 4

• Move {C, C} → cost 2

• Move {M, C} → cost 3

B. Cost Model B — Cost by Boat Direction

Story Motivation: The river current flows right → left. Going against the current (left → right) is harder,
while coming back (right → left) is easier.

• Left → Right trip = cost 2

• Right → Left trip = cost 1

#### Question 3: A* Search with Admissible Heuristics
In this part, you will extend UCS to A* search using Cost Model A. 
We will use the following heuristics with A*

Heuristic 1 — Passenger Weight Remaining: _h1_(𝑠) = 2𝑀(left) + 1𝐶(left)

Heuristic 2 — Trip-Packing Lower Bound: _h2_(𝑠) = ⌈(2𝑀(left) + 1𝐶(left))/3⌉
