## Using Docker :

Building the Image :

`docker build -t my-devlopr-jekyll-blog .`

Running the container :

`docker run -d -p 4000:4000 -it --volume="$PWD:/srv/jekyll" --name "my_blog" my-devlopr-jekyll-blog:latest jekyll serve --watch`

## Using Docker Compose :

### Development :

You can run the app in development mode : (your changes will be reflected --watch moded)

Serve the site at http://localhost:4000 :

`docker-compose -f docker-compose-dev.yml up --build --remove-orphans`

### Production :

You can run the app in production mode : (your changes will be reflected --watch moded)

Serve the site at http://localhost:4000 :

`docker-compose -f docker-compose-prod.yml up --build --remove-orphans`

Stop the app :
`docker-compose -f docker-compose-prod.yml down`
Once everything is good and ready to go live -

`docker-compose -f docker-compose-prod.yml up --build --detach`


## For local development

#### Install Ruby
Ruby is needed to make Jekyll work. Check if you already have it with `ruby -v`. If not, run `apt install ruby-full`.

#### Install bundler
Bundler is the Ruby package manager. Check if you already have it with `bundler -v`. If not, run `gem install bundler`.

#### Fire up the website locally
The first time on a new machine, run `make install` to make bundler install all the dependencies.

Then run `make serve` all other times to run the server locally.

#### Update dependencies
Run `make update`.

## Open admin dashboard
Local dashboard: http://localhost:4000/admin

Actual remote dashboard: https://ledmington.github.io/admin and then login via GitHub.

## Add an image
All images are stored inside `assets/img`. Images used in posts (not thumbnails) have to be stored inside `assets/img/posts`. Authors' profile picture has to be stored inside `assets/img/authors`.

If possible, try to keep an aspect ratio of 2:1 in all images to avoid weird post stretching in the `blog` page.

## Add a post
[Jekyll docs](https://jekyllrb.com/docs/posts/)

For helpful Markdown tricks, check the `old/posts/styleguide.md` file.

For post examples, check the `old/posts` directory.

A post's filename must (apparently) follow the convention `YYYY-MM-DD-name-of-post.md`.

The thumbnail of the post must be in the `/assets/img` directory and the `thumbnail` tag must be the complete path to the image.

To add a post without visualizing it, add `published: false` in the preamble.

## Add an author
You need to create a new `<author-name>.md` file inside the `_authors` folder. Check the template inside the `old/authors` folder to know what informations to write. The profile picture must be inside the `assets/img/authors` folder. To add more information about an author (like projects, social ecc.) add him/her in the `_data/authors.yml` file. To know what to write, check the old template inside the `old/data/_authors.yml`.

## Add a category
TODO

## Modify skills
For now, skills are hard-coded into the `_includes/author_skills.html` file. [Here](https://www.aleksandrhovhannisyan.com/blog/getting-started-with-jekyll-and-github-pages/#example-1-skills-and-abilities) explains how to have some more dynamic skills.

## More Jekyll themes
[Here](http://jekyllthemes.org/)