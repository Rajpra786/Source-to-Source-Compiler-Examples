########################################################################################################
#                   Aim of this program : This program parse a simple script
#                                            repeat 10 p ‘hello world'
#                                       using python module Lark
#                   Author : Rajendra Prajapat
#########################################################################################################
from lark import Lark

Test_grammar = """
    start: instruction+
    instruction: "p" STRING                  -> print
               | "repeat" NUMBER block       -> repeat

    block : instruction+

    STRING : "'" (WORD " ")+ "'"
           | "'" " " (WORD " ")+ "'"
           | "'" (WORD " ")+ WORD "'"

    %import common.WORD
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(Test_grammar)



def run(t):
    if t.data == 'print':
        print(*t.children)
    elif t.data == 'repeat':
        c,block = t.children
        for i in range(int(c)):
            run(block)
    elif t.data == 'block':
        for i in t.children:
            run(i)
    else:
        raise SyntaxError('Unknown instruction: %s' %t.data)



#Execute the script in python using run function
def Run_Program():
    #read input from Input.test file
    file = open("Input.test", "r")
    program = file.read()

    parse_tree = parser.parse(program)
    #uncomment to see parse tree
    # print(parse_tree.pretty())
    for i in parse_tree.children:
        run(i)

Run_Program()
