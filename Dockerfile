FROM jekyll/jekyll:stable as builder

WORKDIR /srv/jekyll

ADD . /srv/jekyll

RUN gem install bundler
RUN rm -rf Gemfile.lock
RUN chmod -R 777 ${PWD} -v
RUN bundle update
RUN bundle install

    # jekyll build && \
    # jekyll serve --livereload --drafts --trace

ARG build_command
ENV BUILD_COMMAND ${build_command}

CMD ${BUILD_COMMAND}

EXPOSE 4000
