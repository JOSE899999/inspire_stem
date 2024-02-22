def print_box(width, height):
    horizontal_border = " + " + " - " * (width - 2)+ '+'
    inner_space = ' | ' + ' ' * ( width + 2) +'|'

    print(horizontal_border)
    for _ in range( height - 2):
        print(inner_space)
        print(horizontal_border)

print_box(25, 20)