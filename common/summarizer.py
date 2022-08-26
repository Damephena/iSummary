from collections import Counter
from heapq import nlargest
from typing import Dict, List, Optional

import en_core_web_sm

nlp = en_core_web_sm.load()

class Summarizer:
    word_frequencies = Counter()
    sentence_scores: Dict = {}
    top_sentences: List = []
    summary: str = ""

    def __init__(self, original_text: str, summary_size: Optional[int] = None) -> None:
        self.reset()
        self.docx = original_text
        self.document = nlp(self.docx)
        self.no_of_summary_text = summary_size

    def reset(self):
        self.word_frequencies = Counter()
        self.sentence_scores = {}
        self.top_sentences = []
        self.summary = ""
        self.docx = ""
        self.document = nlp(self.docx)
        self.no_of_summary_text = None

    def get_frequency_distribution(self):

        """Find weighted frequency via max frequency"""
        for token in self.document:
            if not token.is_stop and not token.is_punct:
                self.word_frequencies[token.text] += 1

        maximum_frequency = self.word_frequencies.most_common(1)[0][1]
        for word in self.word_frequencies.keys():
            self.word_frequencies[word] = (
                self.word_frequencies[word] / maximum_frequency
            )

        return self.word_frequencies

    def get_sentences_score(self):

        """Sentence score and ranking of words in each sentence
        - Scoring every sentence based on number of non stopwords in our word frequency table
        """
        for sent in self.document.sents:
            for word in sent:
                if (
                    word.lower_ in self.word_frequencies.keys()
                    and len(sent.text.split(" ")) < 30
                ):
                    if sent in self.sentence_scores:
                        self.sentence_scores[sent] += self.word_frequencies[word.lower_]
                    else:
                        self.sentence_scores[sent] = self.word_frequencies[word.lower_]
        self.sentence_scores = self.sentence_scores
        return self.sentence_scores

    def get_top_sentences(self):

        """Finding Top N sentence with the largest score"""
        if self.no_of_summary_text:
            print("GOT HERE OOOO")
            self.top_sentences = nlargest(
                self.no_of_summary_text,
                self.sentence_scores,
                key=self.sentence_scores.get,
            )
        else:
            self.top_sentences = nlargest(
                7, self.sentence_scores, key=self.sentence_scores.get
            )
        return self.top_sentences

    def text_summarizer(self) -> str:

        """Summarize text"""
        self.get_frequency_distribution()
        self.get_sentences_score()
        summarized_sentences = self.get_top_sentences()
        final_sentences = [word.text for word in summarized_sentences]

        self.summary = "".join(final_sentences)
        return self.summary

    def get_summary_length(self):
        return len(self.summary)

    def get_summary(self):
        return self.text_summarizer()
