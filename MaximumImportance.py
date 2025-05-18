class Solution(object):
    def maximumImportance(self, n, roads):
        connections = [0] * n

        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1

        # (2, 3, 4, 2, 1)

        #assign importance to cities

        cities = [[0]*3]*n
        for i in range(n):
            cities[i] = [i, connections[i],0]

        # (0:2, 1:3, 2:4, 3:2, 4:1)

        cities.sort(key = lambda x: -x[1])

        #this is importance assignment
        for i in range(n):
            cities[i][2] = n-i

        print(cities)

        total = 0

        for i in range (n):
            total += cities[i][2] * cities[i][1]

        return total 
