from telethon import TelegramClient, sync
from dotenv import load_dotenv
import os
import csv

def main():
    # Get ENV variables from the '.env' file
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    phone = os.getenv('PHONE')
    fileName = input("Enter the File Name: ")
    fileName = fileName + '.csv'

    client = TelegramClient(phone, api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the OTP: '))

    groups_list = []
    group = {}

    # Get's a List of Dictionaries with Group name with Group ID
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

    # Create a CSV file
    with open(fileName, mode="w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username', 'first_name', 'last_name', 'phone','group', 'user_id', 'group_id'])

    # Extract Users from the Group
    for group_name in groups_list:
        # Iterates over List of Dictionaries to extract Users
        # Output CSV file has:- username, first_name, last_name, phone, group, user_id, group_id

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
    
# Generates '.env' File in the project Directory
def generateENV():
    print("Generating ENV File")
    envData = []
    dataName = ['API_ID', 'API_HASH', 'PHONE']
    print("Enter the Required Credentials:")
    index = 0
    for i in dataName:
        data = input('{}: '.format(i))
        envData.append(data)
    with open(".env", mode="w",encoding='UTF-8') as f:
        for index in range(len(envData)):
            f.write('{0} = \'{1}\'\n'.format(dataName[index], envData[index]))
    return

if __name__ == "__main__":
    print("Checking .env file")
    if os.path.isfile('.env'):
        main()
    else:
        generateENV()
        main()
        