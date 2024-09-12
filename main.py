import c4d
from c4d import gui
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True

# Main function
def main():
    x=[]
    y=[]
    z=[]
    p1=""
    p2=""
    p3=""
    
    #X-Data
    x_data = open(r"x_postion.txt", "r")

    x_pos=x_data.read()
    x_pos=x_pos.replace(","," ")
    #print(x_pos)
    for i in range(len(x_pos)):
        if x_pos[i]!=" ":
            p1=p1+x_pos[i]
        else:
            x.append(float(p1))
            p1=""
    #print(x)
    
    #Y-Data
    y_data = open(r"y_postion.txt", "r")

    y_pos=y_data.read()
    y_pos=y_pos.replace(","," ")
    for i in range(len(y_pos)):
        if y_pos[i]!=" ":
            p2=p2+y_pos[i]
        else:
            y.append(float(p2))
            p2=""
    #print(y)
    
    #Z-Data
    z_data = open(r"z_postion.txt", "r")

    z_pos=z_data.read()
    z_pos=z_pos.replace(","," ")
    for i in range(len(z_pos)):
        if z_pos[i]!=" ":
            p3=p3+z_pos[i]
        else:
            z.append(float(p3))
            p3=""
    #print(z)
    
    l=len(x)
    obj = c4d.SplineObject(l,c4d.SPLINETYPE_LINEAR)
    
    for i in range(l):
        obj.SetPoint(i,c4d.Vector(x[i],y[i],z[i]))
    
    doc.InsertObject(obj)
    doc.SetActiveObject(obj)
    c4d.EventAdd()
    
    

# Execute main()
if __name__=='__main__':
    main()