from telethon import TelegramClient, sync
import csv

api_id = '1128991'
api_hash = '6f7c255b1da43aed877093d6d20463b3'
phone = '+919866655322'

client = TelegramClient(phone, api_id, api_hash).start()

groups_list = []
group = {}

for d in client.get_dialogs():
    try:
        if d.is_group and not d.is_channel and d.name != '':
            group = {
                "id": d.entity.id,
                "title" : d.entity.title
            }
            groups_list.append(group)
    except:
        continue

print('Choose a group to scrape members from:')
i=0
for g in groups_list:
    print(str(i) + '- ' + g['title'])
    i+=1

g_index = input("Enter a Number: ")
target_group = groups_list[int(g_index)]

print('Fetching Members...')
all_participants = []

all_participants = client.get_participants(target_group["title"])

print('Saving In file...')
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username', 'phone','group', 'user_id', 'group_id'])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.phone:
            phone = user.phone
        else:
            phone = ""
        if user.id:
            user_id = user.id
        else:
            user_id = ""
        if target_group["title"]:
            group = target_group["title"]
        else:
            group = ""
        if target_group["id"]:
            group_id = target_group["id"]
        else:
            group_id = ""
        writer.writerow([username, phone, group, user_id, group_id])      
print('Members scraped successfully.')