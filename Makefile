redis:
	sudo docker run -p 6379:6379 -d redis
beat:
	python -m celery -A tasks beat -l error --detach --logfile="./tmp/tmp.log" --pidfile="./tmp/tmp.pid"
worker:
	python -m celery -A tasks worker -l info
worker-d:
	python -m celery -A tasks worker -l error --detach --logfile="./tmp/tmp.log" --pidfile="./tmp/tmp.pid"