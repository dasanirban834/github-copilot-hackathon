def description(WeatherCode):
    if WeatherCode.startswith('2'):
        data = {
            "200": "Thunderstorm with light rain: 0.25 mm – 1 mm per hour \
                ",
            "201": "Thunderstorm with rain: 1 mm – 4 mm per hour 💨🌧️",
            "202": "Thunderstorm with heavy rain: 4 mm – 8 mm per hour🌪️⛈️",
            "210": "Light thunderstorm: 0.25 mm – 1 mm per hour 💨",
            "211": "Thunderstorm: 1 mm – 4 mm per hour🌪️",
            "212": "Heavy thunderstorm: 4 mm – 8 mm per hour🌪️",
            "221": "Ragged thunderstorm: 4 mm – 8 mm per hour",
            "230": "Thunderstorm with light drizzle: 0.25 mm – 1 mm per hour🌨️",
            "231": "Thunderstorm with drizzle: 1 mm – 4 mm per hour🌨️🌨️",
            "232": "Thunderstorm with heavy drizzle: 4 mm – 8 mm per hour⛈️⛈️"
        }
        Safety_Tips = '\n1. Postpone outdoor activities until the storms have passed. \n2. Avoid open spaces, isolated objects, high ground and metallic objects. \n3. Stay off corded phones, computers and other electrical equipment that put you in direct contact with electricity. \n4. Avoid plumbing, including sinks, baths and faucets.'
        s1 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s1} {Safety_Tips}")

    elif WeatherCode.startswith('3'):
        data = {
            "300": "Light intensity drizzle: 0.25 mm – 1 mm per hour",
            "301": "Drizzle: 1 mm – 4 mm per hour",
            "302": "Heavy intensity drizzle: 4 mm – 8 mm per hour",
            "310": "Light intensity drizzle rain: 0.25 mm – 1 mm per hour",
            "311": "Drizzle rain: 1 mm – 4 mm per hour",
            "312": "Heavy intensity drizzle rain: 4 mm – 8 mm per hour",
            "313": "Shower rain and drizzle: 1 mm – 4 mm per hour",
            "314": "Heavy shower rain and drizzle: 4 mm – 8 mm per hour",
            "321": "Shower drizzle: 1 mm – 4 mm per hour"
        }
        Safety_Tips = '\n1. Please carry an umbrella or raincoat with you. \n2. Please drive carefully and slowly. \n3. Try to slow your vehicle by taking your foot off the accelerator earlier than you normally would in preparation to slow down or stop.'
        s2 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s2} {Safety_Tips}")

    elif WeatherCode.startswith('5'):
        data = {
            "500": "Light rain: 0.25 mm – 1 mm per hour",
            "501": "Moderate rain: 1 mm – 4 mm per hour",
            "502": "Heavy rain: 4 mm – 8 mm per hour",
            "503": "Very heavy rain: 8 mm – 16 mm per hour",
            "504": "Extreme rain: > 16 mm per hour",
            "511": "Freezing rain: < 0 °C (32 °F)",
            "520": "Light intensity shower rain: 0.25 mm – 1 mm per hour",
            "521": "Shower rain: 1 mm – 4 mm per hour",
            "522": "Heavy intensity shower rain: 4 mm – 8 mm per hour",
            "531": "Ragged shower rain: 4 mm – 8 mm per hour"
        }
        Safety_Tips = '\n1. Turn on your lights. \n2. Rain makes it harder for other drivers to see your vehicle, so make sure to turn on your headlights. \n3. Slow down. Increase your following distance.'
        s3 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s3} {Safety_Tips}")

    elif WeatherCode.startswith('7'):
        data = {
            "701": "Mist",
            "711": "Smoke",
            "721": "Haze",
            "731": "Sand/dust whirls 💨",
            "741": "Fog 🌫",
            "751": "Sand 💨",
            "761": "Dust 💨",
            "762": "Volcanic ash",
            "771": "Squalls",
            "781": "Tornado 🌪"
        }
        Safety_Tips = '\n1. When the outdoor air quality appears to be worsening, close doors and windows. \n2. If you have an air conditioner, turn it to recirculate. \n3. If you have a portable air cleaner, turn it on. \n4. Must wear N95 masks or any doctor prescribed masks to protect body from airbone particles'
        s4 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s4} {Safety_Tips}")

    elif WeatherCode.startswith('8') and WeatherCode != "800":
        data = {
            "801": "Few clouds: 11-25% ☁️",
            "802": "Scattered clouds: 25-50% ☁️",
            "803": "Broken clouds: 51-84% ☁️",
            "804": "Overcast clouds: 85-100% ☁️"
        }
        Safety_Tips = '\n1. It is better to carry umbrella to protect from sunlights as well as from sudden rain as there can be slight chances of little or moderate rain.'
        s5 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s5} {Safety_Tips}")

    elif WeatherCode == "800":
        data = {
            "800": "Clear sky ☀️"
        }
        Safety_Tips = '\n1. Wear sunglasses to protect eyes from UV rays. \n2. Also try to weat light clothes to protect from sunlights.There is no chance of rain.'
        s6 = '\x1B[1m' + 'Safety Tips:' + '\x1B[0m'
        print(f"Weather Category: {data[WeatherCode]}\n\n{s6} {Safety_Tips}")