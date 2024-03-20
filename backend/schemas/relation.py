from .discussion import DiscussionRead
from .discussion_topic import DiscussionTopicRead
from typing import List

class DiscussionRelation(DiscussionRead):
    topics: List[DiscussionTopicRead] = []