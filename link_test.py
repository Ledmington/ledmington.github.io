import os
import re
import sys
import requests
from termcolor import colored

url_regex = (
    r"<a\s+?(?:[\w\-\"\=]+\s+?)?href=\"?((?:https?:\/\/)?(?:[\w\d.:\/]+?))\"?\s*?>"
)


def print_broken_link(link, page, error_code):
    print(
        "Link",
        colored('"' + link + '"', "blue"),
        "in file",
        colored('"' + page + '"', "blue"),
        "received code",
        colored(str(error_code), "red"),
    )


def dfs(file_name, files=[]):
    if os.path.isdir(file_name):
        for f in os.listdir(file_name):
            dfs(file_name + "/" + f)
    else:
        if file_name.endswith(".html"):
            files.append(file_name)
    return files


def check_url(url, file):
    res = requests.get(url)
    c = res.status_code

    if not c == 200:
        print_broken_link(url, file, c)
        return 1
    else:
        return 0


def main():
    build_dir = "./build"
    html_files = dfs(build_dir)

    tot_broken_links = 0
    for file in html_files:
        with open(file) as f:
            urls = re.findall(url_regex, f.read())
        
        curr_broken_links = 0
        for url in urls:
            # add "http://localhost:4000" to each link that starts with "/"
            if url.startswith("/"):
                url = "http://localhost:4000" + url
            curr_broken_links += check_url(url, file)
        
        if curr_broken_links == 0:
            print(file, colored("OK", 'green'))
        
        tot_broken_links += curr_broken_links

    if tot_broken_links > 0:
        print("\n", colored(tot_broken_links, "red"), "broken links found")
        sys.exit(-1)
    else:
        print("\n", colored(tot_broken_links, "green"), "broken links found")
        sys.exit(0)


if __name__ == "__main__":
    main()
