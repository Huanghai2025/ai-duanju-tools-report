#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将调研报告 Markdown 转换为带样式的独立 HTML 页面，供 GitHub Pages 部署。"""
import pathlib
import sys

SRC = pathlib.Path(r"D:\QclawWorkspace\AI短剧漫剧\AI短剧漫剧开源工具调研报告.md")
OUT_DIR = pathlib.Path(r"D:\QclawWorkspace\AI短剧漫剧\website")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "index.html"

CSS = """
:root{
  --bg:#0f1115; --card:#171a21; --ink:#e8eaed; --muted:#9aa4b2;
  --accent:#6ea8fe; --accent2:#7ee787; --border:#2a2f3a; --warn:#f0b429; --bad:#ff7b72;
}
* { box-sizing:border-box; }
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
  line-height:1.75; font-size:16px;
}
.wrap{ max-width:1080px; margin:0 auto; padding:48px 24px 80px; }
header.hero{
  border-bottom:1px solid var(--border); padding-bottom:24px; margin-bottom:32px;
}
header.hero h1{ font-size:30px; margin:0 0 8px; color:#fff; }
header.hero .meta{ color:var(--muted); font-size:14px; }
h1,h2,h3{ color:#fff; line-height:1.3; }
h2{ margin-top:40px; padding-top:16px; border-top:1px solid var(--border); font-size:23px; }
h3{ margin-top:28px; font-size:18px; color:var(--accent); }
p{ color:var(--ink); }
a{ color:var(--accent); }
code{ background:var(--card); padding:2px 6px; border-radius:4px; font-size:13px; color:var(--accent2); }
pre{ background:var(--card); border:1px solid var(--border); border-radius:8px; padding:14px; overflow:auto; }
pre code{ background:none; padding:0; color:var(--ink); }
table{ width:100%; border-collapse:collapse; margin:18px 0; font-size:14px; }
th,td{ border:1px solid var(--border); padding:9px 11px; text-align:left; vertical-align:top; }
th{ background:var(--card); color:#fff; }
tbody tr:nth-child(even){ background:rgba(255,255,255,0.02); }
blockquote{
  border-left:4px solid var(--accent); background:var(--card); margin:18px 0;
  padding:12px 16px; border-radius:0 8px 8px 0; color:var(--muted);
}
blockquote p{ color:var(--muted); margin:0; }
ul,ol{ padding-left:22px; }
li{ margin:4px 0; }
hr{ border:none; border-top:1px solid var(--border); margin:32px 0; }
.footnote{ color:var(--muted); font-size:13px; margin-top:40px; border-top:1px solid var(--border); padding-top:16px; }
"""

def main():
    if not SRC.exists():
        print(f"源文件不存在: {SRC}", file=sys.stderr); sys.exit(1)
    text = SRC.read_text(encoding="utf-8")

    try:
        import markdown
        body = markdown.markdown(
            text,
            extensions=["tables", "fenced_code", "toc", "sane_lists"],
        )
    except ImportError:
        # 退化方案：无 markdown 库时直接转义
        body = f"<pre>{text}</pre>"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI 短剧 / 漫剧 开源开发工具调研报告</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{body}
<div class="footnote">本报告由 WorkBuddy 生成并部署至 GitHub Pages ｜ 数据抓取于 2026-07-07</div>
</div>
</body>
</html>"""
    OUT.write_text(html, encoding="utf-8")
    print(f"已生成: {OUT}  ({len(html)} bytes)")

if __name__ == "__main__":
    main()
