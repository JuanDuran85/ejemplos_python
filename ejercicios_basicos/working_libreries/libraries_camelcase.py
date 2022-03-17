"""_summary_

    Using camelcase library

"""

from camelcase import CamelCase

camel: CamelCase = CamelCase()

texto: str = "ejemplo utilizando la libreria camelcase en python"

print(camel.hump(texto))
