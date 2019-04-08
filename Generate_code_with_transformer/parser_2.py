########################################################################################################
#                   Aim of this program : This program parse a simple script
#                                            repeat 10 p ‘hello world'
#                                       using python module Lark and generate python code from it
#                   Author : Rajendra Prajapat
#########################################################################################################

from lark import Lark,Transformer,v_args

Test_grammar = """
    start: instruction+
    instruction: "p" STRING                  -> printf
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


class Code_generator(Transformer):
    def printf(self,args):
        return "print("+ args[0] +")"
    def repeat(self,args):
        number,block = args[0],args[1]
        list = []
        str = "for i in range(" + number +"):"
        list.append(str)
        for i in block:
            list.append(i)
        return list

    def block(self,args):
        li =[]
        inden = "    "
        for i in args:
            if isinstance(i,list):
                for inst in i:
                    str = ""
                    str = str + inden + inst
                    li.append(str)
            else:
                str = ""
                str = str + inden + i
                li.append(str)
        return li


#Execute the script in python using run function

parser = Lark(Test_grammar,parser = "lalr",transformer = Code_generator())

def Run_Program():
    #read input from Input.test file
    file = open("Input.test", "r")
    program = file.read()
    file.close()
    parse_tree = parser.parse(program)

    # print(parse_tree.pretty())
    code = ""
    x = parse_tree.children
    for i in x[0]:
        code = code + i + "\n"

    # print(code)
    file = open("output.py", "w")
    file.write(code)
    file.close()

Run_Program()
