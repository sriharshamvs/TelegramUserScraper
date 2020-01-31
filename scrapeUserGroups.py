from telethon import TelegramClient, sync
import csv

# Enter your Credentials
api_id = '1128991'
api_hash = '6f7c255b1da43aed877093d6d20463b3'
phone = '+919866655322'
fileName = "users.csv"

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the OTP: '))

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

with open(fileName,"w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username', 'first_name', 'last_name', 'phone','group', 'user_id', 'group_id'])


for group_name in groups_list:
    target_group = group_name
    all_participants = []
    all_participants = client.get_participants(target_group["title"])

    print('Fetching Members from {}\nWriting to the file'.format(target_group["title"]))

    with open(fileName, mode="a", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
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
            writer.writerow([username, first_name, last_name, phone, group, user_id, group_id])      

print('All Group Members are scraped successfully.')