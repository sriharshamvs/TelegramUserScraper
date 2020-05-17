# Telegram Users Scraper

This project is used to scrape Telegram User details from the Group(s).

## Deployment

### Create a Telegram App and Get Your Credentials
- Go to [my.telegram.org](https://my.telegram.org/auth) and log in.
- Click on API development tools and fill the required fields.
- Choose a name for the App and save the `App api_id`, `App api_hash` credentials.

### Install Dependencies
- Install Python Dependencies
```
pip3 install -r requirements.txt
```

## Usage

### Get users from a selected group
- Execute the script
```
python3 scrapeSingleGroup.py
```
- If the script is running for the first time, it generates `.env` file.

Enter the required credentials:

```
API_ID = xxxxxx
API_HASH = xxxxxx
PHONE = +xxxxxxxxxxx
```
Phone Number should contain `country code`
- Enter the `File Name`
- Select the Group Number to be extracted.
- A `CSV` file is generated

### Get users from all the groups
- Execute the script
```
python3 scrapeUserGroups.py
```
- If the script is running for the first time, it generates `.env` file.

Enter the required credentials:

```
API_ID = xxxxxx
API_HASH = xxxxxx
PHONE = +xxxxxxxxxxx
```
Phone Number should contain `country code` exmaple `+911234567890`
- Enter the `File Name`
- A `CSV` file is generated
