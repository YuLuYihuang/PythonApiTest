# -*-coding:utf-8 -*-
import requests
import json
def postaddem(em):
    url = "https://stargate.ar.elenet.me/delimont.saas_tnt/employee/addInitEmployee"
    headers = {
        'Cookie': "PASSPORT_DELIMONT_TOKEN=PBE_2.0_5cd1c6141c127d419f4bcae9f2648bb064aa81e86f244f82a92669d67e3796044af5f0da8db1445c74e3c06cdc28c404bdd458d908ecb547e94c6902cd995f3e987bbc9ea71dccb34a6383570d6858ceb3fe68bd31e7e77771ca1b436a5dd6fedeb7b7949c40c3efda970558e18e1063ea06aeaa2aea21aab4246fd4323f02e7ad4b4185afc3e8207133f7960cfaa275a1a190aa3c0630fb4ea218b94d87a7d4b54cf1e28cd3c812881be4cd3b8e56a371aad46cedaa25cdbfb22595be65480870bb2d7ae2a2254d79ab9843e8b894a7d2d9cb9a47b6772e732f9c53477aa931b01492da338abf7fb43fa86f7ce86cbb37e2d117ae0d4147ae2aa738576379469d2d53c08298f6d545a19adf1b17cf637f132fe6408ccbe94cc0df7207ded21bb674bea6839a7089c8e2f41be0320eb74b12ef8cc6269820e57a28026626c61cfaf97d96976eff0cc5857013faa8ef6c3e8e745bd2ad349673afb3851969ed1690e8d245bd44efe2",
        'Content-Type': "application/json",
        'X-shard': "shardid=2",
        'cache-control': "no-cache",
        'Postman-Token': "6d65ff2d-f07d-404d-84be-29e741885844,f7d0334c-7666-4951-a86d-c9cadbff2c29"
    }
    print '当前em',em.decode('string_escape')
    #response = requests.request("POST", url, data=em, headers=headers)
    #print response.text
    response = requests.post(url, data=em, headers=headers)
    # r.text是decode成Unicode
    print response.text#类型是unicode
    print type(response.text)

    print response.json()#字典{}

    print json.dumps(response.json())#字符串str
    print type(json.dumps(response.json()))
payload = [
        "{\"employee\": {\"tenantId\": 33,\"name\": \"黄qi金\",\"account\": \"qijin.huag@ele.me\",\"gender\": -1,\"email\": \"yijin.huang@ele.me\",\"phone\": \"12849846712\"}}\n",
        "{\"employee\": {\"tenantId\": 33,\"name\": \"黄ba金\",\"account\": \"bajin.hang@ele.me\",\"gender\": -1,\"email\": \"jin.huang@ele.me\",\"phone\": \"13616846522\"}}\n"
    ]
for d in payload:
    postaddem(d)

