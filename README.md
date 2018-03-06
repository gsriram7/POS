# Part of Speech Tagger

The tagger uses Hidden Markov Model to encode the a language corpus with words tagged with corresponding tags.
Uses Viterbi algorithm to decode and tag sentences from test data.

The encoder is generic and it works for ANY language.

The encoder models the [corpus](en_train_tagged.txt) and writes the probabilities into [hmmmodel.txt](hmmmodel.txt)
The decoder consumes the model and tags the [test data](en_dev_raw.txt) and writes the output into [hmmoutput.txt](hmmoutput.txt)

## Accuracy for the model trained on given corpa

 English  - 88.93%
 Chinese  - 87.08%
 Hindi    - 92.34%
 
 These accuracies are obtained using a single generic encoder for 3 different languages.
