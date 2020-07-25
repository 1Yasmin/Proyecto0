from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
# import your parser & lexer here
from DecafLexer import *
from DecafParser import *

def createTree(inp_val):
    lexer = DecafLexer(inp_val)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()

    print((Trees.toStringTree(tree, None, parser)))