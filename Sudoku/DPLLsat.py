#!/usr/bin/python3

import sys, getopt
import random
import copy
class SatInstance:
    def __init__(self):
        pass
    def from_file(self, inputfile):
        self.clauses = list()
        self.VARS = set()
        self.p = 0
        self.cnf = 0
        with open(inputfile, "r") as input_file:
            self.clauses.append(list())
            maxvar = 0
            for line in input_file:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        maxvar = max(maxvar, abs(lit))
                        if lit == 0:
                            self.clauses.append(list())
                        else:
                            self.clauses[-1].append(lit)
                if tokens[0] == "p":
                    self.p = int(tokens[2])
                    self.cnf = int(tokens[3])
            assert len(self.clauses[-1]) == 0
            self.clauses.pop()
            if not (maxvar == self.p):
              print("Non-standard CNF encoding!")
              sys.exit(5)
      # Variables are numbered from 1 to p
        length = self.p%10 
        for i in range(length):
          for j in range(length):
            for k in range(length):
              self.VARS.add(int(str(i+1)+str(j+1)+str(k+1)))
    def __str__(self):
        s = ""
        for clause in self.clauses:
            s += str(clause)
            s += "\n"
        return s



def main(argv):
   inputfile = ''
   verbosity=False
   inputflag=False
   try:
      opts, args = getopt.getopt(argv,"hi:v",["ifile="])
   except getopt.GetoptError:
      print ('DPLLsat.py -i <inputCNFfile> [-v] ')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('DPLLsat.py -i <inputCNFfile> [-v]')
           sys.exit()
    ##-v sets the verbosity of informational output
    ## (set to true for output veriable assignments, defaults to false)
       elif opt == '-v':
           verbosity = True
       elif opt in ("-i", "--ifile"):
           inputfile = arg
           inputflag = True
   if inputflag:
       instance = SatInstance()
       instance.from_file(inputfile)
       solve_dpll(instance, verbosity)
   else:
       print("You must have an input file!")
       print ('DPLLsat.py -i <inputCNFfile> [-v]')


""" Question 2 """
# Finds a satisfying assignment to a SAT instance,
# using the DPLL algorithm.
# Input: a SAT instance and verbosity flag
# Output: print "UNSAT" or
#    "SAT"
#    list of true literals (if verbosity == True)
#    list of false literals (if verbosity == True)
#
#  You will need to define your own
#  solve(VARS, F), pure-elim(F), propagate-units(F), and
#  any other auxiliary functions
def propagate_units(F):
  
  #Initializing
  one_literal = []
  neg_one_literal = []

  #Get the +/-x
  for line in F:
    if len(line) == 1:
      line = list(line)
      one_literal.append(line[0])
      neg_one_literal.append(-line[0])


  i = 0 
  a = 0

  #Remove or pop depending on +/- x
  while i < len(F):
    while a < len(one_literal):
      if len(F[i]) > 1:
        #del all-unit clauses
        if one_literal[a] in F[i]:
            F.pop(i)
            if i == 0:
              break
            else: 
              i = i - 1
        #remove flipped value
        if neg_one_literal[a] in F[i]:
          F[i].remove(neg_one_literal[a])
      else:
        #remove flipped value when len = 1 
        if neg_one_literal[a] in F[i]:
          F[i].remove(neg_one_literal[a])
      a = a + 1

    a = 0 
    i = i + 1
  return F

def pure_elim(F): 
  length = len(F)
  i = 0 
  j = 0
  pos_clauses = []
  neg_clauses = []
  pure_list = []

  #Get the positive and negative values from instance clauses
  while i < length:
    j_len = len(F[i])
    while j < j_len:
      if F[i][j] >= 0: 
        pos_clauses.append(F[i][j])
      else: 
        neg_clauses.append(abs(F[i][j]))
      j = j+1
    j = 0
    i = i + 1

  #Compare positive and negative if they have duplicate
  for pos_elem in pos_clauses:
    if pos_elem not in neg_clauses:
      pure_list.append(pos_elem)
  for neg_elem in neg_clauses:
    if neg_elem not in pos_clauses:
      pure_list.append(-neg_elem)

  #Final pure list (del duplicate)
  pure_list = list(set(pure_list))

 
  i = 0 
  a = 0

  # Check if the the purelist are in instance clause
  while i < len(pure_list):
    while a < len(F):
      # if they are, then pop the whole line
      if pure_list[i] in F[a]:
        F.pop(a)
        if i == 0:
          break
        else: 
          i = i - 1
      a = a + 1
    a = 0
    i = i + 1
  # Add the purelist to the instance clauses
  for elem in pure_list:
    F.append([elem])
  return pure_list


def solve(VARS, F):
  length = len(F)
  pos_x = []
  neg_x = []

  #Call functions 
  propagate_units(F)
  pure_list = pure_elim(F)

  #If there is empty clauses return []
  for i in F:
    if i == []:
      return []

  # If the final F has the same length as VARS then return F
  if len(F) == len(VARS):
    return F
  

  pos_x = copy.deepcopy(F)
  neg_x = copy.deepcopy(F)
  x = F[0][0]

  #Append positve x and negative x
  pos_x.append([x])
  neg_x.append([-x])
  solver = solve(VARS, pos_x)

  #Check what the next recursive function return
  #If return []  
  if solver != []:
    #return positive x
    return solver
  else:
    #if not , then return negative x
    nsolver = solve(VARS.copy(), neg_x)
    return nsolver


  #print (F)

  

def solve_dpll(instance, verbosity):
    #print(instance)
    #print(instance.VARS)
    #print(verbosity)
    ###########################################
    # Start your code
    

    solution = solve(instance.VARS, instance.clauses) 
    true_lit = []
    false_lit = []

    # If return [], UNSAT
    if solution == []:
      print("UNSAT")
    else: 
      #if False
      if not verbosity:
        print("SAT")
      else:
        #Print all the positive clauses
        print ("True Literals: ")
        for i in solution:
          if i[0] >= 0:
            true_lit.append(i)
        print (true_lit)

        #Print all the negative clauses
        print("False Literals: ")
        for a in solution:
          if a[0] < 0:
            false_lit.append(a)
        print(false_lit)
    

    #print (instance.clauses)
    # End your code
    return True
    ###########################################


if __name__ == "__main__":
   main(sys.argv[1:])
