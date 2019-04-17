#!/usr/bin/python3

import sys, getopt
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
# num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
# <Your feedback goes here>
"""

"""
#####################################################
#####################################################

def main(argv):
   inputfile = ''
   N=0
   try:
      opts, args = getopt.getopt(argv,"hn:i:",["N=","ifile="])
   except getopt.GetoptError:
      print ('sudoku.py -n <size of Sodoku> -i <inputputfile>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('sudoku.py  -n <size of Sodoku> -i <inputputfile>')
           sys.exit()
       elif opt in ("-n", "--N"):
           N = int(arg)
       elif opt in ("-i", "--ifile"):
           inputfile = arg
   instance = readInstance(N, inputfile)
   toCNF(N,instance,inputfile+str(N)+".cnf")




def readInstance (N, inputfile):
    if inputfile == '':
        return [[0 for j in range(N)] for i in range(N)]
    with open(inputfile, "r") as input_file:
        instance =[]
        for line in input_file:
            number_strings = line.split() # Split the line on runs of whitespace
            numbers = [int(n) for n in number_strings] # Convert to integers
            if len(numbers) == N:
                instance.append(numbers) # Add the "row" to your list.
            else:
                print("Invalid Sudoku instance!")
                sys.exit(3)
        return instance # a 2d list: [[1, 3, 4], [5, 5, 6]]

def getCell():
  return 0
""" Question 1 """
def toCNF (N, instance, outputfile):
    """ Constructs the CNF formula C in Dimacs format from a sudoku grid."""
    """ OUTPUT: Write Dimacs CNF to output_file """
    import itertools
    n = N
    output_file = open(outputfile, "w")
    "*** YOUR CODE HERE ***"
    constraint = []
    constraint_2 = []
    constraint_3 = []
    counter = 0
    count = 0
    for i in range(N):
      for j in range(N):
        if instance [i][j] != 0:
          counter = counter + 1

    #Write the first line p cnf NNN and Line
    count = (N*N) + (N-1)*(N*N*N)*3 + counter + 1
    output_file.write("p cnf " + str(str(N)+str(N)+str(N)))
    output_file.write(" " + str(count))
    output_file.write("\n")


    #First Constraint
    for i in range(N):
      for j in range(N):
        for k in range(N):
          output_file.write(str(i+1)+str(j+1)+str(k+1)+ " ")
        output_file.write(str(0))
        output_file.write("\n")

    
    #Second Constraint
    for i in range(N):
      for j in range(N):
        for k in range(N):
          for l in range(N):
            if k != l:
              output_file.write("-"+str(i+1)+str(j+1)+str(k+1)+ " ")
              output_file.write("-"+str(i+1)+str(j+1)+str(l+1)+ " ")
              output_file.write(str(0))
              output_file.write(" ")
              output_file.write("\n")


    #Third Constraint
    for i in range(N):
      for k in range(N):
        for j1 in range(N):
          for j2 in range(N):
            if j1 != j2:
              output_file.write("-"+str(i+1)+str(j1+1)+str(k+1)+ " ")
              output_file.write("-"+str(i+1)+str(j2+1)+str(k+1)+ " ")
              output_file.write(str(0))
              output_file.write(" ")
              output_file.write("\n")
          

    #Fourth Constraint
    for j in range(N):
      for k in range(N):
        for i1 in range(N):
          for i2 in range(N):
            if i1 != i2:
              output_file.write("-"+str(i1+1)+str(j+1)+str(k+1)+ " ")
              output_file.write("-"+str(i2+1)+str(j+1)+str(k+1)+ " ")
              output_file.write(str(0))
              output_file.write(" ")
              output_file.write("\n")    


    #Fifth Constraint
    for i in range(N):
      for j in range(N):
        if instance [i][j] != 0 :
          output_file.write(str(i+1)+str(j+1))
          output_file.write(str(instance[i][j]))
          output_file.write(" ")
          output_file.write(str(0))
          output_file.write("\n")  
    "*** YOUR CODE ENDS HERE ***"
    output_file.close()





if __name__ == "__main__":
   main(sys.argv[1:])
