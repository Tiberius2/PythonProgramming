

from unittest import result


def findLoop(mapping):
    resultingList = []
    d_key = mapping['start']
    while mapping[d_key] not in resultingList:
        resultingList.append(d_key)
        d_key = mapping[d_key]
    return resultingList


mapping = {
  'start': 'a',
  'b': 'a',
  'a': '6',
  '6': 'z',
  'x': '2',
  'z': '2',
  '2': '2',
  'y': 'start'
}


print(findLoop(mapping))