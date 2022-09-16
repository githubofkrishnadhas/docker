# using alpine latest as base image for docker image
FROM alpine:latest
MAINTAINER Krishnadhas
# RUN command is used to execute commands in a layer
#figlet is a package which will increase the fontsize
RUN apk add figlet
#CMD exec figlet -f script "Hi Docker"
ENTRYPOINT ["figlet"]
CMD ["Hello Docker!"]
