import pdb
class Parser:
    def __init__(self, content):
        self.content = content 
        self.curContentIdx = 0
        self.curCmd = None
        self.nextCmd = None
        self.asmCmds = []
        self.parse()

    def parse(self):
        while self.hasMoreCommands():
            self.advance()
            self.asmCmds += [self.curCmd.strip()]

    def hasMoreCommands(self):
        if self.nextCmd: return True
        else:
            hasNextCmd = self.getNextCmd()
            return hasNextCmd

    def advance(self):
        self.curCmd = self.nextCmd
        self.nextCmd = None

    def getNextCmd(self):
        content = self.content
        curIdx = self.curContentIdx
        ret = False
        while curIdx < len(content):
            if content[curIdx] == '\n': 
                curIdx += 1
            elif content[curIdx][0] == '/' and content[curIdx][1] == '/':
                curIdx+=1
            else:
                instructionRaw = content[curIdx]
                curIdx+=1
                _curIdx = 0
                while _curIdx < len(instructionRaw) and instructionRaw[_curIdx] not in ['/', '\n']: _curIdx += 1
                self.nextCmd = instructionRaw[0:_curIdx]
                ret = True
                break
        self.curContentIdx = curIdx
        return ret

    @staticmethod
    def commandType(cmd):
        if cmd[0] == '@': return 'A'
        elif cmd[0] == '(': return 'L'
        else: return 'C'

    @staticmethod
    def symbol(cmd):
        if cmd[0] == '@': return cmd[1:]
        elif cmd[0] == '(': return cmd[1:-1]
        else: raise Error(f'Invalid call symbol method with {cmd}' )
                
    @staticmethod
    def dest(cmd):
        if '=' in cmd:
            return cmd.split('=')[0]
        else:
            return ''

    @staticmethod
    def jump(cmd):
        if ';' in cmd:
            return cmd.split(';')[1]
        else:
            return ''

    @staticmethod
    def comp(cmd):
        if '=' in cmd:
            cmd = cmd.split('=')[1]       
        if ';' in cmd:
            cmd = cmd.split(';')[0]
        return cmd

