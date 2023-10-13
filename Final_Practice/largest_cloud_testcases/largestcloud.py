# code efficiently finds the size of the largest cloud in a given binary image by using 
# Disjoint-Set Union (Union-Find) data structure to track connected cloud pixels and compute their sizes. 
# The example provided shows how to use this code to analyze a sample image, but it can be adapted for 
# various applications that involve connected component analysis in binary images.




#used to implement a data structure called Disjoint-Set Union (also known as Union-Find) 
#used to efficiently keep track of "CONNECTED COMPONENTS" in a "graph" or "network".
class DisjointSets:
    def __init__(self, n): #initializes the data structure with n elements.
        #creates two lists, p (parent) and rank, to maintain the parent of each element and their respective ranks.
        self.p = list(range(n))
        self.rank = [0] * n

    #finds the representative (root) of the set containing element u
    #uses path compression for optimization, which makes future find operations faster
    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]
        

        # unions two sets containing elements u and v
    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        #uses the rank of the sets to determine the new parent during the union operation
        # which helps keep the tree balanced
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

#takes the number of rows, columns, and the image matrix as input 
#calculates the size of the largest cloud in the image.
def find_largest_cloud_size(rows, cols, image):
    #a helper function to check whether a given (x, y) coordinate is within the boundaries of the image
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    #represents the four possible directions to move in the image (up, down, left, and right).
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    disjoint_sets = DisjointSets(rows * cols)

    # Helper function to convert 2D coordinates to 1D index
    #helper function converts 2D coordinates (x, y) into a 1D index, which is used to represent elements in the Disjoint-Set
    def to_index(x, y):
        return x * cols + y
    
    # iterates through the entire image
    for x in range(rows):
        for y in range(cols):
            if image[x][y] == 1: #If a pixel is part of a cloud 
                #checks adjacent pixels and performs a union operation if the adjacent pixel is also part of the cloud.
                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy

                    # ensures that all connected cloud pixels are part of the same disjoint set.
                    if is_valid(nx, ny) and image[nx][ny] == 1:
                        disjoint_sets.union(to_index(x, y), to_index(nx, ny))

    #calculates the size of each cloud by tracking the size of their respective disjoint sets
    
    cloud_sizes = [0] * (rows * cols)
    largest_cloud_size = 0
    for x in range(rows):
        for y in range(cols):
            if image[x][y] == 1:
                root = disjoint_sets.findset(to_index(x, y))
                cloud_sizes[root] += 1
                largest_cloud_size = max(largest_cloud_size, cloud_sizes[root])
    #size of the largest cloud is also determined.
    return largest_cloud_size

#block of code is executed only when the Python script is run as the main program 
if __name__ == "__main__":
    # user input for the number of rows and columns and the image matrix
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    image = []

    print("Enter the image matrix (0 for sky, 1 for cloud):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        image.append(row)

    #n calls the find_largest_cloud_size function to compute and print the size of the largest cloud in the image.
    largest_cloud_size = find_largest_cloud_size(rows, cols, image)
    print(f"The size of the largest cloud is: {largest_cloud_size}")