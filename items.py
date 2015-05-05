# 撿金幣
def pickUpCoin():
    item = self.findNearest(self.findByType("coin"))
    if item:
        self.moveXY(item.pos.x, item.pos.y)
        return True
    else:
        return False
