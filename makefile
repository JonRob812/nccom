APP = nccom
UI_SRC_DIR = designer
UI_SRC_FILES = $(wildcard $(UI_SRC_DIR)/*.ui)
UI_FILES = $(patsubst $(UI_SRC_DIR)/%.ui, $(APP)/ui/%_ui.py, $(UI_SRC_FILES))

RESOURCE_QRC = resources.qrc
RESOURCES_DIR = $(APP)/resources
RESOURCES = $(RESOURCES_DIR)/camo_resources.py


.PHONY : ui
ui: $(UI_FILES)

$(APP)/ui/%_ui.py: $(UI_SRC_DIR)/%.ui
	rm -f $@
	pyuic5 -o $@ $<

.PHONY : resources
resource: $(RESOURCES)

$(RESOURCES) : $(RESOURCE_QRC)
	rm -f $@
	touch $(RESOURCES_DIR)
	pyrcc5 -o $@ $<