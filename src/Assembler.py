from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys
import os
import pdb

DEFAULTPATH='/Users/pengfeigao/git/assembler/test/add/Add.asm'
DEFAULTPATH='/Users/pengfeigao/git/assembler/test/max/MaxL.asm'
DEFAULTPATH='/Users/pengfeigao/git/assembler/test/pong/PongL.asm'
DEFAULTPATH='/Users/pengfeigao/git/assembler/test/Rect/RectL.asm'
DEFAULTPATH='/Users/pengfeigao/git/assembler/test/max/Max.asm'
#DEFAULTPATH='/Users/pengfeigao/git/assembler/test/Rect/Rect.asm'

class Assembler:
    def __init__(self, inputPath):
        with open(inputPath, 'r') as f:
            self.content = f.readlines()
        fileName = inputPath.split('/')[-1][:-4]
        outputName = fileName+'.hack'
        self.outputPath = inputPath.replace(fileName+'.asm', outputName)
        self.hackCmds = []

    def run(self, isWrite=True):
        parser = Parser(self.content)
        symbolTable = SymbolTable()
        hackCmds = self.hackCmds
        asmCmds = parser.asmCmds
        print(asmCmds)

        lineNum = 0
        for asmCmd in asmCmds:
            commandType = parser.commandType(asmCmd)
            if commandType == 'L':
                symbol = parser.symbol(asmCmd)
                symbolTable.addEntry(symbol, lineNum+1)
            else: lineNum += 1

        ramNo = 16
        for asmCmd in asmCmds:
            commandType = parser.commandType(asmCmd)

            if commandType in ['A','L']:
                symbol = parser.symbol(asmCmd)
                if symbolTable.contains(symbol):
                    address = symbolTable.getAddress(symbol)
                else:
                    symbolTable.addEntry(symbol,ramNo)
                    address = ramNo
                    ramNo+=1
                hackCmds += ['0'+decimalToBinary15(address)+ '\n']
            elif commandType == 'C':
                dest = parser.dest(asmCmd)
                print('dest:', dest)
                print('code dest',Code.dest(dest))
                comp = parser.comp(asmCmd)
                print('comp:', comp)
                print('code comp',Code.comp(comp))
                jump = parser.jump(asmCmd)
                print('jump:', jump)
                print('code jump',Code.dest(jump))
            
                hackCmds += ['111'+Code.comp(comp)+Code.dest(dest)+Code.jump(jump)+'\n']
        print(hackCmds)
        print(self.outputPath)
           
        if isWrite:
            with open(self.outputPath, 'w') as f:
                f.write(''.join(hackCmds))
         
def decimalToBinary15(decimal):
    decimal = int(decimal)
    binArr = []
    while decimal:
        reminder = decimal%2
        binArr.append(str(reminder))
        decimal = int(decimal/2)
    offsetArr = ['0']*(15-len(binArr))
    ret = ''.join(offsetArr+list(reversed(binArr)))
    return ret

if __name__ == '__main__':
    args = sys.argv
    if  len(args) < 2: inputPath = DEFAULTPATH
    else: inputPath = sys.argv[1]
    assembler = Assembler(inputPath)
    assembler.run()
