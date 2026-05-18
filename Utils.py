import json
def display() :
    with open("response.json", "r") as f :
        response = json.load(f)
    marked = {
                "lon": response["coord"]["lon"],
                "lat": response["coord"]["lat"],
                "id" : response["weather"][0]["id"],
                "main" : response["weather"][0]["main"],
                "description" : response["weather"][0]["description"],
                "temp" : round(float(response["main"]["temp"]) - 273.15, 2),
                "feels_like" : round(float(response["main"]["feels_like"]) -273.15, 2),
                "temp_min" : round(float(response["main"]["temp_min"]) -273.15, 2),
                "temp_max" : round(float(response["main"]["temp_max"]) -273.15, 2),
                "humidity" : response["main"]["humidity"],
                "wind_speed" : response["wind"]["speed"],
                "name" : response["name"]
    }
    with open("options.json", "r") as f:
        print (f"------------------------- {marked.get("name")} -------------------------")
        options = json.load(f)
        for key, value in options.items() :
            if str(value) == "1" :
                if key in marked :
                    print (f"{key} : {marked[key]}")

    for gap in range (5) :
        print ("                                                           ")

