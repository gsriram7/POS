file = open("en_train_tagged.txt", "r")

word_to_tag = {}
tag_to_words = {}

count = 0
for line in file:
    count += 1
    for word in line.split(" "):
        split = word.split("/")
        w = split[0]
        tag = split[1]

        t_for_a_w = word_to_tag.get(w, set())
        t_for_a_w.add(tag)
        word_to_tag[w] = t_for_a_w

        w_for_a_t = tag_to_words.get(tag, set())
        w_for_a_t.add(w)
        tag_to_words[tag] = w_for_a_t

print count
print word_to_tag['In']
print tag_to_words['IN']
print "Total tags %s" % len(tag_to_words)
print "Total unique words %s" % len(word_to_tag)