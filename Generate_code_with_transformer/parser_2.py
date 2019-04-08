#repeat 10 p ‘hello world
import turtle

from lark import Lark,Transformer,v_args

turtle_grammar = """
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
        return "for i in range(" + number +"):\n" + block
    def block(self,args):
        str = "     "
        for i in args:
            str = str +"     "+ i + "\n"
        return str


#Execute the script in python using run function

parser = Lark(turtle_grammar,parser = "lalr",transformer = Code_generator())

def Run_Program():
    #read input from Input.test file
    file = open("Input.test", "r")
    program = file.read()
    file.close()
    parse_tree = parser.parse(program)

    x=parse_tree.children
    file = open("output.py", "w")
    file.write(x[0])
    file.close()

Run_Program()
