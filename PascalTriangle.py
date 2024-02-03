#Printing Pascals triangle 


def pascals_triangle(height):
  
    triangle = []  

    for i in range(height):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            new_row = [1]
            last_row = triangle[-1]  
            for j in range(1, i):
                new_elem = last_row[j-1] + last_row[j]
                new_row.append(new_elem)
            new_row.append(1)
            triangle.append(new_row)

    return triangle

def Display(triangle):
    
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        formatted_row = ' '.join(map(str, row))
        print(formatted_row.center(max_width))

height = 7  
triangle = pascals_triangle(height)
Display(triangle)
