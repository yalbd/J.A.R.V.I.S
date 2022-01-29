import os
def main(txt):
    txt = txt.replace("...", "")
    txt = txt.replace("opening the app ", "")
    os.system(txt)
