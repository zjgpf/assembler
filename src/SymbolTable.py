class SymbolTable:

    def __init__(self):
        self.table = {}
        self.predefined()

    def addEntry(self,symbol,address):
        self.table[symbol] = address

    def contains(self,symbol):
        return symbol in self.table

    def getAddress(self,symbol):
        return self.table[symbol]

    def predefined(self):
        table = self.table
        for i in range(16):
            key = 'R'+str(i)
            table[key] = i
        table['SP'] = 0
        table['LCL'] = 1
        table['ARG'] = 2
        table['THIS'] = 3
        table['THAT'] = 4
        table['SCREEN'] = 16384
        table['KBD'] = 24576
        
