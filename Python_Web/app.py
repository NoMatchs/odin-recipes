from mini_framework import route, run
import datetime

@route('/')
def index():
    return {
        '_template': 'index.html',
        'request_path': '/'
    }

@route('/hello/<name>')
def say_hello(name):
    return {
        '_template': 'hello.html',
        'name': name,
        'current_time': datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),
        'request_path': f'/hello/{name}'
    }

@route('/user/<user_id>')
def get_user(user_id):
    users = {
        '123': {'name': '张三', 'age': 22, 'major': '计算机科学'},
        '456': {'name': '李四', 'age': 21, 'major': '软件工程'},
        '789': {'name': '王五', 'age': 23, 'major': '数据科学'},
    }
    user = users.get(user_id)
    if user:
        return {
            '_template': 'user.html',
            'user_id': user_id,
            'user': user,
            'request_path': f'/user/{user_id}'
        }
    else:
        return {
            '_template': '404.html',
            'path': f'/user/{user_id}',
            'request_path': f'/user/{user_id}'
        }

@route('/post/<year>/<month>')
def show_post(year, month):
    posts = [
        {'title': 'Python Web开发入门', 'date': f'{year}-{month}-01'},
        {'title': '动态路由的实现原理', 'date': f'{year}-{month}-15'},
        {'title': '模板引擎的底层机制', 'date': f'{year}-{month}-28'},
    ]
    html = f"""
    <h1>📝 {year}年{month}月 文章列表</h1>
    <div class="card">
        <ul style="list-style:none; padding:0;">
    """
    for post in posts:
        html += f'<li style="padding:12px 0; border-bottom:1px solid #f0f0f0; display:flex; justify-content:space-between; align-items:center;"><span><i class="fas fa-file-alt" style="color:#667eea;"></i> {post["title"]}</span><span class="badge">{post["date"]}</span></li>'
    html += """
        </ul>
    </div>
    <a href="/" class="btn"><i class="fas fa-arrow-left"></i> 返回首页</a>
    """
    return html

@route('/calc/<a>/<b>')
def calc(a, b):
    result = int(a) + int(b)
    return {
        '_template': 'calc.html',
        'a': a,
        'b': b,
        'result': result,
        'operator': '+',
        'request_path': f'/calc/{a}/{b}'
    }

@route('/about')
def about():
    return {
        '_template': 'about.html',
        'request_path': '/about'
    }

@route('/features')
def features():
    return {
        '_template': 'features.html',
        'request_path': '/features'
    }

if __name__ == '__main__':
    run(port=8000)