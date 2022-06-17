from itertools import count
import requests
import json
import csv
for i in range(0,1000000,300):
    print(i)
    url = f"https://api.opensea.io/api/v1/collections?offset={i}&limit=300"

    headers = {"Accept":"application/json"}

    response = requests.get(url,headers=headers)
    if response.status_code == 400:
        print("Server send response 400")
        break
    collections = response.json()
    
    for x in range(0,len(collections["collections"])):
        print(x)
        name = collections["collections"][x]['name']
        print(name)
        discord_url = collections["collections"][x]['discord_url']
        created_date = collections["collections"][x]['created_date']
        twitter_username = collections["collections"][x]['twitter_username']
        slug = collections["collections"][x]['slug']
        one_day_volume = collections["collections"][x]['stats']['one_day_volume']

        one_day_volume = collections["collections"][x]['stats']['one_day_volume']
        one_day_change = collections["collections"][x]['stats']['one_day_change']
        one_day_sales = collections["collections"][x]['stats']['one_day_sales']
        one_day_average_price = collections["collections"][x]['stats']['one_day_average_price']
        seven_day_volume = collections["collections"][x]['stats']['seven_day_volume']
        seven_day_change = collections["collections"][x]['stats']['seven_day_change']
        seven_day_sales = collections["collections"][x]['stats']['seven_day_sales']
        seven_day_average_price = collections["collections"][x]['stats']['seven_day_average_price']
        thirty_day_volume = collections["collections"][x]['stats']['thirty_day_volume']
        thirty_day_change = collections["collections"][x]['stats']['thirty_day_change']
        thirty_day_sales = collections["collections"][x]['stats']['thirty_day_sales']
        thirty_day_average_price = collections["collections"][x]['stats']['thirty_day_average_price']
        total_volume = collections["collections"][x]['stats']['total_volume']
        total_sales = collections["collections"][x]['stats']['total_sales']
        total_supply = collections["collections"][x]['stats']['total_supply']
        counts = collections["collections"][x]['stats']['count']
        num_owners = collections["collections"][x]['stats']['num_owners']
        average_price = collections["collections"][x]['stats']['average_price']
        num_reports = collections["collections"][x]['stats']['num_reports']
        market_cap = collections["collections"][x]['stats']['market_cap']
        floor_price = collections["collections"][x]['stats']['floor_price']

        payout_address = collections["collections"][x]['payout_address']
        print([name,discord_url,created_date,twitter_username,slug,one_day_volume,payout_address])
        with open('collections.csv','a') as f:
            csvwritter = csv.writer(f)
            csvwritter.writerow([name,discord_url,created_date,twitter_username,slug,payout_address,one_day_volume,one_day_change,one_day_sales,one_day_average_price,seven_day_volume,seven_day_change,seven_day_sales,seven_day_average_price,thirty_day_volume,thirty_day_change,thirty_day_sales,thirty_day_average_price,total_volume,total_sales,total_supply,counts,num_owners,average_price,num_reports,floor_price])
        f.close()