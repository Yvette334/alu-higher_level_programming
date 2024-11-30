class Base:
    """Base class for managing id attribute in other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.

        Args:
            id (int): The id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

