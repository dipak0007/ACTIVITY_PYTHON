import uuid

def generate_table_id(instance):
    """
    Generate a unique ID for a Django model instance's table.

    Args:
        instance: An instance of a Django model.

    Returns:
        str: A unique table ID for the instance.

    Example:
        >>> from myapp.models import productsModel
        >>> instance = productsModel.objects.get(pk=1)
        >>> generate_table_id(instance)
        'LOP_96d3744c-7547-4fa6-84fd-8326e3964d26'
    """
    return instance.PREFIX_TABLE_ID_WORD + '_' + str(uuid.uuid4())
