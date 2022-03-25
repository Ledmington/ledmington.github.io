### [Installation Guide](https://devlopr.netlify.app/get-started)

![devlopr jekyll](https://github.com/sujaykundu777/devlopr-jekyll/blob/master/assets/img/screenshot.PNG?raw=true)

devlopr uses Markdown Files to generate data like Blog Posts, Gallery, Shop Products etc. No external database is required.

### [Get Started Locally]

To get started follow this [tutorial](https://devlopr.netlify.app/get-started).Then follow the below commands to start the server locally at http://127.0.0.1:4000/.

```sh
$ git clone https://github.com/your_github_username/your_github_username.github.io.git
$ cd your_github_username
$ ruby -v
$ gem install bundler
$ bundler -v
$ bundle add jekyll
$ bundle exec jekyll -v
$ bundle update
$ bundle install
$ bundle exec jekyll serve --watch
```

### Deploy your devlopr-jekyll blog - One Click Deploy

[![Deploy with ZEIT Now](https://zeit.co/button)](https://zeit.co/new/project?template=https://github.com/sujaykundu777/devlopr-jekyll)
[![Deploy with Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/sujaykundu777/devlopr-jekyll)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sujaykundu777/devlopr-jekyll)

#### Jekyll Admin
You can easily manage the site locally using the Jekyll admin : [http://localhost:4000/admin](http://localhost:4000/admin)

![Jekyll Admin](https://github.com/sujaykundu777/devlopr-jekyll/blob/master/assets/img/jekyll-admin.PNG?raw=true)

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


### For local development
`bundle update`
`bundle install`
`bundle exec jekyll serve --drafts --unpublished --future --trace`

### Open admin dashboard
Local dashboard: [](http://localhost:4000/admin)
Actual remote dashboard: [](ledmington.github.io/admin) and then login via GitHub.

### Add an image

### Add a post
![Jekyll docs](https://jekyllrb.com/docs/posts/)

### Add an author

### Add a category

### Modify skills
For now, skills are hard-coded into the `_includes/author_skills.html` file. ![Here](https://www.aleksandrhovhannisyan.com/blog/getting-started-with-jekyll-and-github-pages/#example-1-skills-and-abilities) explains how to have some more dynamic skills.