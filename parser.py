import sys
import os

def file_to_list(filename):
  with open(filename) as f:
    _list = [line.strip('\n') for line in f.readlines()]
  return _list

def parse(topics, percentages, response_choices):
  ethnicities = [
    'Asian Indian',
    'Chinese',
    'Filipino',
    'Japanese',
    'Korean',
    'Vietnamese',
    'Total'
  ]

  parsed = []

  for i, topic_name in enumerate(topics):
    topic = {
      'topic': topic_name,
      'responses': {}
    }
    for j, response_choice in enumerate(response_choices):
      topic['responses'][response_choice] = {}
      for k, ethnicity in enumerate(ethnicities):
        index = i*len(response_choices)*len(ethnicities) + j*len(ethnicities) + k
        topic['responses'][response_choice][ethnicity] = percentages[index]
    parsed.append(topic)

  return parsed

if len(sys.argv) < 2:
  sys.exit('Missing directory path parameter')
else:
  path = sys.argv[1]

  topics_path = os.path.join(path, 'topics')
  percentages_path = os.path.join(path, 'percentages')
  response_choices_path = os.path.join(path, 'response_choices')

  topics = file_to_list(topics_path)
  percentages = file_to_list(percentages_path)
  response_choices = file_to_list(response_choices_path)

  print parse(topics, percentages, response_choices)

