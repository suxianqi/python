import random

computer = random.choice(['石头', '剪刀', '布'])
player = input('请出拳(石头/剪刀/布)：')

# print('您出了:', player, '计算机出的是:', computer)
print('您出了: %s, 计算机出的是: %s' % (player, computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You WIN!!!')
    else:
        print('You LOSE!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You LOSE!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You WIN!!!')
else:
    if computer == '石头':
        print('You WIN!!!')
    elif computer == '剪刀':
        print('You LOSE!!!')
    else:
        print('平局')
