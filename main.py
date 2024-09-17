from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get():
    """ Home """
    return Div(P('Portfolio'))

serve()
