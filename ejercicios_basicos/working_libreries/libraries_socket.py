"""_summary_

    Working with library socket

"""

import socket

# get host name from socket
print(f"{socket.gethostname() = }")

# ip direccion
print(f"{socket.gethostbyname(socket.gethostname()) }")
