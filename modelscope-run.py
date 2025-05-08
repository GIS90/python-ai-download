from modelscope import snapshot_download
from modelscope.hub.api import HubApi
from utils import hashlib_md5
from config import MS_ACCESS_TOKEN, MS_USER_NAME, CACHE_DIR


cache_dir = "%s\\Qweb3-0.6B" % CACHE_DIR
print(cache_dir)


# 下载模型
def download_model(model_id, cache_dir):
    snapshot_download(model_id=model_id, cache_dir=cache_dir)
    print(f"模型 {model_id} 下载完成，保存路径: {cache_dir}")   
# download_model(model_id='Qwen/Qwen3-0.6B', cache_dir=cache_dir)

# 上传模型到指定用户空间
try:
    api = HubApi()
    api.login(MS_ACCESS_TOKEN)
    
    upload_model_name = "Qweb3-0.6B-" + hashlib_md5(content=MS_ACCESS_TOKEN)
    model_id = f"{MS_USER_NAME}/{upload_model_name}"

    # 创建模型库
    api.create_model(
        model_id,
        visibility=5,  # 公开
        license="Apache-2.0",
        chinese_name="Qwen3-0.6B上传测试4"
    )
    
    # 上传模型文件夹
    api.upload_folder(
        repo_id=model_id,
        folder_path=cache_dir,
        commit_message='上传Qwen3-0.6B模型'
    )
    print(f"模型已成功上传到 {model_id}")
except Exception as e:
    print(f"上传失败: {str(e)}")