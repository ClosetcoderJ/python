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

