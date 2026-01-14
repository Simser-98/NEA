from math import *




class matrix():
    def __init__(self):
        self.angle = radians(0)
        self.projection = [[1, 0, 0],
                           [0, 1, 0]]
        self.rot_x = ([[1, 0, 0],
                       [0, cos(self.angle), -sin(self.angle)],
                       [0, sin(self.angle), cos(self.angle)],])

        self.rot_y = ([[cos(self.angle), 0, sin(self.angle)],
                       [0, 1, 0],
                       [-sin(self.angle), 0, cos(self.angle)]])
        self.track_pos = (0,0)

    @staticmethod
    def Rotate_X(matrix, angle):

        angle = angle
        # Define the rotation matrix as a nested list
        rot_x = [
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ]

        # Preallocate the result as a list of lists
        result = [[0.0, 0.0, 0.0] for _ in range(len(matrix))]

        # Perform matrix multiplication
        for i in range(len(matrix)):
            result[i][0] = (
                    rot_x[0][0] * matrix[i][0]
                    + rot_x[0][1] * matrix[i][1]
                    + rot_x[0][2] * matrix[i][2]
            )
            result[i][1] = (
                    rot_x[1][0] * matrix[i][0]
                    + rot_x[1][1] * matrix[i][1]
                    + rot_x[1][2] * matrix[i][2]
            )
            result[i][2] = (
                    rot_x[2][0] * matrix[i][0]
                    + rot_x[2][1] * matrix[i][1]
                    + rot_x[2][2] * matrix[i][2]
            )

        return result


    @staticmethod
    def Rotate_Y(matrix, angle):
        # Define the rotation matrix as a nested list
        angle = -angle
        rot_y = [
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ]

        # Preallocate the result as a list of lists
        result = [[0.0, 0.0, 0.0] for _ in range(len(matrix))]

        # Perform matrix multiplication
        for i in range(len(matrix)):
            result[i][0] = (
                    rot_y[0][0] * matrix[i][0]
                    + rot_y[0][1] * matrix[i][1]
                    + rot_y[0][2] * matrix[i][2]
            )
            result[i][1] = (
                    rot_y[1][0] * matrix[i][0]
                    + rot_y[1][1] * matrix[i][1]
                    + rot_y[1][2] * matrix[i][2]
            )
            result[i][2] = (
                    rot_y[2][0] * matrix[i][0]
                    + rot_y[2][1] * matrix[i][1]
                    + rot_y[2][2] * matrix[i][2]
            )

        return result

"""def project_vertex(vertex):
# Project 3D vertex to 2D screen coordinates 
scale = 100 / vertex[2]  # Simple perspective projection
x = int(vertex[0] * scale) + 400
y = int(-vertex[1] * scale) + 300
return (x, y)"""





'''def Rotate_X(self, matrix, angle):
#self.angle += 0.01
#self.angle = pg.mouse.get_pos()[1]/100
self.angle = angle
self.rot_x = ([[1, 0, 0],
               [0, cos(self.angle), -sin(self.angle)],
               [0, sin(self.angle), cos(self.angle)],])
rotList = []
tempList = []
for i in range(len(matrix)):
    result_x = (self.rot_x[0][0] * matrix[i][0])+(self.rot_x[0][1]*matrix[i][1])+(self.rot_x[0][2]*matrix[i][2])
    result_y = (self.rot_x[1][0] * matrix[i][0])+(self.rot_x[1][1]*matrix[i][1])+(self.rot_x[1][2]*matrix[i][2])
    result_z = (self.rot_x[2][0] *matrix[i][0])+(self.rot_x[2][1] *matrix[i][1])+(self.rot_x[2][2] *matrix[i][2])
    tempList.append(result_x)
    tempList.append(result_y)
    tempList.append(result_z)
for i in range(len(tempList) // 3):
    tempTemp = []
    for j in range(3):
        tempTemp.append(tempList[0])
        del tempList[0]
    rotList.append(tempTemp)
matrix = rotList
return matrix

def Rotate_Y(self, matrix, angle):
#self.angle += 0.01
#self.angle = pg.mouse.get_pos()[0] / 100
self.angle = -angle
self.rot_y = ([[cos(self.angle), 0, sin(self.angle)],
               [0, 1, 0],
               [-sin(self.angle), 0, cos(self.angle)]])


rotList = []
tempList = []
for i in range(len(matrix)):
    result_x = (self.rot_y[0][0] * matrix[i][0]) + (self.rot_y[0][1] * matrix[i][1]) + (self.rot_y[0][2] * matrix[i][2])
    result_y = (self.rot_y[1][0] * matrix[i][0]) + (self.rot_y[1][1] * matrix[i][1]) + (self.rot_y[1][2] * matrix[i][2])
    result_z = (self.rot_y[2][0] * matrix[i][0]) + (self.rot_y[2][1] * matrix[i][1]) + (self.rot_y[2][2] * matrix[i][2])
    tempList.append(result_x)
    tempList.append(result_y)
    tempList.append(result_z)
for i in range(len(tempList) // 3):
    tempTemp = []
    for j in range(3):
        tempTemp.append(tempList[0])
        del tempList[0]
    rotList.append(tempTemp)
matrix = rotList
return matrix'''



'''for i in range(len(tempList)):
    temptemp.append(tempList[i])
    temptemp.append(tempList[i+1])
    temptemp.append(tempList[i+2])'''''








'''for i in range(len(tempList)//3 - 3):
    for j in range(3):
        print(i + j)
        rotList.append(tempList[j])
        del tempList[j]
print(rotList)'''






'''for index_row, row in enumerate(matrix):
    for index_col, col in enumerate(row):
        result += self.rot_x[index_row%3][index_col] * col
        print(result)'''




'''for i in range(0, len(matrix) + 1, 3):
    for j in range(3):
        result = 0
        try:
            result += matrix[i + j][0] * self.rot_x[0][j]
            rotList.append(result)
        except:
            print("Heheheheha")
print(rotList)'''
