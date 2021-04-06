run:
	docker run -td \
		-p 8080:8080 \
		-v ${PWD}/jenkins_home:/var/jenkins_home \
		--name jenkins \
		jenkins/jenkins:lts

stop:
	docker stop jenkins
	docker rm jenkins

start:
	docker start jenkins
