import Api
import Utils
import storage
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--w" , help = "...", action="store_true")
parser.add_argument("--search", help = "Search a location", type = str)
parser.add_argument("--save", help= "Save a city", type = str)
parser.add_argument("--remove", help = "Remove a city from saved", type = str)
parser.add_argument("--fav", help = "Displays weather of saved cities")
parser.add_argument("--list", "-l", help="Lists all saved cities", action = "store_true")
parser.add_argument("--settings" , help="Show settings", action="store_true")
parser.add_argument("-set" , help="Configure settings e.g lon 0, or lon 1 , Note 0 means false 1 means true" , nargs=2)
args : Namespace = parser.parse_args()


if  args.search != None :
    response = Api.request(args.search)
    if response != None :
        storage.store_response(response)
        Utils.display()
elif args.save != None :
    storage.save_city(Api.validate_city(args.save))
elif args.remove != None :
    print(storage.remove_city(args.remove))
if args.w :
    storage.find_city()
if args.list :
    storage.list()
if args.settings :
    storage.settings()
if args.set != None : 
    storage.Configure(args.set)

