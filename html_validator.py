import os
import sys
import requests
from termcolor import colored

validator = "https://validator.w3.org/nu/?out=json"

def dfs(file_name, files=[]):
    if os.path.isdir(file_name):
        for f in os.listdir(file_name):
            dfs(file_name+"/"+f)
    else:
        if file_name.endswith(".html"):
            files.append(file_name)
    return files

def validate_page(file):
    res = requests.post(
        validator,
        data={
                "out": "json",
                "showsource": "yes",
            },
        files={
            "file": (file, open(file, "rb"), "text/html")
        }
    )
    
    if res.status_code != 200:
        print(colored("ERROR", "red"), "->", validator, "returned code", res.status_code)
        print(res)
    
    parsed = res.json()

    if len(parsed["messages"]) == 0:
        print(file, colored("OK", "green"))
        return 0
    else:
        print(file)

    for m in parsed["messages"]:
        err_msg = colored(file, "blue") + " "
        err_msg += "[" + colored(m["type"], "red")
        if "subType" in m:
            err_msg += "|" + colored(m["subType"], "yellow")
        err_msg += "]"
        if "lastLine" in m:
            err_msg += ":" + colored(str(m["lastLine"]), "green")
        err_msg += " -> " + m["message"]
        print(err_msg)
        if "extract" in m:
            print("--- source ---")
            print(colored(m["extract"], "cyan"))
            print("--- end source ---")
    
    return len(parsed["messages"])

def main():
    build_dir = "./build"
    html_files = dfs(build_dir)

    errors = 0

    # add "https://localhost:4000" to each link that starts with "/"
    for page in html_files:
        errors += validate_page(page)

    if errors > 0:
        print("\n", colored(errors, 'red'), "errors found")
        sys.exit(-1)
    else:
        print("\n", colored(errors, 'green'), "errors found")
        sys.exit(0)

if __name__ == "__main__":
    main()