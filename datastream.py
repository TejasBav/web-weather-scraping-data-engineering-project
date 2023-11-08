import requests
from bs4 import BeautifulSoup
import pandas as pd
import time as t
import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
import json

EVENT_HUB_CONNECTION_STR = "Endpoint=sb://ehn-getsteramingdata.servicebus.windows.net/;SharedAccessKeyName=managepolicy;SharedAccessKey=N9QpxbggREx9TCkmoSqBNVATrjrRGRnV3+AEhGsEStE=;EntityPath=getweatherdata"
EVENT_HUB_NAME = "getweatherdata"

def getTemperature(city):
    weather_search_url = f'https://www.google.com/search?q=weather+{city}'

    headers_content = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    r = requests.get(weather_search_url, headers=headers_content) 

    #print(r.status_code)

    # print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser') 

    '''fidning temperature'''
    temp = soup.find('span', attrs={'id': 'wob_tm'}).text

    '''finding temperature unit'''
    temp_unit = soup.find('div', attrs={'class': 'vk_bk wob-unit'}).find('span', attrs={'class': 'wob_t'}).text

    '''fidning sky'''
    sky = soup.find('span', attrs={'id': 'wob_dc'}).text

    '''fidning time'''
    time = str(soup.find('div', attrs={'id': 'wob_dts'}).text)

    t.sleep(60)
    tempdf = pd.DataFrame([[temp,temp_unit,sky,time]], columns= ['Temperature', 'Unit', 'Sky', 'Time'])

    return tempdf.to_dict('records')

#print(getTemperature('Mumbai'))


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    while True:
        await asyncio.sleep(5)
        #print(getTemperature('Mumbai'))
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
        )
        async with producer:
            # Create a batch.
            event_data_batch = await producer.create_batch()

            # Add events to the batch.
            event_data_batch.add(EventData(json.dumps(getTemperature('Mumbai'))))

            # Send the batch of events to the event hub.
            await producer.send_batch(event_data_batch)
            print('Data sent successfully to eventhub!')

# asyncio.run(run())
# loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

try:
    asyncio.ensure_future(run())
    loop.run_forever()

except KeyboardInterrupt:
    pass

finally:
    loop.close()