all:
	@python3 ./diagnose-heart-anomaly.py dataset/spect-orig.train.csv dataset/spect-itg.train.csv dataset/spect-resplit-itg.train.csv
	@echo "Finish all"

itg:
	@python3 ./diagnose-heart-anomaly.py dataset/spect-itg.train.csv dataset/spect-resplit-itg.train.csv

orig:
	@python3 ./diagnose-heart-anomaly.py dataset/spect-orig.train.csv

resplit:
	@python3 ./diagnose-heart-anomaly.py dataset/spect-resplit-itg.train.csv