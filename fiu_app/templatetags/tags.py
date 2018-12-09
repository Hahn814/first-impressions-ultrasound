from django import template
from itertools import zip_longest

register = template.Library()


@register.filter(name='group_list_by')
def group_list_by(data, group_size=4):
    """
    Group a list into a list of groups of group_size
    :param data: Iterable
    :param group_size: group size
    """
    args = [iter(data)] * group_size
    return zip_longest(*args, fillvalue=None)

