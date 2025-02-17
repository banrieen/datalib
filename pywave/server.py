#!.venv/bin/python
"""系统主接口说明
支持 rstful API
数据源管理
数据加载
数据生成

"""
from sanic import Sanic
from sanic.response import json
from sanic_ext import Extend
from sanic_ext import openapi
# from sanic_ext import swagger_blueprint, doc
from sanic.log import logger

# Local model infer service
# from src import runner

# 基础元数据
metadata = {}
app = Sanic(__name__, ctx=metadata )
# app.blueprint(swagger_blueprint)
app.extend(config={"oas_url_prefix": "/apidocs",
                   "API_TITLE": "Wave API",
                   "API_VERSION": "0.1"})

# # 跨域访问保护
# app.config.CORS_ORIGINS = "http://foobar.com,http://bar.com"
# Extend(app)


@app.route('/info')
async def default(request):
    return json({'Data lib server is running !': 'Wave'})

@app.route('/snapcut')
async def snapcut(request):
    #  截图
    return json({'截图成功': '图像路径'})


@app.post('/wafer_ssa')
@openapi.definition(
    body='{"image_path":"", "manifest":"默认留空"}',
    summary="User profile update",
    description="ssa 模型调用接口，支持传入图像地址",
    )


async def wafer_ssa_infer_handler(request):
    image_path = request.json["image_path"]
    manifest = request.json["manifest"]
    ssa = ssa_infer(manifest)
    cla, image = ssa.ssa_class_infer(image_path)
    logger.info(f'============>>> Infer wafer map {image_path} class is {cla} !')
    return json({"image": image_path, "cla": cla})

if __name__ == '__main__':
    app.run(auto_reload=True)