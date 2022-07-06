FROM jekyll/jekyll:4.2.2 as build

RUN gem install bundler
RUN chown jekyll:jekyll -R /usr/gem

WORKDIR /srv/jekyll

COPY ./Gemfile .
COPY ./Gemfile.lock .

RUN bundle install


#RUN rm -rf Gemfile.lock
#RUN chmod -R 777 ${PWD}

#RUN bundle update


    # jekyll build && \
    # jekyll serve --livereload --drafts --trace

ARG build_command
ENV BUILD_COMMAND ${build_command}

CMD ${BUILD_COMMAND}

EXPOSE 4000