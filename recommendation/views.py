import os

import jwt
import pandas as pd
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from book_recommender import settings
from books.models import Book
from books.serializers import BookMetaInfoSerializer
from books.views import StandardResultsSetPagination
from users.models import User


def combined_features(data):
    features = []
    for i in range(0, data.shape[0]):
        features.append(
            str(data['original_title'][i]) + ' ' +
            str(data['authors'][i]) + ' ' +
            str(data['genre'][i])
        )
    return features


# requires book_id on which books will be recommended & count of recommendation returns list of recommended book_id
def get_recommendation(selected_book_id, count):
    book_data = os.path.join(settings.STATICFILES_DIRS[0] + '/books.csv')
    df = pd.read_csv(book_data, encoding='unicode_escape', error_bad_lines=False)

    # create a column to store combined features
    df['combined_features'] = combined_features(df)
    # df.describe()

    # Convert the text from combined_features to a matrix of word counts
    cm = CountVectorizer().fit_transform(df['combined_features'])

    # get cosine similarity matrix from the count matrix
    cs = cosine_similarity(cm)
    # print(cs)

    # selected_title = df['original_title'][selected_book_id]
    # create a list of tuples in the form of (book_id, similarity score)

    # print(cs[selected_book_id])
    scores = list(enumerate(cs[selected_book_id]))

    # sort the list of similar books in desc order
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]
    # print(sorted_scores)

    # create a loop to print the first 5 books from sorted list
    j = 0
    recommendations = []
    # print('Most recommended books to ' + selected_title + ' are: \n')
    for item in sorted_scores:
        recommendations.append(item[0])
        j = j + 1
        if j >= count:
            break

    recommended_books = []
    for book_id in recommendations:
        # print(book_id, ": ", df['original_title'][book_id])
        recommended_books.append(df['original_title'][book_id])
    return recommended_books


class GetRecommendationsView(generics.ListAPIView):
    queryset = Book.objects.values('book_id')
    serializer_class = BookMetaInfoSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        token = self.request.headers.get('Authentication')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        if user:
            ids = []
            recommendation_titles = []

            for books in user.library.all():
                if books.book_id < 8000:
                    ids.append(books.book_id)

            for input_book_id in ids:
                for i, bk_id in enumerate(get_recommendation(input_book_id, 5)):
                    recommendation_titles.append(bk_id)

            # print("RECOMM:", recommendation_titles)
            recommended_books_query_set = []
            for book_title in recommendation_titles:
                recommended_books_query_set.extend(list(Book.objects.filter(original_title=book_title)))

            return recommended_books_query_set
        else:
            raise AuthenticationFailed('Unauthenticated')
