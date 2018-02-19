import json
import utils

with open("/Users/selvaram/selva/POS/model.json", 'r') as fp:
    model = json.load(fp)
fp.close()

emission_probability = model['emission_probability']
transition_probability = model['transition_probability']

file = open("/Users/selvaram/selva/POS/assignment_dev_1.txt", 'r')


def get_probability_and_backpointer(transition_probability,
                                    emission_probability,
                                    old_prev_states,
                                    current_word, prev_prob):
    decoded = {}
    for curr_state in emission_probability[current_word].keys():
        max_tag_prob = 0
        back_pointer = ""

        for prev_state in old_prev_states:
            curr_state_prob = utils.get_or_default(transition_probability, [prev_state, curr_state], 0) \
                              * utils.get_or_default(emission_probability, [current_word, curr_state], 0) \
                              * utils.get_or_default(prev_prob, [prev_state, 'prob'], 0)

            if curr_state_prob > max_tag_prob:
                max_tag_prob = curr_state_prob
                back_pointer = prev_state

        if max_tag_prob != 0:
            decoded[curr_state] = {'prob': max_tag_prob, 'parent': back_pointer}

    return decoded


def get_top_tag(tags_for_word):
    temp = tags_for_word.values()[0]
    max_prob = 0
    tag = ''
    for key in temp.keys():
        prob = temp[key]['prob']
        if prob > max_prob:
            tag = key
            max_prob = prob

    return tag


def extract_tags(probs_with_backpointers):
    res = []
    top_tag = get_top_tag(probs_with_backpointers[-1])

    for dict in reversed(probs_with_backpointers):
        word = dict.keys()[0]
        res.append((word, top_tag))
        top_tag = dict[word][top_tag]['parent']

    return res


def format_output_line(list_of_tuples):
    res = ""
    for t in reversed(list_of_tuples):
        (word, tag) = t
        res += word + "/" + tag + " "

    return res.strip(" ")


c = 1
for line in file.readlines():
    viterbi = []
    line = line.strip("\n")
    prev_word = 'start_213'
    old_states = [prev_word]
    prev_state_prob = {prev_word: {'prob': 1}}
    state_number = 1
    for word in line.split(' '):
        try:
            curr_state_prob = get_probability_and_backpointer(transition_probability, emission_probability, old_states,
                                                              word, prev_state_prob)
        except Exception:
            print "Problem %s" % word
        old_states = curr_state_prob.keys()
        prev_state_prob = curr_state_prob
        # TODO: Store probabilities of words along with indices as duplicate words in a line will cause problems as it will overrite dict
        viterbi.append({word: prev_state_prob})
        prev_word = word
    print format_output_line(extract_tags(viterbi))
    print "Done %s" % c
    c += 1

file.close()
