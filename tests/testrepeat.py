import PyNormaliz_cpp

# cone = PyNormaliz_cpp.NmzCone(vertices = [(-3,-2,-1,1), (-1,1,-1,2), (1,1,-1,1), (1,1,1,1)])

for i in range(0,10000):
    print(i)
    print("pre")
    PyNormaliz_cpp.NmzResult(5,"IsPointed")
    print("post")

