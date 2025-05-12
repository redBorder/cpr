PACKAGE_NAME    ?= libcpr
VERSION         ?= $(shell git describe --abbrev=6 --tags master --always | sed 's/-/_/g')
BUILD_NUMBER    ?= 1
MOCK_CONFIG     ?= default
RESULT_DIR      ?= pkgs
LATEST          ?= master

all: rpm

# ensure the SOURCES directory exists
SOURCES:
	mkdir -p SOURCES

archive: SOURCES
	cd ../../ && \
	git archive --prefix=$(PACKAGE_NAME)-$(VERSION)/ \
	           -o $(CURDIR)/SOURCES/$(PACKAGE_NAME)-$(VERSION).tar.gz $(LATEST)

build_prepare: archive
	mkdir -p $(RESULT_DIR)
	rm -f $(RESULT_DIR)/$(PACKAGE_NAME)*.rpm

srpm: build_prepare
	/usr/bin/mock \
	  -r $(MOCK_CONFIG) \
	  --define "__version $(VERSION)" \
	  --define "__release $(BUILD_NUMBER)" \
	  --resultdir=$(RESULT_DIR) \
	  --buildsrpm \
	  --spec=$(PACKAGE_NAME).spec \
	  --sources=SOURCES
	@echo "======= Source RPM now available in $(RESULT_DIR) ======="

rpm: srpm
	/usr/bin/mock \
	  -r $(MOCK_CONFIG) \
	  --define "__version $(VERSION)" \
	  --define "__release $(BUILD_NUMBER)" \
	  --resultdir=$(RESULT_DIR) \
	  --rebuild $(RESULT_DIR)/$(PACKAGE_NAME)*.src.rpm
	@echo "======= Binary RPMs now available in $(RESULT_DIR) ======="

clean:
	rm -rf SOURCES $(RESULT_DIR)

