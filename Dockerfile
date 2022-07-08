FROM jekyll/jekyll:4.2.2

# setup Ruby 2.7 (because newer versions give errors)
# RUN curl -sSL https://get.rvm.io | bash
# RUN source /home/.rvm/scripts/rvm
# RUN rvm install 2.7
# RUN rvm use 2.7

RUN gem install bundler
RUN chown jekyll:jekyll -R /usr/gem

WORKDIR /srv/jekyll

COPY ./Gemfile .

RUN bundle install

RUN chmod -R 777 ${PWD}

#RUN bundle update


    # jekyll build && \
    # jekyll serve --livereload --drafts --trace

COPY . .

# ARG build_command
# ENV BUILD_COMMAND ${build_command}

# CMD ${BUILD_COMMAND}

EXPOSE 4000

RUN bundle update && bundle install
RUN bundle exec jekyll build --trace

CMD bundle exec jekyll serve --drafts --trace