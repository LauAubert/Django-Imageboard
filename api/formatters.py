import imp
from random import sample
def randomCodeGen(length,alpha=True,num=False):
    fullcode = ''
    code = ''
    if alpha: fullcode += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num: fullcode += '0123456789'
    for i in range(length):
        code += sample(fullcode,1)[0]
    return code
