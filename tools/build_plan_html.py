"""Build plan.md and plan.html from this repository's plan.source.json (stdlib only)."""
from pathlib import Path
import html, json

root = Path(__file__).resolve().parents[1]
data = json.loads((root/'docs/plans/plan.source.json').read_text(encoding='utf-8'))
esc = html.escape
pages, sources = data['pages'], data['sources']
css = 'body{font-family:system-ui,"Microsoft YaHei",sans-serif;background:#f2f5f7;color:#24374a;line-height:1.85;margin:0}main{max-width:1000px;margin:28px auto;padding:30px 42px;background:white}h1,h2{color:#16324d}h3,a{color:#087e8b}table{border-collapse:collapse;width:100%;margin:18px 0}th,td{border:1px solid #d7e3ea;padding:10px;text-align:left;vertical-align:top}th{background:#16324d;color:white}.box{background:#eff6f8;border-left:4px solid #087e8b;padding:16px}.page{border-top:1px solid #d7e3ea;margin-top:30px;padding-top:14px}.sub{color:#63758a}a{overflow-wrap:anywhere}@media(max-width:700px){main{padding:16px}table{font-size:13px}}'
out = ['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(pages[0]['title'])+'</title><style>'+css+'</style><main><h1>'+esc(pages[0]['title'])+'</h1><p class="sub">v'+esc(data['version'])+' · '+esc(data['snapshot_date'])+' · 计划，不代表已实现。</p><ol>']
out += [f'<li><a href="#p{i}">{esc(pg["title"])}</a></li>' for i,pg in enumerate(pages,1)]
out.append('</ol>')
md=['# '+pages[0]['title'], '', '版本：v'+data['version']+'；审核日期：'+data['snapshot_date']+'。计划目标不等于已完成成果。', '', '本文件与 HTML 由 plan.source.json 生成；PDF 是同版本固定快照。进度证据记录在 [PROGRESS](../PROGRESS.md)。', '']
def cell(s): return s.replace('|',chr(92)+'|').replace('\n','<br>')
for i,pg in enumerate(pages,1):
    out.append(f'<section class="page" id="p{i}"><h2>{i:02d} {esc(pg["title"])}</h2><p class="sub">{esc(pg["subtitle"])}</p>')
    md += ['## '+pg['title'], '', pg['subtitle'], '']
    for b in pg['blocks']:
        typ=b['type']
        if typ in ('p','h','box'):
            tag='h3' if typ=='h' else 'p';cl=' class="box"' if typ=='box' else ''
            out.append(f'<{tag}{cl}>{esc(b["text"]).replace(chr(10),"<br>")}</{tag}>')
            prefix='### ' if typ=='h' else '> ' if typ=='box' else ''
            md += [prefix+b['text'], '']
        elif typ=='bullets':
            out.append('<ul>'+''.join('<li>'+esc(s)+'</li>' for s in b['items'])+'</ul>')
            md += ['- '+s for s in b['items']]+['']
        elif typ=='refs':
            out.append('<p>'+' · '.join(f'<a href="{esc(sources[k][1])}">{esc(sources[k][0])}</a>' for k in b['ids'])+'</p>')
            md += ['资料：'+' · '.join('['+sources[k][0]+']('+sources[k][1]+')' for k in b['ids']), '']
        elif typ=='table':
            out.append('<table><tr>'+''.join('<th>'+esc(s)+'</th>' for s in b['head'])+'</tr>'+''.join('<tr>'+''.join('<td>'+esc(s)+'</td>' for s in row)+'</tr>' for row in b['rows'])+'</table>')
            md += ['| '+' | '.join(cell(s) for s in b['head'])+' |', '| '+' | '.join('---' for s in b['head'])+' |']
            md += ['| '+' | '.join(cell(s) for s in row)+' |' for row in b['rows']]+['']
    out.append('</section>')
out.append('</main></html>')
for name, text in [('plan.html','\n'.join(out)), ('plan.md','\n'.join(md))]:
    dest=root/'docs/plans'/name
    dest.write_text(text.rstrip()+'\n',encoding='utf-8',newline='\n')
    print(dest)
