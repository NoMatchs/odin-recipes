import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin, urlparse

def setup_output_directory():
    """创建输出目录"""
    output_dir = "godot_docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def get_page_content(url):
    """
    获取页面内容
    
    参数:
        url (str): 要抓取的页面URL
        
    返回:
        str: 页面HTML内容，如果失败则返回None
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None

def extract_links_from_page(html, base_url):
    """
    从页面中提取所有链接
    
    参数:
        html (str): 页面HTML内容
        base_url (str): 基础URL，用于处理相对路径
        
    返回:
        list: 提取到的链接列表
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        # 跳过外部链接和锚点链接
        if href.startswith(('http', '#', 'mailto', 'javascript')):
            continue
        # 转换为绝对URL
        absolute_url = urljoin(base_url, href)
        links.add(absolute_url)
    
    return links

def save_page_content(html, url, output_dir):
    """
    保存页面内容到文件
    
    参数:
        html (str): 页面HTML内容
        url (str): 页面URL
        output_dir (str): 输出目录
    """
    # 创建安全的文件名
    parsed_url = urlparse(url)
    path_parts = [p for p in parsed_url.path.split('/') if p]
    if not path_parts:
        path_parts = ['index']
    
    file_path = os.path.join(output_dir, *path_parts) + '.html'
    
    # 创建必要的子目录
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

def crawl_godot_docs(start_url, max_pages=100):
    """
    爬取Godot文档的主函数
    
    参数:
        start_url (str): 起始URL
        max_pages (int): 最大爬取页面数
    """
    output_dir = setup_output_directory()
    visited_urls = set()
    urls_to_visit = [start_url]
    
    while urls_to_visit and len(visited_urls) < max_pages:
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited_urls:
            continue
            
        print(f"正在爬取: {current_url}")
        html = get_page_content(current_url)
        
        if html:
            save_page_content(html, current_url, output_dir)
            visited_urls.add(current_url)
            
            # 提取新链接
            new_links = extract_links_from_page(html, current_url)
            for link in new_links:
                if link not in visited_urls and link not in urls_to_visit:
                    urls_to_visit.append(link)
            
            # 添加延时，避免请求过于频繁
            time.sleep(1)
    
    print(f"爬取完成！共爬取 {len(visited_urls)} 个页面")

# 使用示例
if __name__ == "__main__":
    # Godot官方文档的起始URL
    start_url = "https://docs.godotengine.org/en/stable/"
    
    # 开始爬取，限制最大爬取页面数为100
    crawl_godot_docs(start_url, max_pages=100)
