class Numbers:

    def __init__(self):
        return

    def scientific(raw, sigfigs=3):
        sci = "{:e}".format(raw)
        [num, exp] = sci.split("e")
    
        num = num[:sigfigs+1] if num[0] != '-' else num[:sigfigs+2]

        sign = exp[0]
        exp = exp[1:]

        while(len(exp) != 1 and exp[0] == '0'):
            exp = exp[1:]

        if(sign == '-'):
            exp = "-" + exp

        return num + r"\times 10^{" + exp + r"}"
