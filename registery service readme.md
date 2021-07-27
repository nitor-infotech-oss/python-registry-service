# Registery Service 
Registry service provides efficient way to manage data variables, class instances and service instances in multiple files

Registry service helps you create singelton object in python that you can share between files.
This also provides elegant alternative of using Global variables for python.

NOTE: It is discouraged to use it as DB or store huge data. It is ideal to use it as store for variable, service instances and class instances, so that they can be access in multiple files. 

# Requirements
1. Python 2.7, 3.x
2. Works with any operating system.
3. No dependency on any other package.

# How to use
1. Import the Class from the package like `from registery_service import RegistryService`
2. Use class methods like 
   ```
   RegistryService().get_key('a_key')
   RegistryService().add_key('a_key', 'a_key_value')
   RegistryService().replace_key('a_key','a_key_value1')
   RegistryService().exists('a_key')
   RegistryService().remove_key('a_key')
   RegistryService().remove_all_key()
    ```
