import os
import re
import sys
import requests

url_regex = r"<a\s+?(?:[\w\-\"\=]+\s+?)?href=\"?((?:https?:\/\/)?(?:[\w\d.:\/]+?))\"?\s*?>"

def dfs(file_name, files=[]):
	if os.path.isdir(file_name):
		for f in os.listdir(file_name):
			dfs(file_name+"/"+f)
	else:
		if file_name.endswith(".html"):
			files.append(file_name)
	return files

def check_url(url, file):
	res = requests.get(url)
	c = res.status_code

	if not c == 200:
		print("Link \""+url+"\" in file \""+file+"\" received code "+str(c))
		return 1
	else:
		return 0

def main():
	build_dir = "./build"
	html_files = dfs(build_dir)
	
	urls_to_check = []
	for file in html_files:
		with open(file) as f:
			urls = re.findall(url_regex, f.read())
		for url in urls:
			urls_to_check.append((url, file))

	broken_links_found = 0

	# add "https://localhost:4000" to each link that starts with "/"
	for t in urls_to_check:
		if t[0].startswith("/"):
			r = check_url("http://localhost:4000"+t[0], t[1])
		else:
			r = check_url(t[0], t[1])
		broken_links_found += r

	if broken_links_found > 0:
		print("\n", broken_links_found, "broken links found")
		sys.exit(-1)
	else:
		sys.exit(0)

if __name__ == "__main__":
	main()