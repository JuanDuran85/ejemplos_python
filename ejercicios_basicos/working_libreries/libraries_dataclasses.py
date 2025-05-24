"""
Using de dataclasses library.

You can use the dataclasses library to implement type annotations

eq=True: Automatically generates an __eq__ method to compare instances of this
class for equality.

frozen=True: Disables the possibility of modifying the attributes of
instances of this class.
That is, it makes the instances immutable (they cannot be modified
after creation), similar to a tuple.

order=True: Automatically generates an __lt__ method to compare instances
of this class by order.


"""

from dataclasses import dataclass

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# Use the simplest possible arguments for your methods. Because you can pass
# them directly from your entry points (API, Celery jobs, etc), no need form
# unnecessarily loading of complex objects.
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------


@dataclass
class User:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    id: int
    username: str


@dataclass
class Ticket:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    id: int
    user_id: int
    title: str


USERS: list[User] = [User(id=1, username="ejemplo1234")]
TICKETS: list[Ticket] = [Ticket(id=1, user_id=1, title="Ejemplo de titulo")]


def list_user_tickets(user_id: int) -> list[Ticket]:
    """
    Retrieve a list of tickets associated with a specific user.

    Args:
        user_id (int): The ID of the user whose tickets are to be retrieved.

    Returns:
        list[Ticket]: A list of Ticket objects that belong to the
        specified user.
    """

    return [ticket for ticket in TICKETS if ticket.user_id == user_id]


result: list[Ticket] = list_user_tickets(USERS[0].id)
print(result)

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

@dataclass
class UserTwo:
    """
    Represents a user with a username.

    Attributes:
        username (str): The username of the user.
    """

    username: str


# good way to use a type annotations


def print_users(users: list[UserTwo]) -> None:
    """Prints all users in the list

    Args:
        users (list[UserTwo]): List of users to print
    """
    for one_user in users:
        print(one_user)


print_users([UserTwo(username="Usuario 1")])
