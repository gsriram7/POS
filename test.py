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

# with open('en_vince.json', 'r') as fp:
#     vince = json.load(fp)
#
# print vince[0]['emissionProbabilities']
# vince_data=vince[0]['emissionProbabilities']
#
# proc = 0
# for k in vince_data.keys():
#     for b in vince_data[k].keys():
#         proc+=1
#         try:
#             if (vince_data[k][b] != emission_probability[k.encode('ascii', 'ignore')][b.encode('ascii', 'ignore')]):
#                 w = [k.encode('ascii', 'ignore'), b.encode('ascii', 'ignore'), vince_data[k][b], emission_probability[k.encode('ascii', 'ignore')][b.encode('ascii', 'ignore')]]
#                 print "Wrong %s" % w
#         except Exception:
#             print "Exception while %s" % [k.encode('ascii', 'ignore'), b.encode('ascii', 'ignore')]
#
# print "Done with %s kvs" % proc