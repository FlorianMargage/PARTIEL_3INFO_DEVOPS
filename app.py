"""Module de calculs mathématiques et Bonjour."""

def add(a, b):
    """Faire la somme de 2 nombres."""
    return a + b

def multiply( x,y ):
    """Faire la multiplication de 2 nombres."""
    return x*y

def divide(x , y ):
    """Faire la division de 2 nombres."""
    if y != 0:
        return x/y
    return None

def greet(name):
    """Retourne Bonjour suivi du nom passé en paramètre."""
    if name =="":
        return "Hello, World!"
    return "Hello,"+name
