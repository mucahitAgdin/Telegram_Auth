import file_transactions


user_list = file_transactions.read_json("users")
delete_user_list = file_transactions.read_json("deleted_user_list")
deleting_user_list = []
for x in user_list:
	user_list[x]['days_left']-=1
	if(user_list[x]['days_left']==0):
		deleting_user_list.append(x)
for i in deleting_user_list:
	del user_list[i]
	delete_user_list.append(i)
file_transactions.convert_to_json(user_list,"users")
file_transactions.convert_to_json(delete_user_list,"deleted_user_list")