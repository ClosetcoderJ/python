menu = {
    "CaffeAmericano": "4,600원",
    "CaffeLatte": "5,100원",
    "Cappuccino": "5,100원",
    "OatmealLatte": "5,400원"
}

print(menu)

# 키만 가져옴
keys = menu.keys()
print(keys)

# 밸류만 가져옴
values = menu.values()
print(values)

# 키와 밸류 쌍을 가져옴
keyValues = menu.items()
print(keyValues)

# 딕셔너리 추가
menu["dolceLatte"] = "6,100원"
menu.setdefault("espresso", "4,100원")
menu["doubleShot"] = "4,800원"
menu.setdefault("coldBrew", "5000원")
print(menu)

menu["Cappuccino"] = 5300 #이경우는 새로만드는건지 수정하는건지 잘 모름
menu.update(dolceLatte=6500)
menu.update(newCoffee=4100) #없는데 새로 만들어짐 하지만 코드가독성 떨어짐

#코딩실습
menu.update(CaffeAmericano=4700)
menu.update(coldBrew=5300)
print(menu)

#리스트에서 팝은 중간에빼거나 앞뒤에있는거 뺐지만(앞,중간은 위치변동), 딕셔너리는 원래 무작위로 저장되기때문에 그냥 키만 정해서 팝하면 됨)
removedItem=menu.pop("doubleShot")
print(removedItem)
print(menu)



