# Basic-NLP-tasks

There are several basic nlp tasks for beginners to understand primitive but fundemantal approaches and algorithms used in Natural Language Processing.Even if these methods are not currently used they are important to
understand basics.

Task 1: A very simple example should be prepared to show how to do word sense
disambiguation using the LESK algorithm on a Turkish corpus.

Task 2 :First, low and high frequency words should be determined in
a Turkish collection. Words with low frequency will be assumed to have spelling errors.
To solve this problem, a Lexical Similarity function(In this task levenshtein distance has been used) will be used and
it will be suggested that these erroneous assumed words can change to the most lexically similar word from high-frequency words. The code to be
prepared must give a two-column list: low-frequency words in the first column and the
most lexically similar high-frequency words in the second column.

Task 3 : In this task the sentence in the corpus which is most similar to the sentence entered by the user is returned.
To measure similarity between sentences similarity method from spacy library has been used.
This method uses word vectors to measure similarity between sentences.

Task 4 : In this task code returns summary of the text.To extract summary first  high frequency word list has been created and the word has been  chosen from the top ten percent with the highest frequency.
Then sentences in the text which include these words has been chosen to create summary of the text.
