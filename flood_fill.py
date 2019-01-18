
def print_matrix(input_matrix):
	num_rows= len(input_matrix)
	print("********")
	for row in range(0, num_rows):
		print str(input_matrix[row])

def fill(input_matrix, x, y):
	if( (x+1) >= 0 and (x+1) <= max_x and input_matrix[x+1][y] == 0):
		input_matrix[x+1][y] = 2
		fill(input_matrix, x+1, y)
	
	if( (x-1) >= 0 and (x-1) <= max_x and input_matrix[x-1][y] == 0):
		input_matrix[x-1][y] = 2
		fill(input_matrix, x-1, y)
	
	if( (y+1) >= 0 and (y+1) <= max_y and input_matrix[x][y+1] == 0):
		input_matrix[x][y+1] = 2
		fill(input_matrix, x, y+1)		
		
	if( (y-1) >= 0 and (y-1) <= max_y and input_matrix[x][y-1] == 0):
		input_matrix[x][y-1] = 2
		fill(input_matrix, x, y-1)
		
	print_matrix(input_matrix)
	

input_matrix = [0,0,0,0]
input_matrix[0] = [0, 0, 0, 0]
input_matrix[1] = [0, 0, 0, 0]
input_matrix[2] = [0, 0, 0, 0]
input_matrix[3] = [0, 0, 0, 0]

input_matrix[0][0] = 0
input_matrix[0][1] = 0
input_matrix[0][2] = 0
input_matrix[0][3] = 1

input_matrix[1][0] = 0
input_matrix[1][1] = 1
input_matrix[1][2] = 1
input_matrix[1][3] = 1

input_matrix[2][0] = 0
input_matrix[2][1] = 2
input_matrix[2][2] = 1
input_matrix[2][3] = 1

input_matrix[3][0] = 0
input_matrix[3][1] = 0
input_matrix[3][2] = 1
input_matrix[3][3] = 1


#start_pos = find_start_position() ##this finds the position with number 2

x = 2
y = 1

max_x = len(input_matrix)-1
max_y = len(input_matrix[0])-1

print("Max x: " + str(max_x) + " Max y:" + str(max_y))

print_matrix(input_matrix)

fill(input_matrix, x, y)




