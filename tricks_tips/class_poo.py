"""[summary]

Tips and tricks for class -POO in Python.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""
"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using inheritance'''
print("\n Using inheritance \n")

# If you need know one class is a subclass of another, you can use the issubclass method.
class Vehicle:
    def __init__(self, year, model):
        self.year = year
        self.model = model

class Car(Vehicle):
    def __init__(self, year, model, color):
        super().__init__(year, model)
        self.color = color
        
print(f"{issubclass(Car, Vehicle) = }")
print(f"{issubclass(Vehicle, Car) = }")

print("\n Using __len__ method \n")

# To get the length of the class, you can use the __len__ method.

class Cart:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)

c = Cart("Hello")
print(f"{len(c) = }")

print("\n Using hasattr and getattr methods \n")

# If you want to know if a class has any attributes or get any attributes, you can use the hasattr and getattr methods.

class Job:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        
job = Job("Juan","Developer")
print(f"{hasattr(job, 'name') = }")
print(f"{hasattr(job, 'title') = }")
print(f"{getattr(job, 'name') = }")
print(f"{getattr(job, 'title') = }")
print(f"{hasattr(job, 'age') = }")


# If you need set a new attribute, you can use the setattr method.

class Animal: ...

cat: Animal = Animal()
print(f"{cat = }")
setattr(cat, 'name', 'Garfield')
print(f"{cat.name = }")

# you can delete a object class with __del__ method.

class Video():
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration
        print(f"Se creo el video {self.title}")
        
    def __str__(self):
        return f"{self.title} - {self.duration}"
        
    def __del__(self):
        print(f"Se elimino el video {self.title}")
        
    def __len__(self):
        return self.duration
        
video_one: Video = Video("Video 1", 130)
print(video_one)
print(f"La duracion del video es: {len(video_one)}")
del(video_one)

# class in one line
School = type('School', (object,), {'fun':{}})
print(f"{School = }")
