#Guest list


dinner_list = ['Sam Scott', 'Tyler Jame', 'Abadn Skrettn', 'Sbadut Reks']

def invites():

	print(f'You want food {dinner_list[0]}? Come get food!')
	print(f'Please honor me {dinner_list[1]}. Dine and talk!')
	print(f'Hunger gnaws at you {dinner_list[2]}. Allow me to correct that.')
	print(f'Poison is not for {dinner_list[3]}. You are safe eating here.')

invites()


print(f'\n{dinner_list[1]} will do me no honor. His name struck from the fun list\n\n')

del dinner_list[1]

dinner_list.append('Nahony Simpho')

invites()

print('\n\nThe council of Elders has seen fit to commission a more grand dining table. We have thus allowed for an expanded guest list.\n\n')

dinner_list.insert(0, 'Havlone of Maxuo')
dinner_list.insert(2, 'Barben Blorts')
dinner_list.append('Bill')

def expanded_invites():
	print(f'We must talk {dinner_list[4]}. The food will be good.')
	print(f'Be there of be dead {dinner_list[5]}. You will not starve.')
	print(f'You have been asking forever. This one time {dinner_list[6]}, you may sit with us.')

invites()
expanded_invites()

print('\nWar! Trechery! The table has been destroyed by the vile Choob! Dinner for many has been lost to the sands of time. Our two closest advisors will be allowed council.\n')

list_len = len(dinner_list) - 2


for i in range(0, list_len): 
	dis_invited = dinner_list.pop()
	print(f'Your dishonor shall be avenged {dis_invited}! Further preperations for correction are forthcoming!\n')



list_len = len(dinner_list)

for i in range(0, list_len):
	print(f'We urgently must consult, {dinner_list[0]}! We must correct our table tragedy!\n')
	del dinner_list[0]

print(dinner_list)	


# note(BCL): Working on 3-7


