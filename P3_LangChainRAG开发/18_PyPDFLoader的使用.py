# 1. 安装依赖
# !pip install langchain pypdf

# 2. 导入并使用
from langchain_community.document_loaders import PyPDFLoader

# 初始化加载器（传入 PDF 文件路径）
loader = PyPDFLoader(
    "./data/pdf1.pdf",          # 文件路径
    mode="page",                        # 默认是page模式: 每个页面形成一个Document文档对象
                                        # single模式: 把整个pdf变成一个独立的Document对象
    # password="itheima",                 # pdf文档密码
)

# 加载文档（返回 Document 列表）
documents = loader.load()

# 查看结果
print(f"总页数: {len(documents)}")
print(f"第一页内容: {documents[0].page_content[:100]}...")
print(f"元数据: {documents[0].metadata}")  # 包含 source、page 等信息

print(documents)