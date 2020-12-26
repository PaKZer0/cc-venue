FROM node:12-alpine3.12

WORKDIR /app

RUN apk add git python3 make g++; \
	git clone https://github.com/kiwiirc/kiwiirc.git ; \
	cd kiwiirc/ ; yarn install; yarn run build

ADD copy-bundle.sh copy-bundle.sh
RUN chmod +x copy-bundle.sh

ENTRYPOINT ["/app/copy-bundle.sh"]
