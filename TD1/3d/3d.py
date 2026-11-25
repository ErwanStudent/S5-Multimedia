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

for i in range(10):
    translation_x = 200 + (75 * i)
    translation_y = 300 - (50 * i)

    Mat = prodMatMat3D(
        Matdilatation3D(1 - (0.15 * i)),
        prodMatMat3D(
            prodMatMat3D(
                Matrotation3DX((pi/12) + ((pi/16) * i)),
                Matrotation3DY((pi/8) + ((pi/16) * i))
            ),
            Matrotation3DZ((pi/24) + ((pi/16) * i)),
        )
    )

    points_proj = [
        projection(
            translation_3d(
                prodMatVect3D(Mat, sommet),
                (translation_x, translation_y, 0)
            )
        )
        for sommet in points
    ]
    compose(dessin, points_proj, cube, 2)

dessin.save()

# Cordonnées homogènes 2D

dessin = svgwrite.Drawing('chat_homo_2d.svg', size=(800, 600))

points_chat = [
    (-100, -70), # 0
    (-50, 0), # 1
    (-100, 0), # 2
    (0, 50), # 3
    (100, 0), # 4
    (100, -70), # 5
    (50, 0), # 6
    (0, -30) # 7
]
triangles = [1, 0, 2, 2, 3, 4, 4, 5, 6, 6, 7, 1]

chathomo=[(sommet[0], sommet[1], 1) for sommet in points]

for i in range(1,10):
  Matrot=Matrotation2DHomo(i*pi/24)
  Mattrans=Mattranslation2DHomo(( i*100,200))
  Matdil=Matdilatation2DHomo(2/i)

  Mat=prodMatMat3D(Mattrans, Matrot )
  Mat=prodMatMat3D(Mat, Matdil)

  points_out=[projection(prodMatVect3D(Mat, sommet)) for sommet in chathomo]

  compose(dessin, points_out, triangles)

dessin.save() 

# Cordonnées homogènes pour la 3D

dessin = svgwrite.Drawing('cords_homo_3d.svg', size=(800, 600))

for i in range(8):
  MatTrans = MatTranslation4D((200 + i*150,200+ i*50, 0))

  # Rotation
  MatRotX = MatRotation4DX(pi/6 + i*pi/12)
  MatRotZ = MatRotation4DZ(pi/24 + i*pi/24)
  MatRotY = MatRotation4DY(pi/48 + i*pi/48)

  M = prodMatMat4D(prodMatMat4D(MatRotX, MatRotY), MatRotZ)
  M = prodMatMat4D(MatTrans, M)

  # Dilatation

  MatDil = Matdilatation4D(1.25-i*0.15)
  M = prodMatMat4D(M, MatDil)

  points_transforme = [projection(prodMatVect4D(M,(*p,1))) for p in points]
  compose(dessin, points_transforme, cube, 2)

dessin.save()