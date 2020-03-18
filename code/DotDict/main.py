class DotDict(dict):
    """
    Wrapper for dictioanries for calling elements by dot

    Work correctly if all elements are primitives
    """

    def __init__(self, d):
        super().__init__(d)

    def __getattr__(self, value):
        return self._get_value(self[value])

    def _get_value(self, value):
        """
        Return dict that wrapped in DotDict
        """
        if isinstance(value, dict):

            return self.__class__(value)

        elif isinstance(value, list):

            result = [self._get_value(i) for i in value]
            return result

        return value
