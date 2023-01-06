import argparse
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

def main():
    parser = argparse.ArgumentParser(description = "A Python script to query LOLBAS: https://lolbas-project.github.io/.", add_help=True)
    parser.add_argument("-f", "--file", type=str, required=True, help="Query LOLBAS API for a specific file.")
    args = parser.parse_args()
    query_api(args.file)

def query_api(file):
    try:
        result = False
        for data in requests.get("https://lolbas-project.github.io/api/lolbas.json", verify=False).json():
            if data["Name"].upper() == file.upper():
                result = True
                print("")
                for key, value in data.items():
                    if key == "Commands":
                        i = 0
                        while i < len(data["Commands"]):
                            print("\nCategory: " + data["Commands"][i]["Category"])
                            print("Description: " + data["Commands"][i]["Description"])
                            print("Command: " + data["Commands"][i]["Command"])
                            print("Usecase: " + data["Commands"][i]["Usecase"])
                            print("Privileges: " + data["Commands"][i]["Privileges"])
                            print("OperatingSystem: " + data["Commands"][i]["OperatingSystem"])
                            print("MitreID: " + data["Commands"][i]["MitreID"])
                            i += 1
                        print("")
                    else:
                        if type(value) == list:
                            for key in data[key]:
                                for k, v in key.items():
                                    print(k,":",v)
                            print("")
                        else:
                            print(key,":",value)
                break
        if result == False:
            print(f"\n{file} was not found in LOLBAS.")
    except:
        print("\nAn unexpected error occured!")

if __name__ == "__main__":
    main()