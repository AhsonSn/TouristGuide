from .models import Message


class MessageManager(object):

    @staticmethod
    def get_list():
        """
        Return all message.

        :return: List of message.
        """
        return Message.query().all()

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
