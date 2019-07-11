import requests
import csv
from datetime import datetime


'''
1. make request to LC api w/ settings
2. parse response 
3. write to CSV 
'''


def main():
    username = input("Please enter username (LiveChat email address): ")
    api_key = input("Please enter password (aka API key): ")

    headers = {
        "X-API-Version": "2",
        # "Authorization": "Basic " + api_key,
        "Cache-Control": "no-cache",
    }
    url = "https://api.livechatinc.com/reports/chats/chatting_time"
    start_date_param = "date_from="
    start_date = input("Please enter the start date in YYYY-MM-DD format:")
    end_date_param = "date_to="
    end_date = input("Please enter the end date in YYYY-MM-DD format:")
    group = "1"
    group_param = "group="
    full_url = url + "?" + start_date_param + start_date + "&" + end_date_param + end_date + "&" + group_param + group

    response = requests.get(full_url, headers=headers, auth=(username, api_key))

    data = []
    for date in response.json():
        # print(date)
        data.append([date, response.json()[date]['hours']])
        # print(response.json()[date]['hours'])

    time = datetime.strftime(datetime.now(), '%Y-%m-%d %I:%M:%S %p')

    filename = 'lc_data' + time + '.csv'
    with open(filename, mode="w") as lc_data:
        field_names = ["Dates", "Hours per Day"]
        lc_writer = csv.writer(lc_data)
        lc_writer.writerow(field_names)
        lc_writer.writerows(data)
    print("Your file has been written to 'lc_data.csv'")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()



