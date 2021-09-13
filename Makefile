# just type make to compile

build:
	docker run --rm -it -v "${PWD}"/lectures:/src dgrnwd/teachingslides:latest
