tag_to_words = {}

out1 = open('out1.txt', 'w')

for k,v in tag_to_words.iteritems():
    for e in v:
        out1.write(e)
        out1.write('/')
        out1.write(k)
        out1.write("\n")
        out1.flush()

out1.close()

file = open("en_train_tagged.txt", "r")
raw1 = open('raw1.txt', 'w')

for line in file.readline():
    for word in line.split(" "):
        raw1.write(word)
        raw1.write("\n")
        raw1.flush()

raw1.close()

file.close()

import json

with open('en_vince.json', 'r') as fp:
    vince = json.load(fp)
fp.close()

with open('model.json', 'r') as fp:
    mine = json.load(fp)
fp.close()

emission_probability = mine['emission_probability']

print(vince[0]['emissionProbabilities'])
vince_data=vince[0]['emissionProbabilities']

proc = 0
for k in vince_data.keys():
    for b in vince_data[k].keys():
        proc+=1
        try:
            if (vince_data[k][b] != emission_probability[k][b]):
                w = [k, b, vince_data[k][b], emission_probability[k][b]]
                print("Wrong %s" % w)
        except Exception:
            print("Exception while %s" % [k, b])

print("Done with %s kvs" % proc)