import sys

def main():
    name = input("Category name? ")
    link = input("Link to category? /blog/categories/")

    filename = "./categories/" + link + ".md"

    old_stdout = sys.stdout

    with open(filename, "w") as f:
        sys.stdout = f
        print("---")
        print("layout: page")
        print("title: " + name)
        print("permalink: /blog/categories/" + link + "/")
        print("---\n")
        print("<h5> Posts by Category : {{ page.title }} </h5>\n")
        print("<div class=\"card\">")
        print("{% for post in site.categories."+link+" %}")
        print(" <li class=\"category-posts\"><span>{{ post.date | date_to_string }}</span> &nbsp; <a href=\"{{ post.url }}\">{{ post.title }}</a></li>")
        print("{% endfor %}")
        print("</div>")
        sys.stdout = old_stdout
    
    print("\n\nGenerated file " + filename)

if __name__ == "__main__":
    main()