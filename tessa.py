import urllib.error, urllib.request, urllib.parse
import json

class Weather:

    def print_forecasts(self, long, lat):

        api_url = f"http://www.7timer.info/bin/api.pl?lon={long}&lat={lat}&product=astro&output=json"

        # load weather data from API
        data = urllib.request.urlopen(api_url).read()
        data_dict = json.loads(data)
        
        dataseries = data_dict['dataseries']
        # iterate over all data series
        for series in dataseries:

            # build weather forecast string
            forecast = f"temp { series['temp2m'] }"

            print(forecast)

weather = Weather()
print("Here is today's weather!")
forecast = weather.print_forecasts(-1.7268826, 55.002352)