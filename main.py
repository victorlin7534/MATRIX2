from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix1 = new_matrix(0)
matrix2 = new_matrix(0)
add_edge(matrix1,3,5,1,1,2,3)
add_edge(matrix1,5,2,3,1,5,2)
print_matrix(matrix1)
add_edge(matrix2,1,2,3,200,150,6)
add_point(matrix2,2,4,6)
add_point(matrix2,100,50,5)
print_matrix(matrix2)
matrix_mult(matrix1,matrix2)
print_matrix(matrix2)

clear_screen(screen)
matrix = new_matrix(0)
for i in range(20):
    add_edge(matrix,350,0,0,x=350 + 5*i,y=10*i,0)

draw_lines(matrix,screen,color)
save_extension(screen,"img.png")
display(screen)
