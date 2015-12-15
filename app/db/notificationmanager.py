from .models import Notification
from datetime import datetime
from app import database

from sqlalchemy import desc, update, and_

class NotificationDAO(object):

    @staticmethod
    def get_list(user):
        """
        Return all message.

        :return: List of message.
        """
        return database.session.query(Notification).filter(Notification.to_user==user)\
                .order_by(desc(Notification.date)).all()

    @staticmethod
    def insert_new_message(id, subject, message):
        if type(id) is list:
            for id_ in id:
                message = Notification(id_, subject, message, datetime.now())
                database.session.add(message)
            database.session.commit()
        else:
            message = Notification(id_, subject, message, datetime.now())
            database.session.add(message)
            database.session.commit()
        

    @staticmethod
    def get_new_mails_count(user):
        return database.session.query(Notification).filter(and_(Notification.read==0,\
                                                           Notification.to_user==user)).count()

    @staticmethod
    def refreshRead(mid, val):
        database.session.execute(
            update(Notification).where(Notification.id == mid).values(
                read=val
            )
        )

        database.session.commit()

        return True

    @staticmethod
    def delete(mid):
        Notification.query.filter_by(id=mid).delete()
        database.session.commit()
