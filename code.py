from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def sky(x0 ,x1,y0,y1,z):
    d=1
    glColor3f(d+ 30/255,d+ 113/255,d+ 184/255)
    glBegin(GL_POLYGON)
    glVertex(x0 ,y0,z)
    glVertex(x0 ,y1,z)
    glVertex(x1,y1,z)
    glVertex(x1,y0,z)
    glEnd()

def road(x0,x1 ,y,z0,z1,r,g,b):
    glColor3f(r,g,b)
    glBegin(GL_POLYGON)
    glVertex(x0 ,y,z0)
    glVertex(x0 ,y,z1)
    glVertex(x1,y,z1)
    glVertex(x1,y,z0)
    glEnd()

def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  #red X
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0) #green Y
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1) #blue Z
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1, 1, 70)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)


    # Enable light 1 and set position
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION,  (0.5, 2.5, 3))
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

angle = 0
x = 0
forward = True

def qroad(x,y,z,r,g,b):
    #glColor3f(35 / 255, 15 / 255, 20 / 255)
    glColor3f(r,g,b)

    glTranslate(x,y,z)

    glRotate(90, 0, 1, 0)
    quadric = gluNewQuadric()
    glScale(5,0.05,30)
    gluCylinder(quadric ,0.5,0.5,5,10,1)
    glScale(1/5, 1/0.05, 1/30)
    glRotate(-90, 0, 1, 0)

    glTranslate(-x, -y, -z)


def lb(x,y,z):
    glTranslate(x, y, z)

    glColor3f(253 / 255, 247 / 255, 176 / 255)
    glutSolidSphere(0.2, 15, 15)

    glTranslate(-x, -y, -z)

def tree(x,y,z):
    glColor3f(35 / 255, 15 / 255, 20 / 255)
    glTranslate(x,y,z)

    glRotate(90, 1, 0, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric ,0.5,0.5,5,10,1)
    glRotate(-90, 1, 0, 0)

    glColor3f(51 / 255, 164 / 255, 87 / 255)
    glutSolidSphere(1.5, 15, 15)

    glTranslate(-x, -y, -z)

def ball():

    glColor3f(0, 1, 1)

    glTranslate(-x, 0, 0)
    glRotate(-angle, 0, 0, 1)
    glutWireSphere(0.91, 15, 15)
    glColor3f(0, 0.9,0.9,)
    glutSolidSphere(0.9, 10, 10)
    glutSolidIcosahedron()
    #inverse
    glRotate(angle, 0, 0, 1)
    glTranslate(x, 0, 0)

def car():
    carbody()

def carbody():
    carlowerbody()
    carupperbody()



def carlowerbody():
    glLoadIdentity()
    glColor3f(1, 0, 1)
    glRotate(-90, 0, 1, 0)
    glTranslate(x, 0, car_z)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 0)
    glutWireCube(5.02)
    glColor3f(0.5, 0, 0.5)



def carupperbody():
    glLoadIdentity()
    glRotate(-90, 0, 1, 0)
    glTranslate(x, 5*0.25, car_z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    glColor3f(0, 0, 0)
    glutWireCube(5.02)


def draw():
    global angle
    global x
    global forward
    global car_z


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glClearColor(51 / 255, 164 / 255, 1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #draw_XYZ()

    glRotate(-90, 0, 1, 0) #from X to Z

    ytree=3
    ztree=6
    for i in range(-30,6,5):
        tree(i, ytree, -ztree)
        tree(i, ytree, ztree)


    yroad=-1.2
    x0road=-55
    x1road=55
    sky(x0road, x1road, 8, -4, -15)
    road(x0road, x1road, yroad,-15,15,0,1,0)  # grass
    qroad(x0road,yroad,0,0.01,0.01,0.01)  # road

    ball()

    car()

    #light bulb
    glLoadIdentity()
    glRotate(-90, 0, 1, 0)

    glTranslate(x, 0, car_z)
    lb(2.5, 0.35, 0.8)
    lb(2.5, 0.35, -0.8)


    glColor3f(0.2, 0.2, 0.2)
    glLoadIdentity()
    glRotate(-90, 0, 1, 0)

    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5+car_z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 20, 20)

    glLoadIdentity()
    glRotate(-90, 0, 1, 0)

    glTranslate(x+0.5*5, -0.5 * 0.25*5, car_z - 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 20, 20)

    glLoadIdentity()
    glRotate(-90, 0, 1, 0)

    glTranslate(x-0.5*5, -0.5 * 0.25*5, car_z-0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 20, 20)

    glLoadIdentity()
    glRotate(-90, 0, 1, 0)

    glTranslate(x-0.5*5, -0.5 * 0.25*5, car_z+0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 20, 20)
    glutSwapBuffers()

    if forward:
        angle -= 2
        x += 0.02
        if x > 5:
            forward = False
    else:
        angle += 2
        x -= 0.02
        if x < -5:
            forward = True


car_z = 0


def specialKeyHandler(key, x, y):
    global car_z
    if key == GLUT_KEY_RIGHT:
        car_z -= 0.1
    elif key == GLUT_KEY_LEFT:
        car_z += 0.1

    draw()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialKeyHandler)
glutMainLoop()
