Weather-CLI

  A command-line weather app in Python that fetches current weather data and lets you save frequently checked cities.

What it does

  Fetches live weather data from a weather API for a given city and displays it in the terminal. Cities can be saved for quick repeat lookups, persisted locally so they're available across sessions.

Features
  Fetch current weather for any city
  , Save and manage a list of favorite cities
  , Persistent local storage (no need to re-enter cities each run)
  
Options

  -h, --help       show this help message and exit
  
  --w              Show weather of saved cities
  
  --search         Search a location
  
  --save           Save a city
  
  --remove         Remove a city from saved
  
  --fav            Displays weather of saved cities
  
  --list, -l       Lists all saved cities
  
  --settings       Show settings
  
  --set             Configure settings e.g lon 0, or lon 1 , Note 0 means false 1 means true
  
Setup

  bash "git clone https://github.com/slimyshit/Weather-CLI"
  
  cd Weather-CLI
  
  pip install requests python-dotenv
  
  You'll also need an API key from (https://openweathermap.org/api). Create a .env file in the project root:

  API_KEY=your_api_key_here

  .env is gitignored, so your key stays local and won't be pushed to GitHub.

Run

  python main.py --(one of the options listed above)

Architecture

  main.py — entry point, CLI interaction
  
  Api.py — handles requests to the weather API
  
  storage.py — saves/loads city list to saved_cities.json
  
  Utils.py — helper functions
  
  options.json — configuration

License
  MIT
