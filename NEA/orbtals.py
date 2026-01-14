from config import *



class orb_vertex_pos:
    def __init__(self, path, col_line=BLACK, col_fill=BLACK):
        self._col_line = col_line
        self._col_fill = col_fill
        self._vertices = []
        self._vertices_normal = []
        self._vertices_texture = []
        self._faces = []
        self._faces_normal = []
        self._file_path = path
        self._view_vector = [0, 0, -1]
        self._visible = []
        self._angle_rel = (0,0)
        self._wire_frame = False
        self._ORIGIN = (WIN_WIDTH/2 - 40, WIN_HEIGHT/2 - 150)
        self._orb_arrangment = []
        self._orb_arrangment_short = []
        self._atom_arrangment = []


    '''def dot_prod(self):
        self.view_angle()
        print(self._view_vector)
        self._visible = []
        for i in range(len(self._faces)):
            dot_product_calc = (self._view_vector[0] * self._vertices_normal[self._faces_normal[i][0] - 1][0] +
                              self._view_vector[1] * self._vertices_normal[self._faces_normal[i][1] - 1][1] +
                              self._view_vector[2] * self._vertices_normal[self._faces_normal[i][2] - 1][2])
            self._visible.append(dot_product_calc < 0)'''


    def angle_set(self, angle_rel):
        self._angle_rel = angle_rel

    """"def view_angle(self):
        rot = matrix()
        if self._angle_rel != (0,0):
            rotX = rot.Rotate_X([self._view_vector], self._angle_rel[0])
            rotY = rot.Rotate_Y(rotX, self._angle_rel[1])
            self._view_vector = rotY[0]"""


    def Vert_load(self):
        try:
            with open(self._file_path, 'r') as f:
                for line in f:
                    if line[0:2] == "v ":
                        vertex = list(map(float, line[2:].strip().split()))                                          # takes the list of value added it to the final list and clears its self
                        self._vertices.append(vertex)
                    if line[0:2] == "vn":
                        vertex_normal = list(map(float, line[2:].strip().split()))
                        self._vertices_normal.append(vertex_normal)
                    if line[0:2] == "vt":
                        vertex_texture = list(map(float, line[2:].strip().split()))
                        self._vertices_texture.append(vertex_texture)
                    if line[0] == "f":
                        face_pre = list(map(int, line[2:].replace("/", " ").strip().split()))
                        face = []
                        face_normal = []
                        for i in range(0, len(face_pre), 3):
                            face.append(face_pre[i])
                            face_normal.append(face_pre[i + 2])
                        self._faces.append(face)
                        self._faces_normal.append(face_normal)
        except:
            with open("_internal/" + self._file_path, 'r') as f:
                for line in f:
                    if line[0:2] == "v ":
                        vertex = list(map(float, line[2:].strip().split()))                                          # takes the list of value added it to the final list and clears its self
                        self._vertices.append(vertex)
                    if line[0:2] == "vn":
                        vertex_normal = list(map(float, line[2:].strip().split()))
                        self._vertices_normal.append(vertex_normal)
                    if line[0:2] == "vt":
                        vertex_texture = list(map(float, line[2:].strip().split()))
                        self._vertices_texture.append(vertex_texture)
                    if line[0] == "f":
                        face_pre = list(map(int, line[2:].replace("/", " ").strip().split()))
                        face = []
                        face_normal = []
                        for i in range(0, len(face_pre), 3):
                            face.append(face_pre[i])
                            face_normal.append(face_pre[i + 2])
                        self._faces.append(face)
                        self._faces_normal.append(face_normal)

        return self._vertices, self._vertices_normal, self._vertices_texture, self._faces

        # print(len(self._vertices), len(self._vertices_normal))
        # print(self._faces)
    # print(measure_index)
    # print(self._vertices)
    # print(self._faces)
    # for line in self._vertices:
    #   print(line)

    def Atom_load(self):
        try:
            with open(self._file_path, 'r', encoding="utf8") as a:
                for line in a:
                    if line[0:30] == "Electron Orbital Arrangement: ":
                        orbArrange = line[30:].strip()
                        self._orb_arrangment.append(orbArrange)
                    if line[0:32] == "Shorthand Electron Arrangement: ":
                        shortOrbArrange = line[32:].strip()
                        self._orb_arrangment_short.append(shortOrbArrange)
                    if line[0:18] == "Atom Arrangement: ":
                        atomArrange = line[18:].strip()
                        self._atom_arrangment.append(atomArrange)
        except:
            with open("_internal/" + self._file_path, 'r', encoding="utf8" ) as a:
                for line in a:
                    if line[0:30] == "Electron Orbital Arrangement: ":
                        orbArrange = line[30:].strip()
                        self._orb_arrangment.append(orbArrange)
                    if line[0:32] == "Shorthand Electron Arrangement: ":
                        shortOrbArrange = line[32:].strip()
                        self._orb_arrangment_short.append(shortOrbArrange)
                    if line[0:18] == "Atom Arrangement: ":
                        atomArrange = line[18:].strip()
                        self._atom_arrangment.append(atomArrange)

        return self._orb_arrangment, self._orb_arrangment_short, self._atom_arrangment


    def Key_toggle_on_f(self):
        key = pg.key.get_pressed()
        if not self._wire_frame and key[pg.K_f]:
            toggle = True
        #elif self._wire_frame and key[pg.K_f]:
         #   toggle = False
        elif not self._wire_frame:
            toggle = False
        else:
            toggle = True
        self._wire_frame = toggle
        return toggle

    def Key_toggle_off_r(self):
        key = pg.key.get_pressed()
        if self._wire_frame and key[pg.K_r]:
            toggle = False
        elif not self._wire_frame:
            toggle = False
        else:
            toggle = True
        self._wire_frame = toggle
        return toggle

    def draw_polygon_alpha(self, color, points):
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        target_rect = pg.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        shape_surf = pg.Surface(target_rect.size, pg.SRCALPHA)
        pg.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
        Window.blit(shape_surf, target_rect)


    def Draw_node(self, matrix, faces, scale_factor, ):
        #pass
        toggle = False
        toggleOn = self.Key_toggle_on_f()
        toggle = toggleOn
        toggleOff = self.Key_toggle_off_r()
        toggle = toggleOff
        lowest, highest = 0, 0
        for i in matrix:
            if i[2] > highest:
                highest = i[2]
            elif i[2] < lowest:
                lowest = i[2]

        '''for i in matrix:
            colour = (21 * ((i[2] + abs(lowest)) / (abs(lowest) * 3)),
                      162 * ((i[2] + abs(lowest)) / (abs(lowest) * 3)),
                      232 * ((i[2] + abs(lowest)) / (abs(lowest) * 3)))'''

        for index, face in enumerate(faces):
            pass
            if len(face) == 3:
                if toggle:
                    pg.draw.polygon(Window, self._col_line
                                    , (
                        (matrix[face[0] - 1][0] * scale_factor + self._ORIGIN[0], matrix[face[0] - 1][1] * scale_factor + self._ORIGIN[1]),
                        (matrix[face[1] - 1][0] * scale_factor + self._ORIGIN[0], matrix[face[1] - 1][1] * scale_factor + self._ORIGIN[1]),
                        (matrix[face[2] - 1][0] * scale_factor + self._ORIGIN[0], matrix[face[2] - 1][1] * scale_factor + self._ORIGIN[1])), 1)
                if not toggle:
                    self.draw_polygon_alpha( self._col_fill, (
                        (matrix[face[0] - 1][0] * scale_factor + self._ORIGIN[0],matrix[face[0] - 1][1] * scale_factor + self._ORIGIN[1]),
                        (matrix[face[1] - 1][0] * scale_factor + self._ORIGIN[0], matrix[face[1] - 1][1] * scale_factor + self._ORIGIN[1]),
                        (matrix[face[2] - 1][0] * scale_factor + self._ORIGIN[0], matrix[face[2] - 1][1] * scale_factor + self._ORIGIN[1])))







        """toggleKey = pg.key.get_pressed()

                if toggleKey[pg.K_f]:
                    self._wire_frame = True
                else:
                    self._wire_frame = False"""


#if 1:
#if self._visible[index]:

            #pg.draw.circle(Window, self._col_line,
            #               (i[0] * self._scale_factor + WIN_WIDTH / 2, i[1] * self._scale_factor + WIN_HEIGHT / 2), 3)


"""                else:
                    #pg.draw.polygon(Window, self._col_line
                     #               , (
                      #  (matrix[face[0] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[0] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                       # (matrix[face[1] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[1] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                        #(matrix[face[2] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[2] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                        #(matrix[face[3] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[3] - 1][1] * self._scale_factor + WIN_HEIGHT / 2)), 1)
                    self.draw_polygon_alpha( self._col_fill, (
                        (matrix[face[0] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[0] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                        (matrix[face[1] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[1] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                        (matrix[face[2] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[2] - 1][1] * self._scale_factor + WIN_HEIGHT / 2),
                        (matrix[face[3] - 1][0] * self._scale_factor + WIN_WIDTH / 2, matrix[face[3] - 1][1] * self._scale_factor + WIN_HEIGHT / 2)))"""


'''  def Bubble_Sort(self):
        for j in len(self._vertices):
            for i in len(self._vertices) - 1:
                if self._vertices[i][2] > self._vertices[i+1][2]:     #  15 > 14
                    temp = self._vertices[i][2]   #  15 = temp
                    self._vertices[i+1][2] = self._vertices[i][2]    # 14
                    self._vertices[i+1][2] = temp    # 15 = temp
        print(self._vertices)
        return self._vertices '''


"""for j in range(len(self._vertices)):
                for i in range(len(self._vertices) - 1):
                    if self._vertices[i][2] > self._vertices[i + 1][2]:
                        #print(self._vertices[i][2])
                        #print(self._vertices[i + 1][2])
                        smal_list = self._vertices[i]
                        big_list = self._vertices[i + 1]
                        self._vertices[i + 1] = smal_list
                        self._vertices[i] = big_list
                        for n in range(3):
                            for m in range(len(self._faces)):
                                # check the condition
                                if (self._faces[m][n] == i +1):
                                    self._faces[m][n] = int(i + 2)

                                elif (self._faces[m][n] == i + 2):
                                    self._faces[m][n] = int(i+1)
                                                        else:
                        pass"""

"""measure_index = []
            for i in range(len(self._faces)):
                measure_index.append(min(self._faces[i]))

            for j in range(len(self._faces)):
                for i in range(len(self._faces) - 1):
                    if measure_index[i] > measure_index[i + 1]:
                        #print(self._vertices[i][2])
                        #print(self._vertices[i + 1][2])
                        smal_list = self._faces[i]
                        big_list = self._faces[i + 1]
                        self._faces[i + 1] = smal_list
                        self._faces[i] = big_list

                        smal_ind = measure_index[i]
                        big_ind = measure_index[i + 1]
                        measure_index[i + 1] = smal_ind
                        measure_index[i] = big_ind"""

"""def quicksort(self, messy_v, index_list):
        if len(messy_v) < 2:
            return messy_v, index_list

        low, same, high = [], [], []

        low_index, same_index, high_index = [], [], []

        # Select your `pivot` element randomly
        pivot = messy_v[randint(0, len(messy_v) - 1)][2]

        for i in range(len(messy_v)):
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.

            if messy_v[i][2] < pivot:
                low.append(messy_v[i])
                low_index.append(i)
            elif messy_v[i][2] == pivot:
                same.append(messy_v[i])
                same_index.append((i))
            elif messy_v[i][2] > pivot:
                high.append(messy_v[i])
                high_index.append(i)"""

       # low_v, low_index = self.quicksort(low, low_index)
        #high_v, high_index = self.quicksort(high, high_index)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
       # return low + same + high, low_index + same_index + high_index
    # self._vertices, vert_indexes = self.quicksort(self._vertices, [i for i in range(len(self._vertices))])

""" def Draw_node(self ,faces, transformed_vertices, vertex_normals):
         #Determine if a face is visible using averaged vertex normals
        # Average the vertex normals of the face to approximate the face normal
        print(faces)
        print(transformed_vertices)
        print(vertex_normals)
        normals = [vertex_normals[faces[i]] for i in range(3)]
        normal = [
            sum(normals[i][j] for i in range(3)) / 3 for j in range(3)
        ]

        # View direction is towards the camera, along the Z-axis
        view_direction = [0, 0, -1]

        # Dot product of normal and view direction
        dot_product = sum(normal[i] * view_direction[i] for i in range(3))

        # If the dot product is less than 0, the face is visible
        #return dot_product < 0

        # Draw only visible faces
        for face in faces:
            if Draw_node(faces, transformed_vertices, vertex_normals):
                points = [project_vertex(transformed_vertices[face[i]]) for i in range(3)]
                pg.draw.polygon(Window, (100, 150, 200), points, 1)

            # If the dot product is less than 0, the face is visible
            return dot_product < 0"""