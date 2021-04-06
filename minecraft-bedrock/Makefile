run:
	docker run -itd \
		-e EULA=TRUE \
		-p 19132:19132/udp \
		--name minecraft \
		itzg/minecraft-bedrock-server:latest

stop:
	docker stop minecraft
	docker system prune -f

restart: stop run