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

dessin = svgwrite.Drawing('question4.svg', size=(800, 600))

for i in range(1, 6):
    matdil = Matdilatation(1-0.2*i)
    matrot = Matrotation(i*pi/12)
    vectrans = (250, 250)
    
    dessin.add(dessin.polygon([translater(
        prodMatVect(matrot,
        prodMatVect(matdil,sommet)),
        vectrans)
        for sommet in carre], fill='#0000FF', stroke='#000000', opacity=0.7-(0.1*i)))
dessin.save()

