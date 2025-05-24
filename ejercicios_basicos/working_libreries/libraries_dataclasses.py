"""
Using de dataclasses library.

You can use the dataclasses library to implement type anotations

eq=True: Automatically generates an __eq__ method to compare instances of this class for equality.

frozen=True: Disables the possibility of modifying the attributes of instances of this class.
That is, it makes the instances immutable (they cannot be modified after creation), similar to a tuple.

order=True: Automatically generates an __lt__ method to compare instances of this class by order.


"""

from dataclasses import dataclass

# ----------------------------------------------------------------------------------------------# ----------------------------------------------------------------------------------------------
# Use the simplest possible argumennts for your methods. Becouse you can pass them directly from your entry points (API, Celery jobs, etc), no need form unnecessarily loading of complex objects.
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------


@dataclass
class User:
    id: int
    username: str


@dataclass
class Ticket:
    id: int
    user_id: int
    title: str


USERS: list[User] = [User(id=1, username="ejemplo1234")]
TICKETS: list[Ticket] = [Ticket(id=1, user_id=1, title="Ejemplo de titulo")]


def list_user_tickets(user_id: int) -> list[Ticket]:
    return [ticket for ticket in TICKETS if ticket.user_id == user_id]


result: list[Ticket] = list_user_tickets(USERS[0].id)
print(result)

# ----------------------------------------------------------------------------------------------# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------# ----------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------


@dataclass
class UserTwo:
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
