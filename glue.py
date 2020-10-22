import os
import json

sections = []
for directory in os.scandir('sections/'):
	section_name = directory.name
	with open('sections/{}/{}.json'.format(section_name, section_name)) as section_file: 
		section = json.load(section_file)

	widgets = []
	for item in os.scandir('sections/{}'.format(section_name)):
		if item.name != '{}.json'.format(section_name):
			with open('sections/{}/{}'.format(section_name, item.name)) as widget_file:
				widgets.append(json.load(widget_file))

	section['widgets'] = widgets
	sections.append(section)

with open('content.json', 'w') as content_file:
	json.dump({'sections': sections}, content_file)