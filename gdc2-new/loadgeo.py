import os
import logging
import argparse

from sqlalchemy import func,distinct,create_engine
from sqlalchemy.orm import sessionmaker

from models import Base,GitHubEvent,get_login_location
from archiveparser import GitHubArchiveParser
import time


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)



if __name__ == '__main__':

    echo = False

    engine = create_engine('sqlite:///github-events-new.db', echo=echo)
    Base.metadata.create_all(engine)  # creates if not exists
    Session = sessionmaker(bind=engine)
    session = Session()

    logins = session.query(distinct(GitHubEvent.actor_login))

    for loginRec in logins.all():
      login = loginRec[0]
      print login
      events = session.query(GitHubEvent).filter(GitHubEvent.actor_login == login).all()
      print len(events)
      for event in events:
        event.actor_location = get_login_location(login)
      session.add_all(events)
      session.commit()
      time.sleep(1)
