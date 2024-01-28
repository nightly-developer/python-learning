import re

#pattern = r'^[\w\.\-\-]*\.[a-zA-Z]*$'
#pattern = r'^[1]?[0-9]:[0-5]?[0-9] ?[a|A|p|P][m|M]$'
#pattern = r'\([A-Z|0-9][A-Z|a-z|0-9]*\)'
#pattern = r' \d{5}\-?[\d{4}]?'
#pattern = r'\[(\d+)\]: (\w+)'
#pattern = r'[\d+|-]+'
#pattern = r'(\w+[a|e|i|o|u]{3,}\w+)'
#pattern = r'^#+' <--- Error
#pattern = r'(\b\d{3}\b)-(\b\d{3}\b-\b\d{4}\b)'
#pattern = r'(^Jul \d \d{2}:\d{2}:\d{2}).*\[(\d+)\]' 


def main():
  text = "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"
  pattern = r''
  search_result = re.search(pattern,text)
  result = f'{search_result[1]} pid:{search_result[2]}'
  print(result)

if __name__ == '__main__':
  main()
