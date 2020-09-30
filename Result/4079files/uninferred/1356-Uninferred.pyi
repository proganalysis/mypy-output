from app import db
from typing import Any, Optional

LIMITS: bool

class QuestionStatus(db.Model):
    user_id: Any = ...
    question_id: Any = ...
    word_id: Any = ...
    position: Any = ...
    created_on: Any = ...
    updated_on: Any = ...

class Query(db.Model):
    id: Any = ...
    user_id: Any = ...
    question_id: Any = ...
    word_id: Any = ...
    created_on: Any = ...
    updated_on: Any = ...

class Result(db.Model):
    user_id: Any = ...
    question_id: Any = ...
    word_id: Any = ...
    position: Any = ...
    guess: Any = ...
    correct: Any = ...
    fold: Any = ...
    created_on: Any = ...
    updated_on: Any = ...

class User(db.Model):
    id: Any = ...
    api_key: Any = ...
    email: Any = ...
    display_name: Any = ...
    question_statuses: Any = ...
    queries: Any = ...
    created_on: Any = ...
    updated_on: Any = ...

class Question(db.Model):
    id: Any = ...
    qb_id: Any = ...
    words: Any = ...
    n_words: Any = ...
    answer: Any = ...
    fold: Any = ...
    created_on: Any = ...
    updated_on: Any = ...
    @staticmethod
    def id_translations(): ...

class Word(db.Model):
    id: Any = ...
    position: Any = ...
    question_id: Any = ...
    text: Any = ...
    created_on: Any = ...
    updated_on: Any = ...

class QuizBowl:
    @staticmethod
    def user_answer_pairs(): ...
    @staticmethod
    def handle_word_request(user_id: Any, question_id: Any, position: Any): ...
    @staticmethod
    def submit_guess(user_id: Any, question_id: Any, guess: Any): ...
    @staticmethod
    def create_user(email: Any, api_key: Any): ...
    @staticmethod
    def check_auth(user_id: Any, api_key: Any): ...
    @staticmethod
    def num_questions(fold: Optional[Any] = ...): ...
    @staticmethod
    def question_length(question_id: Any): ...
    @staticmethod
    def question_statuses(user_id: Any): ...
    @staticmethod
    def list_questions(): ...
    @staticmethod
    def get_buzzes(): ...
    @staticmethod
    def get_scores(): ...

def load_questions(filename: str = ...) -> None: ...