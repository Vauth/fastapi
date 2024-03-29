from somnium.sync import Somnium

async def Styles():
    "Get Art Styles as JSON"
    return await Somnium.Styles()

async def Generate(prompt:str, style:int):
    "Generate Art Using Somnium"
    return {"ok":True, "result":await Somnium.Generate(prompt, style)}