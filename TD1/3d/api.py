from math import cos, sin

def projection(point3d):
    return((point3d[0],point3d[1]))

def compose(dessin, points, triangles, nbmodulo = 1):
    colors=("blue","red","green","purple","yellow","white","coral","darkblue")
    for i in range(0,len(triangles)//3):
        # print(triangles[3*i],triangles[3*i+1],triangles[3*i+2])
        dessin.add(dessin.polygon((points[triangles[3*i]],points[triangles[3*i+1]],points[triangles[3*i+2]]), fill=colors[(i%(len(colors)*nbmodulo))//nbmodulo], opacity=0.5,stroke='black'))

def translation_3d(point, direction):
    x, y, z = point
    dx, dy, dz = direction
    return (x + dx, y + dy, z + dz)

def prodMatVect3D(Mat, Vect):
    x, y,z = Vect
    ((a11,a12,a13), (a21, a22,a23), (a31, a32,a33)) = Mat

    x2 = a11 * x + a12 * y+ a13 * z
    y2 = a21 * x + a22 * y+ a23 * z
    z2 = a31 * x + a32 * y+ a33 * z

    return (x2,y2,z2)

def prodMatVect(Mat, Vect):
    x, y = Vect
    ((a11, a12), (a21, a22)) = Mat

    x2 = a11 * x + a12 * y
    y2 = a21 * x + a22 * y

    return (x2, y2)

def prodMatMat3D(MatA, MatB ):
    ((a11,a12,a13),
    (a21, a22,a23),
    (a31, a32,a33)) = MatA

    ((b11,b12,b13),
    (b21, b22,b23),
    (b31, b32,b33)) = MatB

    return (
        (a11*b11+a12 * b21+a13*b31, a11*b12+a12 * b22+a13*b32, a11*b13+a12 * b23+a13*b33),
        (a21*b11+a22 * b21+a23*b31, a21*b12+a22 * b22+a23*b32, a21*b13+a22 * b23+a23*b33),
        (a31*b11+a32 * b21+a33*b31, a31*b12+a32 * b22+a33*b32, a31*b13+a32 * b23+a33*b33))

def Matdilatation3D(coefDilatation):
    return (
        (coefDilatation, 0, 0),
        (0, coefDilatation , 0),
        (0, 0, coefDilatation)
    )

def Matrotation3DX(angle):
    return (
        (1, 0, 0),
        (0, cos(angle), -sin(angle)),
        (0, sin(angle), cos(angle))
    )

def Matrotation3DY(angle):
    return (
        (cos(angle), 0, sin(angle)),
        (0,1,0),
        (-sin(angle), 0, cos(angle))
    )

def Matrotation3DZ(angle):
    return (
        (cos(angle), -sin(angle), 0),
        (sin(angle), cos(angle), 0),
        (0, 0, 1)
    )

def Matrotation2DHomo(angle):
    return (
        (cos(angle), -sin(angle),0),
        (sin(angle), cos(angle),0),
        (0,0,1)
    )


def Matdilatation2DHomo(coefDilatation):
    return (
        (coefDilatation,0,0),
        (0, coefDilatation,0),
        (0,0,1)
    )

def Mattranslation2DHomo(Vect):
    return (
        (1,0,Vect[0]),
        (0,1, Vect[1]),
        (0,0,1)
    )

# 4D

def Matdilatation4D(coefDilatation):
         return ((coefDilatation ,0 ,0, 0),
                 (0 ,coefDilatation ,0 ,0),
                 (0 ,0 ,coefDilatation, 0),
                 (0, 0 ,0 ,1)
                )

def MatRotation4DY(angle):
    return (
        (cos(angle), 0, sin(angle), 0),
        (0 ,1, 0, 0),
        (-sin(angle), 0, cos(angle), 0),
        (0, 0, 0, 1)
    )

def MatRotation4DX(angle):
    return (
        (1, 0, 0, 0),
        (0, cos(angle), -sin(angle), 0),
        (0, sin(angle), cos(angle), 0),
        (0, 0, 0, 1)
    )

def MatRotation4DZ(angle):
    return (
        (cos(angle), -sin(angle), 0, 0),
        (sin(angle), cos(angle), 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1)
    )

def MatTranslation4D(translation: tuple[int,int,int]):
    x,y,z = translation

    return (
        (1, 0, 0, x),
        (0, 1, 0, y),
        (0, 0, 1, z),
        (0, 0, 0, 1)
    )

def prodMatMat4D(MatA, MatB):

    (
        (a11, a12, a13, a14),
        (a21, a22, a23, a24),
        (a31, a32, a33, a34),
        (a41, a42, a43, a44)
    )  = MatA

    (
        (b11, b12, b13, b14),
        (b21, b22, b23, b24),
        (b31, b32, b33, b34),
        (b41, b42, b43, b44)
    )  = MatB

    return (
        (a11*b11 + a12*b21 + a13*b31 + a14*b41 , a11*b12 + a12*b22 + a13*b32 + a14*b42 , a11*b13 + a12*b23 + a13*b33 + a14*b43, a11*b14 + a12*b24 + a13*b34 + a14*b44),
        (a21*b11 + a22*b21 + a23*b31 + a24*b41 , a21*b12 + a22*b22 + a23*b32 + a24*b42 , a21*b13 + a22*b23 + a23*b33 + a24*b43, a21*b14 + a22*b24 + a23*b34 + a24*b44),
        (a31*b11 + a32*b21 + a33*b31 + a34*b41 , a31*b12 + a32*b22 + a33*b32 + a34*b42 , a31*b13 + a32*b23 + a33*b33 + a34*b43, a31*b14 + a32*b24 + a33*b34 + a34*b44),
        (a41*b11 + a42*b21 + a43*b31 + a44*b41 , a41*b12 + a42*b22 + a43*b32 + a44*b42 , a41*b13 + a42*b23 + a43*b33 + a44*b43, a41*b14 + a42*b24 + a43*b34 + a44*b44)
    )

def prodMatVect4D(Mat, Vect):
    x, y, z, w = Vect
    ( (a11,a12,a13,a14), (a21, a22,a23,a24), (a31, a32,a33, a34), (a41, a42, a43, a44) ) = Mat

    x2 = a11 * x + a12 * y + a13 * z + a14 * w
    y2 = a21 * x + a22 * y + a23 * z + a24 * w
    z2 = a31 * x + a32 * y + a33 * z + a34 * w
    w2 = a41 * x + a42 * y + a43 * z + a44 * w

    return (x2,y2,z2,w2)