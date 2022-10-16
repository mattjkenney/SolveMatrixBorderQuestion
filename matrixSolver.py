class Matrix_():

    def __init__(
        self,
        matrix=[[]]
        ):

        self.matrix = matrix

    def num_rows(self):
        return len(self.matrix)

    def num_columns(self):
        return len(self.matrix[0])

class element(Matrix_):

    def __init__(
        self,
        row,
        column,
        matrix,
        is_island = True
        ):

        super().__init__(matrix)
        self.row = row
        self.column = column
        self.is_island = is_island

    def is_border(self):
        if self.row in (0, self.num_rows() - 1) or \
           self.column in (0, self.num_columns() - 1):
            b = True
        else:
            b = False
        return b

    def value(self):
        return self.matrix[self.row][self.column]

    def value_is_1(self):
        if self.value() == 1:
            b = True
        else:
            b = False
        return b

    def distance(self, elm):
        return ((self.row - elm.row)**2 + (self.column - elm.column)**2)**0.5

def dist(an_elm, elements):
    i_s = []
    for i in elements:
        if an_elm.distance(i) == 1 and i.is_island == True:
            i.is_island = False
            i_s.append(i)
    return i_s

def solve(Matrix):
    m = Matrix_(Matrix)
    elements = []
    for i in range(m.num_rows()):
        for j in range(m.num_columns()):
            e = element(i, j, m.matrix)
            if e.value_is_1():
                elements.append(e)

    for elm in elements:
        if elm.is_border():
            elm.is_island = False
            nss = dist(elm, elements)
            while len(nss) > 0:
                ns = dist(nss[0], elements)
                nss.pop(0)
                nss = nss + ns

    for e in elements:
        if e.is_island:
            Matrix[e.row][e.column] = 0

    for row in Matrix:
        print(row)

    return Matrix
