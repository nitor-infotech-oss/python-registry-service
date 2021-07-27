def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class RegistryService:
    """
    Registry Service holds a set of key, value pairs.
    In application it can be used for dependency injection or inversion of control IOC.
    """

    def __init__(self):
        self.reg_var = dict()

    def add_key(self, key, value):
        """
        Use 'replace_key' for replacing value of key
        """
        if key in self.reg_var:
            raise Exception('key `{}` already exists in RegistryService.'.format(key))
        self.reg_var[key] = value

    def replace_key(self, key, value):
        """
        Will create the key and value if provided key does not exist in reg_var. Use add_key for adding the key instead
        """
        self.reg_var[key] = value

    def exists(self, key):
        """
        Will check if the value exists in reg_var
        """
        return key in self.reg_var

    def get_key(self, key):
        """
        Will get the value of key if key exists in reg_var
        """
        if key not in self.reg_var:
            raise Exception('key {} not found in RegistryService'.format(key))
        return self.reg_var[key]

    def remove_key(self, key):
        """
        Will remove the key from reg_var
        """
        if key in self.reg_var:
            self.reg_var.pop(key, None)
        else:
            raise Exception('key {} not found in RegistryService'.format(key))

    def remove_all_key(self):
        """
        Will remove all keys and values in reg_var
        """
        self.reg_var = dict()
