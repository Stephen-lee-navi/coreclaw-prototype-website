#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open('pages/google-data-scraping-solutions.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义新的卡片式网格布局内容 - 只修改这个板块
new_section = '''    <!-- One-Click Extraction Section -->
    <section class="section">
        <div class="section-inner">
            <div class="section-header">
                <h2 class="section-title">一次调用，轻松抓取Google数据</h2>
            </div>
            <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(28rem, 1fr)); gap: 2.4rem;">
                <div class="feature-card" style="background: var(--color-neutral-background); border-radius: 16px; padding: 3.2rem; border: 1px solid var(--color-neutral-border); transition: all 0.3s ease;">
                    <div class="feature-number" style="width: 5rem; height: 5rem; background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: 700; margin-bottom: 2rem;">01</div>
                    <h4 style="font-size: 2rem; font-weight: 600; margin-bottom: 1.2rem; color: var(--color-neutral-text);">结构化输出</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>抓取到的数据可按清晰字段进行组织</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>更方便接入数据库、分析系统或内部工具</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>无需团队手动处理大量原始页面内容</li>
                    </ul>
                </div>

                <div class="feature-card" style="background: var(--color-neutral-background); border-radius: 16px; padding: 3.2rem; border: 1px solid var(--color-neutral-border); transition: all 0.3s ease;">
                    <div class="feature-number" style="width: 5rem; height: 5rem; background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: 700; margin-bottom: 2rem;">02</div>
                    <h4 style="font-size: 2rem; font-weight: 600; margin-bottom: 1.2rem; color: var(--color-neutral-text);">本地化采集</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>面向不同国家、地区、语言和搜索环境</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>采集更贴近目标市场的 Google 数据</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>获得更有参考价值的结果</li>
                    </ul>
                </div>

                <div class="feature-card" style="background: var(--color-neutral-background); border-radius: 16px; padding: 3.2rem; border: 1px solid var(--color-neutral-border); transition: all 0.3s ease;">
                    <div class="feature-number" style="width: 5rem; height: 5rem; background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: 700; margin-bottom: 2rem;">03</div>
                    <h4 style="font-size: 2rem; font-weight: 600; margin-bottom: 1.2rem; color: var(--color-neutral-text);">覆盖多种 Google 页面类型</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>不仅支持普通搜索结果</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>也支持地图、购物、趋势、评论等</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>满足更多细分业务需求</li>
                    </ul>
                </div>

                <div class="feature-card" style="background: var(--color-neutral-background); border-radius: 16px; padding: 3.2rem; border: 1px solid var(--color-neutral-border); transition: all 0.3s ease;">
                    <div class="feature-number" style="width: 5rem; height: 5rem; background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: 700; margin-bottom: 2rem;">04</div>
                    <h4 style="font-size: 2rem; font-weight: 600; margin-bottom: 1.2rem; color: var(--color-neutral-text);">自动化集成</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>支持定时任务、批量采集</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>监控系统和内容工作流</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>更自然地把 Google 数据接入现有流程</li>
                    </ul>
                </div>

                <div class="feature-card" style="background: var(--color-neutral-background); border-radius: 16px; padding: 3.2rem; border: 1px solid var(--color-neutral-border); transition: all 0.3s ease;">
                    <div class="feature-number" style="width: 5rem; height: 5rem; background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: 700; margin-bottom: 2rem;">05</div>
                    <h4 style="font-size: 2rem; font-weight: 600; margin-bottom: 1.2rem; color: var(--color-neutral-text);">可扩展性</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>从少量关键词测试开始</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>到多地区、多类别、多任务并行采集</li>
                        <li style="font-size: 1.5rem; color: var(--color-neutral-text-muted); padding: 0.6rem 0; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: #4285f4;">•</span>支持持续型数据收集需求</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>'''

# 查找并替换 One-Click Extraction Section
pattern = r'    <!-- One-Click Extraction Section -->.*?    </section>'
match = re.search(pattern, content, re.DOTALL)

if match:
    content = content[:match.start()] + new_section + content[match.end():]
    with open('pages/google-data-scraping-solutions.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("文件修改成功！")
else:
    print("未找到目标区块")
