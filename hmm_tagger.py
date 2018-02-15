import utils as utils

file = open("en_train_tagged.txt", "r")

word_to_tags = {}
tag_to_words = {}
word_freq = {}
tag_freq = {}
word_and_tag_freq = {}
bigrams = {}


def get_bigram_freq_dict(first_tag, second_tag, bigrams_dict):
    temp = bigrams_dict.get(first_tag, {})
    bigram_freq = temp.get(second_tag, 0)
    temp[second_tag] = bigram_freq + 1
    return temp


for line in file.readlines():
    line = line.strip("\n")
    first_tag = "start_213"
    end_tag = "end_146"
    for word in line.split(" "):
        (w, tag) = utils.split_word_from_tag(word)
        second_tag = tag

        bigrams[first_tag] = get_bigram_freq_dict(first_tag, second_tag, bigrams)

        w_and_tag = w + "/" + tag

        word_freq[w] = word_freq.get(w, 0) + 1
        tag_freq[tag] = tag_freq.get(tag, 0) + 1
        word_and_tag_freq[w_and_tag] = word_and_tag_freq.get(w_and_tag, 0) + 1

        t_for_a_w = word_to_tags.get(w, set())
        t_for_a_w.add(tag)
        word_to_tags[w] = t_for_a_w

        w_for_a_t = tag_to_words.get(tag, set())
        w_for_a_t.add(w)
        tag_to_words[tag] = w_for_a_t

        first_tag = second_tag

    bigrams[first_tag] = get_bigram_freq_dict(first_tag, end_tag, bigrams)

file.close()

print word_to_tags['In']
print tag_to_words['IN']
print "Total tags %s" % len(tag_to_words)
print "Total unique words %s" % len(word_to_tags)
print word_to_tags.keys()
print tag_freq
print word_freq
print word_and_tag_freq
print sum(bigrams['start_213'].values())
print bigrams
