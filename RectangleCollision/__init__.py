class collision():
    def rectangle(x, y, target_x, target_y, width=32, height=32, target_width=32, target_height=32):

        if (x >= target_x and x < (target_x + target_width)) or ((x + width) >= target_x and (x + width) < (target_x + target_width)):
            if (y >= target_y and y < (target_y + target_height)) or ((y + height) >= target_y and (y + height) < (target_y + target_height)):
                return True
        return False
