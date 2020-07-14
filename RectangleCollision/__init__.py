class collision():

    def rectangle(Obj1X,Obj1Y ,Obj2X,Obj2Y ,Obj1Width=32,Obj1Height=32 ,Obj2Width=32,Obj2Height=32):

        if Obj1X < Obj2X + Obj2Width and Obj1X + Obj1Width > Obj2X and Obj1Y < Obj2Y + Obj2Height and Obj1Y + Obj1Height > Obj2Y:
             return True

        if Obj1X == Obj2X and Obj1Y == Obj2Y: return True

        return False