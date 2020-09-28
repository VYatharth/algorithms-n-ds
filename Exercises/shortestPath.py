class UserMainCode(object):
    path = 0
    @classmethod
    def GetMinAnts(cls,input1,input2,input3):
        graph=[ [0] * input1 for _ in range(input1)]
        for i in range(input1):
            for j in range(i,input1):
                graph[i][j] = abs(input2[i][0] - input2[j][0]) + abs(input2[i][1] - input2[j][1])
                graph[j][i] = graph[i][j]

        UserMainCode.getMinPath(graph,input1)
        return int((UserMainCode.path * 100) / input3)

    @staticmethod
    def getMinPath(G,V): #using Prim's algo here
        INF = 9999999

        selected = [0] * V
        # set number of edge to 0
        no_edge = 0
        selected[0] = True
        while (no_edge < V - 1):
            # For every vertex in the set S, find the all adjacent vertices
            #, calculate the distance from the vertex selected at step 1.
            # if the vertex is already in the set S, discard it otherwise
            # choose another vertex nearest to selected vertex  at step 1.
            minimum = INF
            x = 0
            y = 0
            for i in range(V):
                if selected[i]:
                    for j in range(V):
                        if ((not selected[j]) and G[i][j]):  
                            # not in selected and there is an edge
                            if minimum > G[i][j]:
                                minimum = G[i][j]
                                x = i
                                y = j
            print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
            UserMainCode.path +=G[x][y]
            selected[y] = True
            no_edge += 1


# number of vertices in graph


#G = [[0, 2, 4],
#     [2, 0, 2],
#     [4, 2, 0]]
# create a array to track selected vertex
# selected will become true otherwise false



if __name__ == '__main__':
    coordinates = [[0,0],[0,3],[1,1],[1,2],[2,2],[3,0],[4,2],[4,4]]
    print(UserMainCode.getNoOfConnectedPatches(8,coordinates,10))