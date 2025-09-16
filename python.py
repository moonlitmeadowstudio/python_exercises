def show(image):
    for line in image:
        print(line)

def enlarge(array):
    line = []
    for item in array:
        string  = str(item)
        line_str = ""
        for char in string:
            char *= 2
            line_str += char
        line.append(line_str)
        line.append(line_str)
    return line

dot = ['@']
show(enlarge(dot))
# => @@
# => @@

dot = ['##']
show(enlarge(dot))
# => @@
# => @@

frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]
show(frame)
# => ****
# => *  *
# => *  *
# => ****
show(enlarge(frame))
# => ********
# => ********
# => **    **
# => **    **
# => **    **
# => **    **
# => ********
# => ********'''