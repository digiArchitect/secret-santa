#secret santa pairing!
import random
import json
santas = ["bob", "jeese", "luke", "gonzalio", "jackie", "beth", "like", "nona"]
name = santas[:]
random.shuffle(name)
match = {}
def sec_santas(name,santas,dic):
  i = 0
  for names in santas:
    x = 0
    pops = ''
    for val in name:
      if (santas[i] == name[x]):
        print("passed")
        x += 1
        continue
      else:
        pops = name[x]
        dic[santas[i]] = pops
        name.pop(x)
        break

    i += 1
  return dic
  
matrices = sec_santas(name,santas,match)
print(json.dumps(matrices, sort_keys=False, indent=4))


         