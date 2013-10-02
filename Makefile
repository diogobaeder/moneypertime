MANAGE=python manage.py

DATA_STORES=moneypertime/stores/stores.json


build: test

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver 8888

dump-stores:
	$(MANAGE) dumpdata stores | python -m json.tool > $(DATA_STORES)

load-stores:
	$(MANAGE) loaddata $(DATA_STORES)

fix-stores:
	DATA_STORES=$(DATA_STORES) $(MANAGE) fix_stores

rebuild-db:
	rm moneypertime.db
	$(MANAGE) syncdb
	make load-stores
	make fix-stores
