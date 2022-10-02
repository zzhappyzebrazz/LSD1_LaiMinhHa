def read_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

def read_report_file(filename):
    f = open(filename, "r")
    content = str(f.read())
    f.close()
    lines = content.count('\n') + 1
    words = content.count(' ') + lines
    chars = len(content) + 1
    return lines, words, chars