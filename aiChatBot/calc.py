def calc(txt):
    x = ""
    y = ""
    result = 0
    if "+" in txt:
        x = txt.replace(txt[txt.index("+") - 1:], "")
        y = txt.replace(txt[:((txt.index("+") - 2) * -1)], "")
        result = int(x) + int(y)
    elif "-" in txt:
        x = txt.replace(txt[txt.index("-") - 1:], "")
        y = txt.replace(txt[:((txt.index("-") - 2) * -1)], "")
        if int(x) >= int(y):
            result = int(x) - int(y)
        else:
            result = int(y) - int(x)
    elif "*" in txt or "x" in txt:
        if "x" in txt:
            x = txt.replace(txt[txt.index("x") - 1:], "")
            y = txt.replace(txt[:((txt.index("x") - 2) * -1)], "")
        else:
            x = txt.replace(txt[txt.index("*") - 1:], "")
            y = txt.replace(txt[:((txt.index("*") - 2) * -1)], "")
        result = int(x) * int(y)
        x = txt
    elif "/" in txt or "d" in txt:
        if "/" in txt:
            x = txt.replace(txt[txt.index("/") - 1:], "")
            y = txt.replace(txt[:((txt.index("/") - 2) * -1)], "")
        else:
            x = txt.replace(txt[txt.index("d") - 1:], "")
            y = txt.replace(txt[:((txt.index("d") - 2) * -1)], "")
        if int(x) >= int(y):
            result = float(x) / float(y)
        else:
            result = float(y) / float(x)
    print(result)
