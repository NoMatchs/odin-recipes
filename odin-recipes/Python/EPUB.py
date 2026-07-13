import ebooklib
from ebooklib import epub
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os

def epub_to_pdf_simple(epub_path, pdf_path):
    """
    最简 EPUB 转 PDF 转换器
    只提取纯文本，按页排版
    """
    # 1. 读取 EPUB 文件
    print(f"正在读取: {epub_path}")
    book = epub.read_epub(epub_path)
    
    # 2. 提取所有文本内容
    all_text = []
    for item in book.get_items():
        # 只处理文档类型的文件（HTML/XHTML）
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            try:
                # 解码为文本
                content = item.get_content().decode('utf-8')
                # 简单去除 HTML 标签（只保留纯文本）
                # 这是一个极简的清理，实际项目需要用 BeautifulSoup
                import re
                text = re.sub(r'<[^>]+>', ' ', content)  # 去除标签
                text = re.sub(r'\s+', ' ', text)         # 合并空白
                text = text.strip()
                if text:
                    all_text.append(text)
            except:
                continue
    
    full_text = ' '.join(all_text)
    print(f"提取文本长度: {len(full_text)} 字符")
    
    # 3. 生成 PDF
    print(f"正在生成 PDF: {pdf_path}")
    
    # 创建 PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    margin = 72  # 1英寸边距
    y_position = height - margin
    font_size = 12
    line_height = font_size * 1.5
    max_width = width - 2 * margin
    
    # 设置字体（使用默认字体，中文可能不显示）
    c.setFont('Helvetica', font_size)
    
    # 分页处理
    words = full_text.split()
    current_line = ''
    
    for word in words:
        # 测试添加这个词是否超宽
        test_line = current_line + ' ' + word if current_line else word
        text_width = c.stringWidth(test_line, 'Helvetica', font_size)
        
        if text_width <= max_width:
            current_line = test_line
        else:
            # 当前行已满，绘制
            if y_position < margin:
                # 新页面
                c.showPage()
                c.setFont('Helvetica', font_size)
                y_position = height - margin
            
            c.drawString(margin, y_position, current_line)
            y_position -= line_height
            current_line = word
    
    # 绘制最后一行
    if current_line:
        if y_position < margin:
            c.showPage()
            c.setFont('Helvetica', font_size)
            y_position = height - margin
        c.drawString(margin, y_position, current_line)
    
    c.save()
    print(f"✅ 转换完成！PDF 保存在: {pdf_path}")

# 使用示例
if __name__ == "__main__":
    # 替换成你的 EPUB 文件路径
    epub_file = "《经济学人》百词斩 · 每日一词100期合辑（每天三分钟，助你一年读懂《经济学人》的英文！） (《经济学人·商论》选辑) (经济学人·商论) (z-library.sk, 1lib.sk, z-lib.sk).epub"
    pdf_file = "output.pdf"
    
    if os.path.exists(epub_file):
        epub_to_pdf_simple(epub_file, pdf_file)
    else:
        print(f"❌ 文件不存在: {epub_file}")
        print("请将 example.epub 替换为你的 EPUB 文件路径")