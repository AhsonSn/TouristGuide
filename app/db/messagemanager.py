from .models import Message
from datetime import datetime
from app import database

from sqlalchemy import desc, update

class MessageDAO(object):

    @staticmethod
    def get_list():
        """
        Return all message.

        :return: List of message.
        """
        return database.session.query(Message).order_by(desc(Message.date)).all()

    @staticmethod
    def get_list_between_date(start, end):
        """
        Return all message between date.

        :param start: String that represent date: "2015-01-01 00:00:00"
        :param end: String that represent date: "2015-01-01 00:00:00"
        :return: list of message
        """
        return Message.query.filter_by(Message.date.between(start, end))

    @staticmethod
    def get_list_from_date(start):
        """
        Return all message from date to now.

        :param start: String that represent date: "2015-01-01 00:00:00"
        :return: list of message
        """
        return Message.query.filter_by(Message.date >= start)

    @staticmethod
    def insert_new_message(id, subject, message):
        message = Message(id, subject, message, datetime.now())

        database.session.add(message)
        database.session.commit()

    @staticmethod
    def get_new_mails_count():
        return database.session.query(Message).filter(Message.read==0).count()

    @staticmethod
    def refreshRead(mid, val):
        database.session.execute(
            update(Message).where(Message.id == mid).values(
                read=val
            )
        )

        database.session.commit()

        return True

    @staticmethod
    def delete(mid):
        Message.query.filter_by(id=mid).delete()
        database.session.commit()
