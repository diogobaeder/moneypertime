MANAGE=python manage.py


build: test

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver 8888

dump-stores:
	$(MANAGE) dumpdata stores > moneypertime/stores/stores.json

load-stores:
	$(MANAGE) loaddata moneypertime/stores/stores.json