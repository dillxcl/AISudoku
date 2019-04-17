# AISudoku

The goal of the game is to place N copies of numbers 1 thru N on this board satisfying the following 
constraints in conjunction with constraints stemming from numbers already placed on the board, e.g., cell (1,1) contains 5.

Part1 - Create CNF file 
Ex
Here is the CNF file that corresponds to the simple formula discussed above:

      c  simple_v3_c2.cnf
      c
      p cnf 3 2
      1 -3 0
      2 3 -1 0
      

    1. Each cell contains exactly one copy of any number.
    2. Each row contains every number exactly once, 
           i.e., there are no duplicate copies of a number in a row.
    3. Each column contains every number exactly once,
          i.e., there are no duplicate copies of a number in a column
          
 
 Part 2 - DPLL SAT Solver
 
    1. Unit Propagation
        #Pseudo code
        propagate-units(F):
          for each unit clause {+/-x} in F
          remove all non-unit clauses containing +/-x
          remove all instances of -/+x in every clause // flipped sign!
          
    2. Pure Literal Elimination
        #Pseudo code
        pure-elim(F):   
          for each variable x
            if +/-x is pure in F
              remove all clauses containing +/-x
              add a unit clause {+/-x}
              
    3. Recursive Backtracking
        #Pseudo code
        solve(VARS, F):
          F := propagate-units(F)
          F := pure-elim(F)
          if F contains the empty clause, return the empty clause // call this "unsat" in output
          if F is a consistent set of unit clauses that involves all VARS, return F
          x := pick-a-variable(F) // do anything reasonable here
          if solve(VARS, F + {x}) isn't the empty clause, return solve(VARS, F + {x}) // works to have +x
          else return solve(VARS, F + {-x}) // check -x
          
    All command are in the command.txt to run the program in terminal 
