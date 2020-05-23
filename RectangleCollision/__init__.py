class collision():
    def rectangle(obj1x,obj1y,obj2x,obj2y,obj1w=32,obj1h=32,obj2w=32,obj2h=32):
         if obj1x < obj2x + obj2w and obj1x + obj1w > obj2x and obj1y < obj2y + obj2h and obj1y + obj1h > obj2y:
            return True