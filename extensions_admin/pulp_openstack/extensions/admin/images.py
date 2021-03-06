from gettext import gettext as _

from pulp.client.commands.unit import UnitCopyCommand, UnitRemoveCommand

from pulp_openstack.common import constants


DESC_COPY = _('copies images from one repository into another')
DESC_REMOVE = _('remove images from a repository')
DESC_SEARCH = _('search for images in a repository')

MODULE_ID_TEMPLATE = '%(image_checksum)s'


def get_formatter_for_type(type_id):
    """
    Return a method that takes one argument (a unit) and formats a short string
    to be used as the output for the unit_remove command.

    :param type_id: The type of the unit for which a formatter is needed
    :type  type_id: str

    :raises ValueError: if the method does not recognize the type_id
    :return: method
    :rtype:  callable
    """

    if type_id != constants.IMAGE_TYPE_ID:
        raise ValueError(_("The openstack image formatter can not process %s units.") % type_id)

    return lambda x: MODULE_ID_TEMPLATE % x


class ImageCopyCommand(UnitCopyCommand):
    """
    Copy command. This is still in progress.
    """

    def __init__(self, context, name='copy', description=DESC_COPY):
        """
        Initailize copy command.

        See super() for more detail, we just set the type_id here.
        """
        super(ImageCopyCommand, self).__init__(context, name=name, description=description,
                                               method=self.run, type_id=constants.IMAGE_TYPE_ID)

    @staticmethod
    def get_formatter_for_type(type_id):
        """
        Returns a method that can be used to format the unit key of a openstack image
        for display purposes.

        :param type_id: the type_id of the unit key to get a formatter for
        :type  type_id: str

        :return: formatter function
        :rtype: function
        """
        return get_formatter_for_type(type_id)


class ImageRemoveCommand(UnitRemoveCommand):
    """
    Class for executing unit remove commands for openstack image units.
    """

    def __init__(self, context, name='remove', description=DESC_REMOVE):
        """
        Initialize remove command.

        See super() for more detail; we just set a few items here
        """
        UnitRemoveCommand.__init__(self, context, name=name, description=description,
                                   type_id=constants.IMAGE_TYPE_ID)

    @staticmethod
    def get_formatter_for_type(type_id):
        """
        Returns a method that can be used to format the unit key for display
        purposes.

        :param type_id: the type_id of the unit key to get a formatter for
        :type  type_id: str

        :return: formatter function
        :rtype: function
        """
        return get_formatter_for_type(type_id)
