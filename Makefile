build-w:
	python -m venv venv
	.\venv\Scripts\activate
	pip install -r requirements.txt
	echo "Successfully builded, run make start"
start-w:
	.\venv\Scripts\activate
	python app

build:
	python3 -m venv venv
	source .\venv\Scripts\activate
	pip install -r requirements.txt
	echo "Successfully builded, run make start"
start:
	source .\venv\Scripts\activate
	python3 app