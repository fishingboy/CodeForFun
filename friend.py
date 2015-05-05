# 呼叫幫手
def call_friend(type="soldier"):
    while self.gold > self.costOf(type):
        self.summon(type)

# 叫同伴攻擊最靠近的敵人
def call_friend_attack():
    for friend in self.findFriends():
        enemy = friend.findNearestEnemy()
        self.command(friend, "attack", enemy)
