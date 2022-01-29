import webbrowser

def main(res):
    x = res.replace("opening", "")
    y = x.replace("...", "")
    z = y.replace(" ", "")
    if z == "calendar":
        webbrowser.open_new('https://calendar.google.com')
    else:
        webbrowser.open_new('https://' + z + '.com')

def search(txt):
    new_txt = txt.replace(" ", "+")
    new_x = new_txt.replace("search", "")
    webbrowser.open_new('https://google.com/search?q=' + new_x)
