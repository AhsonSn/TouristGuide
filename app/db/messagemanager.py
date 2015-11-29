from .models import Message


class MessageManager(object):

    def get_list(self):
        """
        Return all message.

        :return: List of message.
        """
        return Message.query().all()

    def get_list_between_date(self, start, end):
        """
        Return all message between date.

        :param start: String that represent date: "2015-01-01 00:00:00"
        :param end: String that represent date: "2015-01-01 00:00:00"
        :return: list of message
        """
        return Message.query.filter_by(Message.date.between(start, end))

    def get_list_from_date(self, start):
        """
        Return all message from date to now.

        :param start: String that represent date: "2015-01-01 00:00:00"
        :return: list of message
        """
        return Message.query.filter_by(Message.date >= start)
