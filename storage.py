import Utils
import Api
import json

noFile =FileNotFoundError
emptyFile =json.JSONDecodeError

def save_city(city) :
    if city == None :
        return "failed"
    while  True:
        try :
            with open("saved_cities.json", "r") as f :
                extract = json.load(f)
        except (noFile, emptyFile) :
            initialize_cities()
        else :
            extract.setdefault(city, "True")
            print(extract[city])
            with open("saved_cities.json", "w") as f :
                json.dump(extract, f, indent=4)
            return "saved"

def settings() :
    with open("options.json" , "r" ) as f :
        options = json.load(f)
        for key , value in options.items() :
            print(f"{key} = {value}")

def Configure(args) :
    key = args[0]
    value = args[1]
    print(value)
    with open("options.json", "r") as f : 
        options = json.load(f)
        configured = options
    try : 
     if int(value) in range(0, 2) :
        configured[key] = value
        print(configured[key])
        with open("options.json", "w") as f : 
            json.dump(configured, f, indent=4)
     else : 
        print("ERROR, the value is not in range 0-1 ")
    except : 
        print("ERROR, try entering exact spells as the option")
        with open("options.json", "w") as f :
            json.dump(options, f, indent = 4)

def find_city() :
    try :
        with open("saved_cities.json", "r") as f :
            locations = json.load(f)
            for key in locations :
                if key.strip() != "" :
                    response = Api.request(key.strip())
                    store_response(response)
                    Utils.display()
    except (noFile, emptyFile) :
        initialize_cities()
        return None

def initialize_cities() : 
    with open("saved_cities.json", "w") as f :
        data = {}
        json.dump(data, f)

def list() :
    try : 
        with open("saved_cities.json", "r") as f :
            locations = json.load(f)
            for key in locations :
                print(key.strip())
    except (noFile, emptyFile) :
        initialize_cities()
        print("Empty")

def remove_city (city) :
    try :
        with open("saved_cities.json", "r") as f :
            locations = json.load(f)
    except (noFile, emptyFile) :
        initialize_cities()
        print("Empty")
    else :
        removed = False
        configured_locations = {}
        with open("saved_cities.json", "w") as f :
            for key , value in locations.items() :  
                if key.strip().lower() != city.strip().lower() :
                    configured_locations[key] = value
                else :
                    removed = True
            json.dump(configured_locations, f, indent=4)
        if removed == True :
            return "removed"
        else :
            return "City not found"
            
def store_response(response) :
    while  True:
        try :
            with open("response.json", "w") as f :
                json.dump(response,f)
                break
        except FileNotFoundError :
            open("response.json", "w") 
            close("response.json")
