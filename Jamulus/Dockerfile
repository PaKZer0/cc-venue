FROM alpine:3.12 as builder
# based on https://github.com/grundic/jamulus-docker with minor improvements

RUN \
 echo "**** updating system packages ****" && \
 apk update

RUN \
 echo "**** install build packages ****" && \
   apk add --no-cache --virtual .build-dependencies \
        build-base \
        wget \
        curl \
        grep \
        qt5-qtbase-dev \
        qt5-qttools-dev \
        qtchooser

WORKDIR /tmp
RUN \
 echo "**** getting source code ****" && \
   export JAMULUS_VERSION=`curl -s https://api.github.com/repos/corrados/jamulus/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")'` && \
   wget "https://github.com/corrados/jamulus/archive/${JAMULUS_VERSION}.tar.gz" && \
   tar xzf ${JAMULUS_VERSION}.tar.gz; echo $JAMULUS_VERSION > /tmp/version

RUN ls /tmp; JAMULUS_VERSION=$(cat /tmp/version); echo $JAMULUS_VERSION

# Github directory format for tar.gz export
WORKDIR /tmp/
RUN \
 echo "**** compiling source code ****" && \
   JAMULUS_VERSION=$(cat /tmp/version); \
   cd jamulus-${JAMULUS_VERSION}; \
   qmake "CONFIG+=nosound headless" Jamulus.pro && \
   make clean && \
   make && \
   cp Jamulus /usr/local/bin/ && \
   rm -rf /tmp/* && \
   apk del .build-dependencies

FROM alpine:3.12

RUN apk add --update --no-cache \
    qt5-qtbase-x11 icu-libs tzdata

COPY --from=builder /usr/local/bin/Jamulus /usr/local/bin/Jamulus
ENTRYPOINT ["Jamulus"]
