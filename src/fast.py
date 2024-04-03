#Powered by t.me.feelded

import os
import ssl
import ast
import uvicorn
import inspect
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

#FastAPI App
app = FastAPI(debug=False)
# app.add_middleware(HTTPSRedirectMiddleware)

#Error
@app.exception_handler(404)
async def Custom404(_, __):
    return JSONResponse(status_code=404, content={"success": 0, "detail": "What could have been?"})

#Refetch Plugins
def RefetchPlugins():
    Plugins = [i[:-3] for i in os.listdir("plugins") if not i.startswith("_")]
    Details = []
    for name in Plugins:
        for func in [node.name for node in ast.walk(ast.parse((open("plugins/"+name+".py", 'r')).read())) if isinstance(node, ast.AsyncFunctionDef)]:
            exec(f"from plugins.{name} import {func}")
            FuN = ", ".join([j for j in inspect.signature(eval(func)).parameters])
            FuT = ", ".join([d+":"+str(k.annotation).split("'")[1] for d, k in inspect.signature(eval(func)).parameters.items()])
            DeC = inspect.getdoc(eval(func)) if inspect.getdoc(eval(func)) else "None"
            Details.append({"plugin":name, "function":func, "funcdef":FuT, "funcrun":FuN, "description": DeC})
    with open("functions.txt", "w") as f: f.write(str(Details))
    return {"success": 1}

#Refetch
RefetchPlugins()

#Plugins Import
with open("functions.txt", "r") as f: funcs = eval(f.read())
for one in funcs: exec(f"from plugins.{one['plugin']} import {one['function']}")

#Update app
def Update():
    with open("functions.txt", "r") as f: funcs = eval(f.read())
    for one in funcs:
        exec(f"@app.get('/{one['plugin']}/{one['function']}', description='{one['description']}', tags=['{one['plugin']}'])\nasync def {one['function']}({one['funcdef']}):\n   return await {one['function']}({one['funcrun']})")
        print(f">>> Import {one['function']} from {one['plugin']}.py")
    return {"success": 1}


#Main
@app.get("/", include_in_schema=False)
async def root():
    return {"success": 1, "detail": "Still alive? am I?"}

#Updater
@app.post('/admin/update', description='Update The Plugins', tags=['admin'])
async def update():
    RefetchPlugins()
    return {"success": 1}

#Cookie Tester
@app.get("/admin/cookie", description="Cookie validation tester", tags=['admin'])
async def cookie(request: Request):
    headers = request.headers
    cookies = request.cookies
    if cookies and cookies['password'] and cookies['password'] == '666':
        return {"success": 1, "headers": headers, "cookies": cookies}
    else:
        return {'success': 0}

#Update static
Update()

#Run
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # ssl_keyfile="INSERT KEY", ssl_certfile="INSERT CERT" https://certbot.eff.org/instructions
