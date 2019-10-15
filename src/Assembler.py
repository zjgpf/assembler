from Parser import Parser
from Code import Code
import sys
import os
import pdb

DEFAULTPATH='/Users/pengfeigao/git/assembler/test/add/Add.asm'

class Assembler:
    def __init__(self, inputPath):
        with open(inputPath, 'r') as f:
            self.content = f.readlines()
        fileName = inputPath.split('/')[-1][:-3]
        outputName = fileName+'.hack'
        self.outputPath = inputPath.replace(fileName+'.asm', outputName)
        self.hackCmds = []

    def run(self, isWrite=False):
        parser = Parser(self.content)
        hackCmds = self.hackCmds
        asmCmds = parser.asmCmds
        print(asmCmds)

        for asmCmd in asmCmds:
            commandType = parser.commandType(asmCmd)

            if commandType in ['A','L']: 
                symbol = parser.symbol(asmCmd)
                print('symbol:', symbol)

            elif commandType == 'C':
                dest = parser.dest(asmCmd)
                print('dest:', dest)
                comp = parser.comp(asmCmd)
                print('comp:', comp)
                jump = parser.jump(asmCmd)
                print('jump:', jump)
            
                #hackCmds += ['111'+Code.comp(comp)+Code.dest(dest)+Code.jump(jump)]
           
        if isWrite:
            with open(self.outputPath, 'w') as f:
                f.write(''.join(asmCmds))
         
        

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    assembler = Assembler(inputPath)
    assembler.run()
