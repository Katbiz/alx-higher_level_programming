0x0C. Python - Almost a circle

TASKS

0. Write the first class Base:

1. Write the class Rectangle that inherits from Base:

2. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

3. Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

4. Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you t need to handle x and y here.don

5. Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

6. Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

7. Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

8. Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

9. Write the class Square that inherits from Rectangle:

10. Update the class Square by adding the public getter and setter size

11. Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

12. Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

13. Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

14. Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

15. Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

16. Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

17. Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

18. Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

19. Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:

20. Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares: