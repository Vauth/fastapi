"""
Notes:
    - Only async functions are accepted (async def blabla)
    - You have to define the type of objects (name:str) [str, int, bool ...]
    - Function have to return something (expect json, string, int formats)
    - Function names will be case sensitive.
    * Other than these, you're free to import anything as plugin with this structure.

Returns:
    - Endpoint is /{plugin name}/{function name}/
    - In this case, it will be /pluginexample/Test/
    - Description will be the description of the function
"""


async def Test(name:str):
    "Says your name"
    return f"Your name is '{name}'"