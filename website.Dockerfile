FROM ubuntu:21.10

RUN apt update -y
RUN apt upgrade -y

COPY . ./website

RUN apt install ruby-full -y

RUN gem install bundler

WORKDIR /website

RUN bundle update
RUN bundle add jekyll
RUN bundle install

CMD bundle exec jekyll serve --watch

EXPOSE 4000