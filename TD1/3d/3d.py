import svgwrite
from api import *
from math import pi

# Q1

aux = 100
points = [
    [-aux, -aux, aux], # point 0 (face devant)
    [-aux, aux, aux], # point 1   (face devant)
    [aux, -aux, aux], # point 2   (face devant)
    [aux, aux, aux], # point 3    (face devant)
    [-aux, -aux, -aux], # point 4 (face arrière)
    [-aux, aux, -aux], # point 5
    [aux, -aux, -aux], # point 6
    [aux, aux, -aux] # point 7
]

cube = [
    0,1,2,
    1,2,3,
    4,5,7,
    4,6,7,
    3,2,6,
    3,6,7,
    1,7,3,
    1,7,5,
    0,5,4,
    0,5,1,
    2,0,4,
    2,6,4
]

dessin = svgwrite.Drawing('exercice_translation.svg', size=(800, 600))

Mat = prodMatMat3D(
    prodMatMat3D(
        Matrotation3DX(pi/12),
        Matrotation3DY(pi/8)
    ),
    Matrotation3DZ(pi/24),
)

points_proj = [
    projection(
        translation_3d(
            prodMatVect3D(Mat, sommet),
            (200, 200, 0)
        )
    )
    for sommet in points
]
compose(dessin, points_proj, cube, 2)

dessin.save()

# Q8

dessin = svgwrite.Drawing('multi_cube_transformation.svg', size=(800, 600))

# WIP

for i in range(10):
    Mat = prodMatMat3D(
        Matdilatation3D(1-0.1*i),
        prodMatMat3D(
            prodMatMat3D(
                Matrotation3DX(pi/12),
                Matrotation3DY(pi/8)
            ),
            Matrotation3DZ(pi/24),
        )
    )

    points_proj = [
        projection(
            translation_3d(
                prodMatVect3D(Mat, sommet),
                (200, 200, 0)
            )
        )
        for sommet in points
    ]
    compose(dessin, points_proj, cube, 2)

dessin.save()