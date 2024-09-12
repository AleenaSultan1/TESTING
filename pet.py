'''
CSCI 204 Lab 02 Class Design, Inheritance, and Exceptions
Lab section: CSCI 204, Tuesday 1:00pm - 2:50pm
Student name(s): Aleena Sultan, Khanh Cao 
Instructor name: Professor Todd Schmid 
'''

class Pet:
    """ Base class: Publication
       A class capturing information about a publication.
       Attributes:
          _title; string
          _author; string
   """
    UNKNOWN = 0
    WALKING = 1
    EATING = 2
    SLEEPING = 3
    BARKING = 4
    MEOWING = 5
    
    def __init__(self, nam, spec, age = 0, activity = UNKNOWN):
        '''
        Initializes a new instance of the class with the specified attributes.

        Args:
            name (str): The name of the individual (e.g., animal, person).
            species (str): The species of the individual.
            age (int, optional): The age of the individual. Defaults to 0.
            activity (str, optional): The primary activity of the individual. Defaults to UNKNOWN.

        Raises:
            AgeException: If the provided age is invalid (less than 0), an AgeException is raised.
    
        Attributes:
            _name (str): The name of the individual.
            _age (int): The age of the individual.
            _activity (str): The primary activity of the individual.
            species (str): The species of the individual.
        '''
        self._name = nam
        validate_age(age)
        self._age = age
        self._species = spec
        self._activity = activity

    def walk(self):
        """
        Updates the activity status of the pet to 'walking'.

        Return: None

        """
        self._activity = self.WALKING
    
    def eat(self):
        """
        Updates the activity status of the pet to 'eating'.

        Return: None

        """
        self._activity = self.EATING
    
    def sleep(self):
        """
        Updates the activity status of the individual to 'sleeping'.

        Return: None

        """
        self._activity = self.SLEEPING
    
    def make_noise(self):
        """
        Updates the activity status to reflect the noise the individual is making based on its species.  

        The method checks the `_species` attribute and updates the `_activity` attribute accordingly:
            - If the species is 'Dog', the activity is set to `BARKING`.
            - If the species is 'Cat', the activity is set to `MEOWING`.

        For a Dog, the activity is set to 'barking'.  
        For a Cat, the activity is set to 'meowing'.

        Return: None
        """
        if self._species == 'Cat':
            self._activity = self.MEOWING
        else:
            self._activity = self.BARKING
    
    def celebrate_birthday(self):
        """
        Increments the individual's age by 1 year.

        This method simulates the individual having a birthday and increases the `_age` attribute by 1.

        Return: None
        """
        self._age += 1
    
    def get_human_age(self):
        """
        Calculates and returns the equivalent human age based on the individual's species.

        For Dogs:
        The age is multiplied by 7 to get the human equivalent.
    
        For Cats:
        - 1 year is equivalent to 15 human years.
        - 2 years are equivalent to 24 human years.
        - For ages 3 and above, 4 human years are added for each additional year after age 2.

        Returns:
        int: The equivalent human age based on the species.

        """
        age = self._age
        if self._species == 'Cat':
            if age == 1:
                human_age = 15
            elif age == 2:
                human_age = 24
            else:
                human_age = 24 + 4*(age - 2)
        else:
            human_age = self._age * 7
        return human_age

    def __str__(self):
        """
        Returns a string representation of the object, detailing its current activity.

        The method maps the internal `_activity` value to a string, 
        based on predefined activity codes:
            - 0: 'UNKNOWN'
            - 1: 'walking'
            - 2: 'eating'
            - 3: 'sleeping'
            - 4: 'barking'
            - 5: 'meowing'

        Returns:
            str: A string representing the individual's current activity.
        """
        if self._activity == 0:
            act = 'doing UNKNOWN'
        elif self._activity == 1:
            act = 'walking'
        elif self._activity == 2:
            act = 'eating'
        elif self._activity == 3:
            act = 'sleeping'
        elif self._activity == 4:
            act = 'barking'
        elif self._activity == 5:
            act = 'meowing'
        return f'{self._name} (age: {self._age}) is {act}.'

class AgeException(Exception):
    def __init__(self, message="Invalid Age"):
        """
        Initializes the exception with an optional custom error message.

        Parameters:

        message : str, optional
            The error message to display when the exception is raised. 
            Defaults to "Invalid Age".

        Attributes:
            message : str
            The error message associated with the exception.
        """
        self.message = message
        super().__init__(self.message)
    
def validate_age(age):
    """
    Validates if the given age is within a valid range.

    Args:
        age (int): The age to be validated.

    Raises:

        AgeException: If the age is less than 0, an AgeException is raised
                      indicating that the age is invalid.
    """
    if not (age >= 0):
        raise AgeException



if __name__=="__main__":
    testPet = Pet("Mable", "Cat", 8)
    print(testPet._name)
    print(testPet._age)
    print(testPet)
    testPet = Pet("Mable", "Cat", -1)
    print(testPet)
