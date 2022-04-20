import pyvisa as visa
import hp33120aLib as tb
def run2(dev, cmd):
    cmd = "dev.write('" + cmd + "')"
    eval(cmd)
    return True

def run(dev, func, args):
    check = cmdCheck(func, args)
    if check[0]:
        cmd = "dev.write('" + check[3] + "')"
        eval(cmd)
    return True

def cmdCheck(func, args):
    """_summary_

    Args:
        func (string): _description_
        args (array)): space split command string

    Returns:
        _type_: _description_
    """
    line = 'tb.' + str(func)+ '.__code__.co_varnames'
    call = 'tb.' + str(func) + '(' + ', '.join(args) + ')'
    cmd = ''
    if len(args) / 2 == len(eval(line)) - 1:
        cmdArr = []
        call = 'tb.' + str(func) + '('
        for j in range(0,len(eval(line))-1):
            sub = "'" + args[2*(j % len(eval(line)))] + " " + args[2*(j % len(eval(line)))+1] + "'"
            cmdArr.append(sub)
        call = call + ', '.join(cmdArr) + ')'
        flag = True
        cmd = eval(call)
    else:
        flag = False
    return [flag, line, call, cmd]