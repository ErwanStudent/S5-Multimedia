import svgwrite
from math import *

# Original

dessin = svgwrite.Drawing('exercice_1.svg', size=(800, 600))
carre = [(0,0), (400, 0), (200, 300)]

dessin.add(dessin.polygon(carre, fill='#0000FF', stroke='#000000', opacity=0.7))
dessin.save()

# Triangle Rouge

dessin = svgwrite.Drawing('exercice_1_rouge.svg', size=(800, 600))
carre = [(0,300), (200, 0), (400, 300)]

dessin.add(dessin.polygon(carre, fill='#FF0000', stroke='#000000', opacity=0.7))
dessin.save()

# Carré vert

dessin = svgwrite.Drawing('exercice_carre.svg', size=(800, 600))
carre = [(-100,100), (-100, -100), (100, -100), (100, 100)]

dessin.add(dessin.polygon(carre, fill='#00FF00', stroke='#000000', opacity=0.7))
dessin.save()

# Carré vert translaté

def translater(input, vectTrans):
    x, y = input
    tx, ty = vectTrans
    return ((x + tx, y + ty))

dessin = svgwrite.Drawing('exercice_carre_trans.svg', size=(800, 600))

carre = [(-100,100), (-100, -100), (100, -100), (100, 100)]
trans = (100, 100)

carre_trans = [translater(sommet, trans) for sommet in carre]
dessin.add(dessin.polygon(carre_trans, fill='#00FF00', stroke='#000000', opacity=0.7))

dessin.save()

# Carré tourné de 30 degrés

def rotation(point, angle):
    x, y = point

    out = ((x * cos(angle) - y * sin(angle)), (x * sin(angle) + y * cos(angle)))
    
    return out

dessin = svgwrite.Drawing('exercice_carre_rotation.svg', size=(800, 600))
carre = [(-100,100), (-100, -100), (100, -100), (100, 100)]

dessin.add(dessin.polygon([rotation(translater(sommet, [400, 300]), pi/24) for sommet in carre], fill='#FF0000', stroke='#000000', opacity=0.7))
dessin.save()

# Matrice 2D

def prodMatVect(Mat, Vect):
    x, y = Vect
    ((a11, a12), (a21, a22)) = Mat

    x2 = a11 * x + a12 * y
    y2 = a21 * x + a22 * y

    return (x2, y2)

def Matrotation(angle):
    return ((cos(angle), -sin(angle)), (sin(angle), cos(angle)))

matRot=Matrotation(pi/12)

carre_out=[translater(prodMatVect(matRot,sommet),trans) for sommet in carre]

dessin = svgwrite.Drawing('exercice_carre_matrice_2d.svg', size=(800, 600))
dessin.add(dessin.polygon(carre_out, fill='#FF0000', stroke="#000000", opacity=0.7))
dessin.save()

# Dilatation

def Matdilatation(coefDilatation):
    return ((coefDilatation, 0), (0, coefDilatation))

dessin = svgwrite.Drawing('question3.svg', size=(3000, 500))

for i in range(1, 6):
    matdil = Matdilatation(1-0.1*i)
    vectrans = (0 + i*200, 250)
    
    dessin.add(dessin.polygon([translater(
        prodMatVect(matdil,sommet),
        vectrans)
        for sommet in carre], fill='#0000FF', stroke='#000000', opacity=0.7))
dessin.save()

dessin = svgwrite.Drawing('question4.svg', size=(800, 600))

for i in range(1, 6):
    matdil = Matdilatation(1-0.2*i)
    matrot = ((1,0), (0, 1))
    vectrans = (300, 300)
    
    dessin.add(dessin.polygon([translater(
        prodMatVect(matrot,
        prodMatVect(matdil,sommet)),
        vectrans)
        for sommet in carre], fill='#0000FF', stroke='#000000', opacity=0.7-(0.1*i)))
dessin.save()


def prodMatMat(MatA, MatB):
    ((a11, a12), (a21, a22)) = MatA
    ((B11, B12), (B21, B22)) = MatB

    return (
        (a11 * B11 + a12 * B21, a11 * B12 + a12 * B22),
        (a21 * B11 + a22 * B21, a21 * B12 + a22 * B22)
    )

dessin = svgwrite.Drawing('question4_prod_mat_mat.svg', size=(800, 600))
for i in range(1, 6):
    MatA = Matrotation(i*pi/24)
    MatB = Matdilatation((1.0/(2*i))*0.5)
    Mat = prodMatMat(MatA, MatB)
    
    dessin.add(dessin.polygon([translater(
        prodMatVect(Mat, sommet), (50+i*100, 300))
        for sommet in carre], fill='#0000FF', stroke='#000000', opacity=0.7))
dessin.save()

# Limiter les calculs

## Q1
aux = 100
points = [(aux, aux), (-aux, aux), (-aux, -aux), (aux, -aux)]
triangles = [0,1,2,0,2,3]

dessin = svgwrite.Drawing('limit_calcul_q1.svg', size=(800, 600))
for i in range(2):
    dessin.add(dessin.polygon((points[triangles[3*i]], points[triangles[3*i+1]], points[triangles[3*i+2]]), fill='blue', opacity=0.5, stroke='black'))
dessin.save()

#Q2

aux = 100
points = [(aux, aux), (-aux, aux), (-aux, -aux), (aux, -aux)]
triangles = [0,1,2,0,2,3]

dessin = svgwrite.Drawing('limit_calcul_q2.svg', size=(800, 600))
for i in range(2):
    liste_points = [
        points[triangles[3*i]],
        points[triangles[3*i+1]],
        points[triangles[3*i+2]]
    ]

    dessin.add(
        dessin.polygon(
            [translater(sommet, (100, 100)) for sommet in liste_points],
            fill='blue', opacity=0.5, stroke='black'
        )
    )
dessin.save()

# Q3

dessin = svgwrite.Drawing('limit_calcul_q3.svg', size=(800, 600))

def compose(points,triangles):
  liste_point=[]
  colors=("blue","red","green","purple","yellow","white","coral","darkblue")
  for i in range(0,len(triangles)//3):
      print(triangles[3*i],triangles[3*i+1],triangles[3*i+2])
      dessin.add(dessin.polygon((points[triangles[3*i]],points[triangles[3*i+1]],points[triangles[3*i+2]]), fill=colors[(i%(len(colors)*2))//2],  opacity=0.5,stroke='black'))

compose(points, triangles)
dessin.save()

# Q4

dessin = svgwrite.Drawing('limit_calcul_q4_chat.svg', size=(800, 600))

points = [
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

def compose(points,triangles, opacity=0.7):
  colors=("blue","purple", "green", "red","yellow","white","coral","darkblue")
  for i in range(0,len(triangles)//3):
      print(triangles[3*i],triangles[3*i+1],triangles[3*i+2])
      dessin.add(dessin.polygon((points[triangles[3*i]],points[triangles[3*i+1]],points[triangles[3*i+2]]), fill=colors[(i%len(colors))], opacity=0.5,stroke='black'))

compose(points, triangles)
dessin.save()

# Q5

dessin = svgwrite.Drawing('limit_calcul_q5_chat_rot.svg', size=(800, 600))
points_out = [translater(prodMatVect(Matrotation(pi/12),sommet), (100, 100)) for sommet in points]

compose(points_out, triangles)
dessin.save()

# Q6

dessin = svgwrite.Drawing('limit_calcul_q6_chat_rot.svg', size=(800, 400))

for i in range(1, 6):
    MatA = Matrotation(-i*pi/8)
    MatB = Matdilatation(1-(i*0.15))
    Mat = prodMatMat(MatA, MatB)

    vectrans = (100 + i*80, 250)

    points_out = [translater(prodMatVect(Mat,sommet), vectrans) for sommet in points]

    compose(points_out, triangles, 0.7 - (0.1*i))
dessin.save()

