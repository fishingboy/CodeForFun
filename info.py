# 告訴我敵人的類型
def tell_me_enemy_type():
    items = self.findEnemies()
    tell_me_type(items)

# 告訴我物品的類型
def tell_me_item_type():
    items = self.findItems()
    tell_me_type(items)

# 告訴我同伴的類型
def tell_me_item_type():
    items = self.findItems()
    tell_me_type(items)

# 告訴我 item 的類型？
def tell_me_type(items):
    if len(items) > 0:
        item_arr = []
        for item in items:
            # 看看是否已知
            finded = False
            i = 0
            while i < len(item_arr):
                # 已知的類型
                if item.type == item_arr[i].type:
                    item_arr[i].count += 1
                    finded = True
                    break
                i += 1

            # 新類型
            if finded == False:
                item_arr.append({"obj" : item, "type" : item.type, "count" : 1})

        # 顯示資訊
        for item_obj in item_arr:
            show_item_info(item_obj)

# 顯示資訊
def show_item_info(item):
    obj = item.obj
    msg = "(" + item.count + ") "
    msg += obj
    msg += ", type=" + item.type
    msg += ", HP=" + int(obj.maxHealth)
    self.say(msg)
