##################################################
## 6. Classes
##################################################

# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instanted.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or object or attributes) like: __int__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder)
    # methods). You should not invent such names on your own.
    def __init(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name
        
        # Initialize property
        self._age = 0 # the leading underscore indicates the "age" property is
                      # intended to be used internally
                      # do not rely on this to be enforced: it's a hint to other devs

     # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."
    
    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species
    
    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"
    
    # A property is just like a getter.
    # It turns the method age() into a read-only attributes of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age
    
    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block executed when this
# module is the main program.
if __name__ == "__main__":
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")             # "Ian: hi"
    j = Human("Joel")
    j.say("hello")          # "Joel: hello"
    # i and j are instances of type Human; i.e, they are Human objects.

    # Call our class method
    i.say(i.get_species())      # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())      # => "Ian: H. neanderthalensis"
    j.say(j.get_species())      # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())        # => "*grunt*"

    # Static methods can be called by instances too
    print(i.grunt())            # => "*grunt*"

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                # => "Ian: 42"
    j.say(j.age)                # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                     # => this would raise an AttributeError