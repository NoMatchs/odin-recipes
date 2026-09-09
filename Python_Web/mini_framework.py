from http.server import HTTPServer, BaseHTTPRequestHandler
import re
import os

# ============ 获取项目根目录 ============
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============ 模板引擎实现 ============

class TemplateEngine:
    """极简模板引擎 - 支持继承、变量、块替换"""
    
    def __init__(self, template_dir='templates'):
        self.template_dir = os.path.join(BASE_DIR, template_dir)
        print(f"📁 模板目录: {self.template_dir}")
    
    def render(self, template_name, **context):
        """渲染模板"""
        try:
            template_path = os.path.join(self.template_dir, template_name)
            
            if not os.path.exists(template_path):
                return f"<h1>模板文件不存在</h1><p>{template_path}</p>"
            
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查模板继承
            extends_match = re.search(r'{%\s*extends\s+"([^"]+)"\s*%}', content)
            if extends_match:
                parent_name = extends_match.group(1)
                parent_path = os.path.join(self.template_dir, parent_name)
                
                if not os.path.exists(parent_path):
                    return f"<h1>父模板不存在</h1><p>{parent_path}</p>"
                
                with open(parent_path, 'r', encoding='utf-8') as f:
                    parent_content = f.read()
                
                blocks = self._extract_blocks(content)
                result = self._replace_blocks(parent_content, blocks)
            else:
                result = content
            
            # 替换变量
            result = self._replace_variables(result, context)
            return result
            
        except Exception as e:
            print(f"❌ 模板渲染错误: {e}")
            import traceback
            traceback.print_exc()
            return f"<h1>模板渲染错误</h1><p>{e}</p>"
    
    def _extract_blocks(self, content):
        blocks = {}
        pattern = r'{%\s*block\s+(\w+)\s*%}(.*?){%\s*endblock\s*%}'
        for match in re.finditer(pattern, content, re.DOTALL):
            blocks[match.group(1)] = match.group(2).strip()
        return blocks
    
    def _replace_blocks(self, parent_content, blocks):
        pattern = r'{%\s*block\s+(\w+)\s*%}(.*?){%\s*endblock\s*%}'
        def replacer(match):
            block_name = match.group(1)
            return blocks.get(block_name, match.group(2))
        return re.sub(pattern, replacer, parent_content, flags=re.DOTALL)
    
    def _replace_variables(self, content, context):
        pattern = r'{{\s*([a-zA-Z_][a-zA-Z0-9_.]*)\s*}}'
        def replacer(match):
            var_name = match.group(1)
            if '.' in var_name:
                parts = var_name.split('.')
                value = context
                for part in parts:
                    if isinstance(value, dict):
                        value = value.get(part, '')
                    else:
                        value = getattr(value, part, '')
                return str(value) if value is not None else ''
            return str(context.get(var_name, ''))
        return re.sub(pattern, replacer, content)

# 创建全局模板引擎实例
template_engine = TemplateEngine()

# ============ 路由系统 ============

routes = []

def route(path_pattern):
    """装饰器：注册路由"""
    def decorator(func):
        pattern = re.sub(r'<([^>]+)>', r'(?P<\1>[^/]+)', path_pattern)
        pattern = r'^' + pattern + r'$'
        routes.append((re.compile(pattern), func))
        return func
    return decorator

# ============ HTTP 请求处理器 ============

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        
        # 去掉查询参数
        if '?' in path:
            path = path.split('?')[0]
        
        # 处理静态文件
        if path.startswith('/static/'):
            self._serve_static(path)
            return
        
        # 遍历路由表
        for pattern, func in routes:
            match = pattern.match(path)
            if match:
                kwargs = match.groupdict()
                try:
                    result = func(**kwargs)
                    
                    # 根据返回值类型处理
                    if isinstance(result, dict):
                        template_name = result.pop('_template', 'index.html')
                        context = result.copy()
                        context['request_path'] = path
                        response_body = template_engine.render(template_name, **context)
                    elif isinstance(result, str):
                        response_body = result
                    else:
                        response_body = str(result)
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(response_body.encode('utf-8'))
                    
                except Exception as e:
                    self.send_response(500)
                    self.end_headers()
                    error_msg = f"服务器错误: {e}"
                    self.wfile.write(error_msg.encode('utf-8'))
                    print(f"❌ 错误: {e}")
                    import traceback
                    traceback.print_exc()
                return
        
        # 404
        self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        try:
            not_found_html = template_engine.render('404.html', path=path, request_path=path)
            self.wfile.write(not_found_html.encode('utf-8'))
        except:
            self.wfile.write(f"<h1>404 Not Found</h1><p>{path}</p>".encode('utf-8'))
    
    def _serve_static(self, path):
        file_path = path[8:]
        full_path = os.path.join('static', file_path)
        
        try:
            with open(full_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            if file_path.endswith('.css'):
                self.send_header('Content-type', 'text/css')
            elif file_path.endswith('.js'):
                self.send_header('Content-type', 'application/javascript')
            else:
                self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

def run(port=8000):
    """启动服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'🚀 服务器已启动: http://localhost:{port}')
    print(f'📋 已注册的路由:')
    for pattern, func in routes:
        print(f'   {pattern.pattern} -> {func.__name__}')
    print('=' * 50)
    print('按 Ctrl+C 停止服务器')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n👋 服务器已停止')