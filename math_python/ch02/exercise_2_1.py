from vector_drawing import *

#2.1 恐龙角脚指尖上的点的x坐标和y坐标是什么,并画出图像
draw((-1,-4))
#2.2 在平面上画出（2，-2）以及与其对应的箭头
draw(
    Points((2,-2)),
    Arrow((2,-2))
)
#2.3 教材中恐龙图像个点的位置向量
dino_vectors = [(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4)
                ,(1,-4),(2,-3),(1,-2),(3,-1),(5,1)]
#2.4构建以dino_vectors 为顶点的Polygon对象，画出每个点相连的恐龙图像
draw(
    Points(*dino_vectors),
    Polygon(*dino_vectors)
     )
draw(Arrow((2,-2)))
#2.5绘制当x坐标在-10到10的范围内的（x，x**2）的点
draw(
    Points(*[(x,x**2) for x in range(-10,11)]),
    grid=(1,10),
    nice_aspect_ratio=False
)