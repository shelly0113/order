print('歡迎使用拉麵點餐機~')
print('(1)鹽味拉麵 $220\n(2)醬油拉麵 $240\n(3)豚骨拉麵 $280')

order = input('請選擇拉麵口味(輸入1 or 2 or 3)')
size = input('是否加大, 豚骨口味+$50 其他口味+$30 (輸入Y or N)').upper()
egg = input('是否加蛋+$30 (輸入Y or N)').upper()
pork = input('是否叉燒+$60 (輸入Y or N)').upper()
total = 0

if order == '1':
    total += 220
elif order == '2':
    total += 240
elif order == '3':
    total += 280

if size == 'Y' and order == '3':
    total += 50
elif size == 'Y' and order == '1' or order == '2':
    total += 30


if egg == 'Y':
    total += 30


if pork == 'Y':
    total += 60

if size == 'Y' and egg == 'Y' and pork == 'Y':
    total -= 20
    print(f'\n\n加好加滿折價$20，總金額${total}，感謝您的光臨')
else:
    print(f'總金額${total}，感謝您的光臨')
