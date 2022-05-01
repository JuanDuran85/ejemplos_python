"""_summary_

    Using textwrap library

"""

from textwrap import dedent, shorten

# dedent remove any common leading whitespace from every line in text. This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.
def test() -> None:
    string_text: str = '''\
        texto de prueba
            mas otra linea de texto de prueba
    '''
    print(repr(string_text))
    print(repr(dedent(string_text)))
    

def shor_text(text_in: str, width_in: int) -> str:
    return shorten(text_in, width_in)
    
if __name__ == '__main__':
    test()
    print(shor_text('texto de prueba para aplicar short', 17))