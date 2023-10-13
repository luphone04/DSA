class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

def find_largest_cloud_size(rows, cols, image):
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    disjoint_sets = DisjointSets(rows * cols)

    # Helper function to convert 2D coordinates to 1D index
    def to_index(x, y):
        return x * cols + y

    for x in range(rows):
        for y in range(cols):
            if image[x][y] == 1:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and image[nx][ny] == 1:
                        disjoint_sets.union(to_index(x, y), to_index(nx, ny))

    cloud_sizes = [0] * (rows * cols)
    largest_cloud_size = 0

    for x in range(rows):
        for y in range(cols):
            if image[x][y] == 1:
                root = disjoint_sets.findset(to_index(x, y))
                cloud_sizes[root] += 1
                largest_cloud_size = max(largest_cloud_size, cloud_sizes[root])

    return largest_cloud_size

if __name__ == "__main__":
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    image = []

    print("Enter the image matrix (0 for sky, 1 for cloud):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        image.append(row)

    largest_cloud_size = find_largest_cloud_size(rows, cols, image)
    print(f"The size of the largest cloud is: {largest_cloud_size}")