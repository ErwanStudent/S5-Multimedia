from math import cos, sin

def projection(point3d):
    return((point3d[0],point3d[1]))

def compose(dessin, points, triangles, nbmodulo = 1):
  colors=("blue","red","green","purple","yellow","white","coral","darkblue")
  for i in range(0,len(triangles)//3):
    #   print(triangles[3*i],triangles[3*i+1],triangles[3*i+2])
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