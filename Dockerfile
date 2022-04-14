FROM jekyll/jekyll:3.8.6 as build

WORKDIR /srv/jekyll

ADD ./Gemfile /srv/jekyll

RUN gem install bundler
#RUN rm -rf Gemfile.lock
#RUN chmod -R 777 ${PWD}
RUN chown jekyll:jekyll -R /usr/gem
RUN bundle update
RUN bundle install

    # jekyll build && \
    # jekyll serve --livereload --drafts --trace

ARG build_command
ENV BUILD_COMMAND ${build_command}

CMD ${BUILD_COMMAND}

EXPOSE 4000