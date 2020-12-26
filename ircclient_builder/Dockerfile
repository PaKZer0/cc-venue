FROM node:12-alpine3.12

WORKDIR /app

ADD copy-bundle.sh copy-bundle.sh
RUN apk add git python3; chmod +x copy-bundle.sh ; \
	git clone https://github.com/kiwiirc/kiwiirc.git ; \
	cd kiwiirc/ ; yarn install; yarn run build

ENTRYPOINT ["/app/copy-bundle.sh"]
