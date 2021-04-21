run:
	docker run -d --restart=always \
		-p 127.0.0.1:2376:2375 \
		-v /var/run/docker.sock:/var/run/docker.sock \
		--name socat \
		alpine/socat \
		tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock

stop:
	docker stop socat

start:
	docker start socat

clean:
	docker rm socat