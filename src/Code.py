class Code:

    @staticmethod
    def comp(cmd):
        if 'M' in cmd: a = '1'
        else: a = '0'
        cmd = cmd.replace('M','A')
        ret = ''
        if cmd == '0': ret = '101010'
        elif cmd  == '1': ret = '111111' 
        elif cmd  == '-1': ret = '111010' 
        elif cmd  == 'D': ret = '001100' 
        elif cmd  == '!D': ret = '001101' 
        elif cmd  == '-D': ret = '001111' 
        elif cmd  == 'D+1': ret = '011111' 
        elif cmd  == 'D-1': ret = '001110' 
        elif cmd  == 'A': ret = '110000' 
        elif cmd  == '!A': ret = '110001' 
        elif cmd  == '-A': ret = '110011' 
        elif cmd  == 'A+1': ret = '110111' 
        elif cmd  == 'A-1': ret = '110010' 
        elif cmd  == 'D+A': ret = '000010' 
        elif cmd  == 'D-A': ret = '010011' 
        elif cmd  == 'A-D': ret = '000111' 
        elif cmd  == 'D&A': ret = '000000' 
        elif cmd  == 'D|A': ret = '010101' 
        return a + ret
        

    @staticmethod
    def dest(cmd):
        ret = [0,0,0]
        if 'A' in cmd: ret[0] = 1
        if 'D' in cmd: ret[1] = 1
        if 'M' in cmd: ret[2] = 1
        return ''.join([str(v) for v in ret])

    @staticmethod
    def jump(cmd):
        if not cmd: return '000'
        elif cmd == 'JGT': return '001'
        elif cmd == 'JEQ': return '010'
        elif cmd == 'JGE': return '011'
        elif cmd == 'JLT': return '100'
        elif cmd == 'JNE': return '101'
        elif cmd == 'JLE': return '110'
        elif cmd == 'JMP': return '111'
