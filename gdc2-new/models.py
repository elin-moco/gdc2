from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
import urllib2
import json
from github import Github
from geocoder import get_country


Base = declarative_base()
loginLocations = {}

def get_login_location(login):
  if login in loginLocations:
    return loginLocations[login]
  try:
    gh = Github('elin-moco', '0315oshb5975')
    user = gh.get_user(login)
    country = get_country(user.location)
    loginLocations[login] = country
    return loginLocations[login]
  except:
    loginLocations[login] = ''
    return ''


class GitHubEvent(Base):
    __tablename__ = 'event'

    pk = Column(Integer, primary_key=True)
    id = Column(Integer, index=True, unique=False)
    url = Column(String)
    created_at = Column(String, index=True, unique=False)
    type = Column('type', String, index=True, unique=False)
    actor_id = Column(String)
    actor_login = Column(String)
    actor_gravatar_id = Column(String)
    actor_location = Column(String, index=True, unique=False)
    repo_name = Column(String)
    repo_url = Column(String, index=True, unique=False)

    def __init__(self, **kwargs):
        for k in kwargs:
            if isinstance(kwargs[k], basestring):
                kwargs[k].strip()
            setattr(self, k, kwargs[k])
        # self.actor_location = get_login_location(self.actor_login)

