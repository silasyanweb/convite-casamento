import base64, json, pathlib
R=pathlib.Path('/home/claude/convite'); T=pathlib.Path('/home/claude/tools')
src=(R/'src/index.html').read_text()
def uri(p,mime): return f'data:{mime};base64,'+base64.b64encode((R/'img'/p).read_bytes()).decode()
img={'bg':uri('bg.webp','image/webp'),'couple':uri('couple.webp','image/webp'),'venue':uri('venue.webp','image/webp'),
     'hands':uri('hands.webp','image/webp'),'lineart':uri('lineart.webp','image/webp'),
     'floraltr':uri('floral-tr.webp','image/webp'),'floralbl':uri('floral-bl.webp','image/webp')}
src=src.replace('"__IMG_JSON__"', json.dumps(img))
src=src.replace('/*__GSAP__*/', (T/'node_modules/gsap/dist/gsap.min.js').read_text().replace('</script','<\\/script'))
src=src.replace('/*__QR__*/', (T/'node_modules/qrcode-generator/qrcode.js').read_text().replace('</script','<\\/script'))
(R/'dist').mkdir(exist_ok=True)
(R/'dist/index.html').write_text(src)
print(len(src)//1024,'KB')
