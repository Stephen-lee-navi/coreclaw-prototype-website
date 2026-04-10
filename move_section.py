#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open('pages/google-data-scraping-solutions.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到"谷歌数据抓取演示"板块 (Code Demo Section)
code_demo_pattern = r'    <!-- Code Demo Section -->.*?    </section>\n'
code_demo_match = re.search(code_demo_pattern, content, re.DOTALL)

if code_demo_match:
    code_demo_section = code_demo_match.group(0)
    
    # 从原位置删除该板块
    content_without = content[:code_demo_match.start()] + content[code_demo_match.end():]
    
    # 找到"为什么需要谷歌数据？"板块的结束位置
    use_cases_pattern = r'(    <!-- Use Cases Section -->.*?    </section>\n)'
    use_cases_match = re.search(use_cases_pattern, content_without, re.DOTALL)
    
    if use_cases_match:
        # 在该板块后面插入"谷歌数据抓取演示"板块
        insert_pos = use_cases_match.end()
        new_content = content_without[:insert_pos] + code_demo_section + content_without[insert_pos:]
        
        with open('pages/google-data-scraping-solutions.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("板块移动成功！")
    else:
        print("未找到'为什么需要谷歌数据？'板块")
else:
    print("未找到'谷歌数据抓取演示'板块")
