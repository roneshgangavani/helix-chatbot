import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class QnACosineSimilarityBot:
    def __init__(self, qna_pairs):
        self.qna_pairs = qna_pairs
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform([pair[0] for pair in qna_pairs])
    
    def get_answer(self, user_question):
        user_question_vector = self.vectorizer.transform([user_question])
        
        similarity_scores = cosine_similarity(user_question_vector, self.question_vectors)
        most_similar_question_index = np.argmax(similarity_scores)
        
        return self.qna_pairs[most_similar_question_index][1]



