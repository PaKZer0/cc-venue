FROM golang:1.16beta1-alpine3.12

WORKDIR /app

RUN apk add git make gcc g++ binutils-gold; \
	git clone https://github.com/kiwiirc/webircgateway.git ; \
	cd webircgateway/ ; go build; cp config.conf.example config.conf ;\
	sed -i 's/irc.example.net/irc/' config.conf
	

ENTRYPOINT ["/app/webircgateway/webircgateway", \
				"--config=/app/webircgateway/config.conf"]
