build:
	docker build . -t "rating_notification"
	docker create --name rating_notification rating_notification
start:
	docker run -d rating_notification
stop:
	docker stop rating_notification