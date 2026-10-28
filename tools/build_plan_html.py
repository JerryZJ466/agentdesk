"""Build this repository's plan HTML using only Python's standard library."""
from pathlib import Path
import html, json

root=Path(__file__).resolve().parents[1]
src=root/'docs/plans/plan.source.json'
data=json.loads(src.read_text(encoding='utf-8'))
esc=html.escape
css='body{font-family:system-ui,"Microsoft YaHei",sans-serif;background:#f2f5f7;color:#24374a;line-height:1.85;margin:0}main{max-width:1000px;margin:28px auto;padding:30px 42px;background:white}h1,h2{color:#16324d}h3,a{color:#087e8b}table{border-collapse:collapse;width:100%;margin:18px 0}th,td{border:1px solid #d7e3ea;padding:10px;text-align:left;vertical-align:top}th{background:#16324d;color:white}.box{background:#eff6f8;border-left:4px solid #087e8b;padding:16px}.page{border-top:1px solid #d7e3ea;margin-top:30px;padding-top:14px}.sub{color:#63758a}a{overflow-wrap:anywhere}'
pages=data['pages'];sources=data['sources']
out=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(pages[0]['title'])+'</title><style>'+css+'</style><main><h1>'+esc(pages[0]['title'])+'</h1><p class="sub">计划快照 '+esc(data['snapshot_date'])+' · 时间估算以仓库中的“面试准备与时间评估”为准。</p><ol>']
out += [f'<li><a href="#p{i}">{esc(pg["title"])}</a></li>' for i,pg in enumerate(pages,1)]
out.append('</ol>')
for i,pg in enumerate(pages,1):
 out.append(f'<section class="page" id="p{i}"><h2>{i:02d} {esc(pg["title"])}</h2><p class="sub">{esc(pg["subtitle"])}</p>')
 for b in pg['blocks']:
  typ=b['type']
  if typ in ('p','h','box'):
   tag='h3' if typ=='h' else 'p';cl=' class="box"' if typ=='box' else ''
   out.append(f'<{tag}{cl}>{esc(b["text"]).replace(chr(10),"<br>")}</{tag}>')
  elif typ=='bullets':out.append('<ul>'+''.join('<li>'+esc(s)+'</li>' for s in b['items'])+'</ul>')
  elif typ=='refs':out.append('<p>'+' · '.join(f'<a href="{esc(sources[k][1])}">{esc(sources[k][0])}</a>' for k in b['ids'])+'</p>')
  elif typ=='table':out.append('<table><tr>'+''.join('<th>'+esc(s)+'</th>' for s in b['head'])+'</tr>'+''.join('<tr>'+''.join('<td>'+esc(s)+'</td>' for s in row)+'</tr>' for row in b['rows'])+'</table>')
 out.append('</section>')
out.append('</main></html>')
outpath=root/'docs/plans/plan.html'
outpath.write_text('\n'.join(out),encoding='utf-8')
print(outpath)
