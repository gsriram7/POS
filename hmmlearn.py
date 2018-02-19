import utils as utils
import json

file = open("zh_dev_tagged.txt", "r", encoding="utf8")

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

print("Total tags %s" % len(tag_to_words))
print("Total unique words %s" % len(word_to_tags))
print(tag_freq)
print(word_freq)
print(word_and_tag_freq)
print(sum(bigrams['start_213'].values()))
print(bigrams)


def compute_transition_probability(tag_bigrams):
    conditional_prob = {}
    for a in tag_bigrams.keys():
        for b in tag_bigrams.keys():
            temp = tag_bigrams.get(a, {})
            freq_a_b = temp.get(b, 0)
            # TODO: Instead of assigning 0, try to smooth it
            if freq_a_b != 0:
                sub_temp = conditional_prob.get(a, {})
                sub_temp[b] = float(freq_a_b) / float(sum(temp.values()) - temp.get(end_tag, 0))
                conditional_prob[a] = sub_temp
    return conditional_prob


transition_prob = compute_transition_probability(bigrams)

with open('en_tp.json', 'w') as fp:
    json.dump(transition_prob, fp, indent=4)
fp.close()


def compute_emission_probability(word_freq, tag_freq):
    emission_probability = {}
    for word in word_freq.keys():
        for tag in tag_freq.keys():
            temp = emission_probability.get(word, {})
            freq = word_and_tag_freq.get(word + "/" + tag, 0)
            if freq != 0:
                temp[tag] = float(freq) / float(tag_freq.get(tag, 1))
                emission_probability[word] = temp
    return emission_probability


emission_probability = compute_emission_probability(word_freq, tag_freq)

with open('en_emission.json', 'w') as fp:
    json.dump(emission_probability, fp, indent=4)
fp.close()

model = {}
model['transition_probability'] = transition_prob
model['emission_probability'] = emission_probability

with open('model.json', 'w', encoding='utf8') as fp:
    json.dump(model, fp, indent=4, ensure_ascii=False)
fp.close()

