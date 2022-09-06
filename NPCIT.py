import math
import os


def spaces(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def maxstartpoint(g):
    height = []
    for j in g:
        height.append(j.location['Z'])

    return height.index(max(height))


def getspacing(a, b, c, d, e, f):
    return round(math.sqrt(pow(d - a, 2) + pow(e - b, 2) + pow(f - c, 2)), 7)


class Allvertex:
    def __init__(self, x, y, z, id):
        self.location = {'X': x, 'Y': y, 'Z': z}
        self.id = id
        self.chgLocation = {}

    def chgMethod(self, apex, d1, d2):
        o1 = {}
        o2 = {}
        if g.verList[apex].location['X'] == self.location['X']:
            return False
        k1 = (g.verList[apex].location['Y'] - self.location['Y']) / (g.verList[apex].location['X'] - self.location['X'])
        b1 = g.verList[apex].location['Y'] - k1 * g.verList[apex].location['X']
        k2 = (g.verList[d1].location['Y'] - g.verList[d2].location['Y']) / (g.verList[d1].location['X'] - g.verList[d2].location['X'])
        b2 = g.verList[d1].location['Y'] - k2 * g.verList[d1].location['X']
        l1 = spaces(g.verList[apex].location['X'], g.verList[apex].location['Y'], self.location['X'],self.location['Y'])
        l3 = spaces(g.verList[d1].location['X'], g.verList[d1].location['Y'], g.verList[d2].location['X'], g.verList[d2].location['Y'])
        l4 = spaces(g.verList[d1].chgLocation['X'], g.verList[d1].chgLocation['Y'], g.verList[d2].chgLocation['X'],g.verList[d2].chgLocation['Y'])
        o1['X'] = (b2 - b1) / (k1 - k2)
        o1['Y'] = k1 * o1['X'] + b1
        l2 = spaces(g.verList[d1].location['X'], g.verList[d1].location['Y'], o1['X'], o1['Y'])
        l6 = spaces(g.verList[apex].location['X'], g.verList[apex].location['Y'], o1['X'], o1['Y'])
        l5 = (l2 * l4) / l3
        o2['X'] = g.verList[d1].chgLocation['X'] + (l5 / l4) * (g.verList[d2].chgLocation['X'] - g.verList[d1].chgLocation['X'])
        o2['Y'] = g.verList[d1].chgLocation['Y'] + (l5 / l4) * (g.verList[d2].chgLocation['Y'] - g.verList[d1].chgLocation['Y'])
        l7 = spaces(g.verList[apex].chgLocation['X'], g.verList[apex].chgLocation['Y'], o2['X'], o2['Y'])
        l8 = (l1 * l7) / l6
        self.chgLocation['X'] = g.verList[apex].chgLocation['X'] + (l8 / l7) * (o2['X'] - g.verList[apex].chgLocation['X'])
        self.chgLocation['Y'] = g.verList[apex].chgLocation['Y'] + (l8 / l7) * (o2['Y'] - g.verList[apex].chgLocation['Y'])
        self.chgLocation['Z'] = self.location['Z']


class All:
    def __init__(self):
        self.allList = {}
        self.allNum = 0

    def addAllvertex(self, x, y, z):
        self.allNum = self.allNum + 1
        newAllvertex = Allvertex(x, y, z, self.allNum)
        self.allList[self.allNum] = newAllvertex

    def __iter__(self):
        return iter(self.allList.values())


class Vertex:
    def __init__(self, key, x, y, z):
        self.id = key
        self.location = {'X': x, 'Y': y, 'Z': z}
        self.ctoLocation = {}
        self.chgLocation = {}
        self.cto = set()

    def transMethod(self):
        for key in self.cto:
            ctoX = g.verList[key].location['X']
            ctoY = g.verList[key].location['Y']
            ctoZ = g.verList[key].location['Z']
            discto = getspacing(self.location['X'], self.location['Y'], self.location['Z'], ctoX, ctoY, ctoZ)
            temlocation = {}
            if ctoY == self.location['Y'] and ctoX > self.location['X']:
                temlocation['X'] = round(discto + self.location['X'], 7)
                temlocation['Y'] = round(self.location['Y'], 7)
                continue
            elif ctoY == self.location['Y'] and ctoX < self.location['X']:
                temlocation['X'] = round(self.location['X'] - discto, 7)
                temlocation['Y'] = round(self.location['Y'], 7)
                continue
            radian = math.atan(abs((ctoX - self.location['X']) / (ctoY - self.location['Y'])))
            if ctoX >= self.location['X'] and ctoY >= self.location['Y']:
                temlocation['X'] = round(discto * math.sin(radian) + self.location['X'], 7)
                temlocation['Y'] = round(discto * math.cos(radian) + self.location['Y'], 7)
            elif ctoX <= self.location['X'] and ctoY >= self.location['Y']:
                temlocation['X'] = round(self.location['X'] - discto * math.sin(radian), 7)
                temlocation['Y'] = round(discto * math.cos(radian) + self.location['Y'], 7)
            elif ctoX >= self.location['X'] and ctoY <= self.location['Y']:
                temlocation['X'] = round(discto * math.sin(radian) + self.location['X'], 7)
                temlocation['Y'] = round(self.location['Y'] - discto * math.cos(radian), 7)
            elif ctoX <= self.location['X'] and ctoY <= self.location['Y']:
                temlocation['X'] = round(self.location['X'] - discto * math.sin(radian), 7)
                temlocation['Y'] = round(self.location['Y'] - discto * math.cos(radian), 7)

            self.ctoLocation[key] = temlocation


class Graph:
    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    def addVertex(self, x, y, z):
        newVertex = Vertex(self.numVertices, x, y, z)
        self.verList[self.numVertices] = newVertex
        self.numVertices = self.numVertices + 1
        return newVertex

    def __iter__(self):
        return iter(self.verList.values())


g = Graph()
start = 0
end = 3
data = open(r'C:\Users\xinxin\Desktop\20mmesh.txt', 'r')
vertexfile = open(r'C:\Users\xinxin\Desktop\20mProximity.txt', 'r')
floder = r"C:\Users\xinxin\Desktop\20mpointcloud"
lines = data.readlines()[1:]
vertexdata = vertexfile.readlines()[1:]
vertexdata1 = []

for line in lines:
    information = [float(x) for x in line.split()][1:4]
    g.addVertex(information[0], information[1], information[2])

for line1 in vertexdata:
    trivertex0 = [int(x) for x in line1.split()]
    vertexdata1.append(trivertex0[1])

while end <= len(vertexdata1):
    trivertex = vertexdata1[start:end]
    g.verList[trivertex[0]].cto.update({trivertex[1], trivertex[2]})
    g.verList[trivertex[1]].cto.update({trivertex[0], trivertex[2]})
    g.verList[trivertex[2]].cto.update({trivertex[0], trivertex[1]})
    start += 3
    end += 3

for i in g:
    i.transMethod()

startpoint = maxstartpoint(g)
g.verList[startpoint].chgLocation = g.verList[startpoint].location
test = []

for point in g.verList[startpoint].ctoLocation:
    g.verList[point].chgLocation = g.verList[startpoint].ctoLocation[point]
    g.verList[point].chgLocation['Z'] = g.verList[point].location['Z']
    test.append(point)

for m in test:
    for dot, loc in g.verList[m].ctoLocation.items():
        if g.verList[dot].chgLocation:
            continue
        else:
            g.verList[dot].chgLocation['X'] = round(g.verList[m].chgLocation['X'] + g.verList[m].ctoLocation[dot]['X'] - g.verList[m].location['X'], 7)
            g.verList[dot].chgLocation['Y'] = round(g.verList[m].chgLocation['Y'] + g.verList[m].ctoLocation[dot]['Y'] - g.verList[m].location['Y'], 7)
            g.verList[dot].chgLocation['Z'] = g.verList[dot].location['Z']
        test.append(dot)

# nnn = open("",'w')
#
# nnn.write('ID''\t''X1''\t''Y1''\t''Z1''\t''X''\t''Y''\t''Z')
# nnn.write('\n')
#
# for d in g:
#     nnn.write(str(d.id)+'\t')
#     for key,value in d.chgLocation.items():
#         nnn.write(str(value)+'\t')
#     nnn.write(str(d.location['X'])+'\t'+str(d.location['Y'])+'\t'+str(d.location['Z']))
#     nnn.write('\n')
#
# nnn.close()

with open("C:\\Users\\xinxin\\Desktop\\ITLiDAR2.txt", "w") as abstract:
    so = os.listdir(floder)
    so.sort(key=lambda x: int(x[:-13]))
    start = 0
    end = 2

    for file in so:
        p = All()
        file_name = floder + "\\" + file
        print(file_name)
        filein = open(file_name, "r")
        fileindata = filein.readlines()[1:]

        for line2 in fileindata:
            information = [float(x) for x in line2.split()]
            p.addAllvertex(information[0], information[1], information[2])

        for ts in p:
            iferror = ts.chgMethod(vertexdata1[start],vertexdata1[start+1],vertexdata1[end])
            if iferror == False:
                continue
            abstract.write(str(ts.chgLocation['X'])+'\t'+str(ts.chgLocation['Y'])+'\t'+str(ts.chgLocation['Z']))
            abstract.write('\n')

        start += 3
        end += 3
        del p
        break

