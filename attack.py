# 攻擊敵人
def attack_enemy(enemy):
    if enemy:
        len = self.distanceTo(enemy)
        self.shield()
        if self.canElectrocute(enemy) and self.distanceTo(enemy) > 10 and self.isReady("electrocute"):
            # 電暈
            self.electrocute(enemy)
        elif self.isReady("bash"):
            # 盾牌攻擊
            self.bash(enemy)
        elif self.isReady("cleave") and self.distanceTo(enemy) < 5:
            # 範圍攻擊
            self.cleave(enemy)
        elif self.canCast("chain-lightning", enemy) and self.isReady("cast"):
            # 閃電攻擊
            self.cast("chain-lightning", enemy)
        else:
            # 普通攻擊
            self.attack(enemy)

# 攻擊最靠近的敵人
def attack_nearest_enemy():
    enemy = self.findNearest(self.findEnemies())
    attack_enemy(enemy)

# 判斷是否有敵人
def hasEnemy():
    return len(self.findEnemies()) > 0