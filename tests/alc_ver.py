from arclet.alconna import Alconna,Arg,MultiVar
from rich import print

alc:AlconnaAlconna('select',Arg(name='args',value=Multivar(value=str,flag='+')))

def wrapper(slot:int | str,content:str | None)->str | None:
    if content is not None:
        return''.join(content.split(sep='还是'))
    return None

alc.shortcut(
    key=r'选(?P<args>,*)',
    command='select {args}',
    fuzzy=False,    
    wrapper=wrapper,
)
print(alc.parse(message='选a还是b还是c'))