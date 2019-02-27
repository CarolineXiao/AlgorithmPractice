def removeObstacle(numRows, numColumns, lot):
    visited = []
    queue = []
    start = (0, 0, 0)
    queue.append(start)
    while queue:
        v = queue.pop(0)
        neighbour = []
        if v[0]-1 >= 0 and v[0]-1 < numRows and v[1] >= 0 and v[1] < numColumns and lot[v[0]-1][v[1]] != 0:
            neighbour.append((v[0]-1, v[1], v[2]+1))
        if v[0]+1 >= 0 and v[0]+1 < numRows and v[1] >= 0 and v[1] < numColumns and lot[v[0]+1][v[1]] != 0:
            neighbour.append((v[0]+1, v[1], v[2]+1))
        if v[0] >= 0 and v[0] < numRows and v[1]-1 >= 0 and v[1]-1 < numColumns and lot[v[0]][v[1]-1] != 0:
            neighbour.append((v[0], v[1]-1, v[2]+1))
        if v[0] >= 0 and v[0] < numRows and v[1]+1 >= 0 and v[1]+1 < numColumns and lot[v[0]][v[1]+1] != 0:
            neighbour.append((v[0], v[1]+1, v[2]+1))

        for n in neighbour:
            if lot[n[0]][n[1]] == 9:
                return n[2]
            if n not in visited and n not in queue:
                queue.append(n)
        visited.append(v)
    return -1








if __name__ == "__main__":
    r = removeObstacle(5, 4, [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]])
    #r = removeObstacle(3, 3, [[1, 0, 0], [1, 0, 0], [1, 1, 9]])
    print(r)
