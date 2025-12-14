def read_lines(file, new_line):
    buf = ""
    while True:
        while new_line in buf:
            pos = buf.index(new_line)
            yield buf[:pos]
            buf = buf[pos + len(new_line):]
        chunk = file.read(4096)
        if not chunk:
            yield buf
            break
        buf += chunk


with open("big_file.txt", "r") as f:
    for line in read_lines(f, "{|}"):
        print(line)
