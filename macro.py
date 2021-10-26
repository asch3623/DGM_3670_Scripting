import maya.cmds as cmds

def create_snowman():
    names=[]
    cmds.polySphere(radius=10, subdivisionsX=20, subdivisionsY=20,
                    axis=[0,1,0],
                    createUVs=2,
                    constructionHistory=1,
                    name='bottom')

    cmds.polySphere(radius=6, subdivisionsX=20, subdivisionsY=20,
                    axis=[0,1,0],
                    createUVs=2,
                    constructionHistory=1,
                    name='middle')

    cmds.polySphere(radius=4, subdivisionsX=20, subdivisionsY=20,
                    axis=[0,1,0],
                    createUVs=2,
                    constructionHistory=1,
                    name='top1')

    cmds.polySphere(radius=0.6, subdivisionsX=20, subdivisionsY=20,
                    axis=[0,1,0],
                    createUVs=2,
                    constructionHistory=1,
                    name='R_Eye')

    cmds.polySphere(radius=0.6, subdivisionsX=20, subdivisionsY=20,
                    axis=[0,1,0],
                    createUVs=2,
                    constructionHistory=1,
                    name='L_Eye')

    cmds.polyCube(width=1, height=1, depth=10, subdivisionsX=1,
                  subdivisionsY=1, subdivisionsZ=1,
                  axis=[0,1,0],
                  createUVs=4,
                  constructionHistory=1,
                  name='L_Arm')

    cmds.polyCube(width=1, height=1, depth=10, subdivisionsX=1,
                  subdivisionsY=1, subdivisionsZ=1,
                  axis=[0,1,0],
                  createUVs=4,
                  constructionHistory=1,
                  name='R_Arm')

    cmds.polyCylinder(radius=6, height=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=2,
                      axis=[0,1,0],
                      roundCap=0,
                      createUVs=3,
                      constructionHistory=1,
                      name='Hat')

    for x in range(3):
        y = str(x)
        cmds.polySphere(radius=0.6, subdivisionsX=20, subdivisionsY=20,
                        axis=[0, 1, 0],
                        createUVs=2,
                        constructionHistory=1,
                        name='Button'+y)
        names.append('Button'+y)

    i= float(-3)
    for x in range(5):
        y=str(x)
        cmds.polySphere(radius=.5, subdivisionsX=20, subdivisionsY=20,
                        axis=[0, 1, 0],
                        createUVs=2,
                        constructionHistory=1,
                        name='Mouth'+y)
        names.append('Mouth'+y)
        cmds.select('Mouth' + y)
        cmds.move(4, .15*(i**2)+25, i)
        i=i+1.5

    cmds.move(0,16,0, 'middle')
    cmds.move(0,26,0, 'top1')
    cmds.move(0,30,0, 'Hat')
    cmds.move(3.3,28,1, 'R_Eye')
    cmds.move(3.3,28,-1, 'L_Eye')
    cmds.move(0,22,8, 'R_Arm')
    cmds.rotate(-37,0,0, 'R_Arm')
    cmds.move(0,22,-8, 'L_Arm')
    cmds.rotate(37,0,0, 'L_Arm')
    cmds.move(6,17,0, 'Button0')
    cmds.move(5,9,0, 'Button1')
    cmds.move(8,6,0, 'Button2')

    cmds.polyExtrudeFacet('Hat.f[80:99]',constructionHistory=1, keepFacesTogether=1,
                          pvx=-3.576278687e-07, pvy=30.5, pvz=-4.768371582e-07, divisions=1,
                          twist=0, taper=1, off=0, thickness=0, smoothingAngle=30,
                          localTranslateZ=7.9)

    moreNames = ['middle', 'top1', 'bottom', 'Hat', 'R_Eye', 'L_Eye', 'L_Arm', 'R_Arm']
    names.extend(moreNames)

    cmds.group(names)
    cmds.rename('group1', 'Snowman')

create_snowman()