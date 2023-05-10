diagram:
	rm -rf diagrams
	mkdir diagrams
	pyreverse -o png . -d diagrams


black:
	black --line-length 120 .
