import markdown
import asyncio
from playwright.async_api import async_playwright
import os

# Configurações Gerais
BASE_DIR = r'c:\SISTEMA_ORIGEM\WIKI_MATHEUS_TI'
OUTPUT_DIR = os.path.join(BASE_DIR, 'ebooks', 'premium_pdfs')

FILES_TO_CONVERT = [
    {'name': 'Redes_Computadores', 'path': os.path.join(BASE_DIR, 'guias', 'Curso_Redes_Computadores.md'), 'subtitle': 'Redes de Computadores'},
    {'name': 'Dominio_Linux', 'path': os.path.join(BASE_DIR, 'guias', 'Curso_Dominio_Linux.md'), 'subtitle': 'Domínio Linux'},
    {'name': 'Troubleshooting', 'path': os.path.join(BASE_DIR, 'guias', 'Guia_Troubleshooting_Profissional.md'), 'subtitle': 'Troubleshooting Profissional'},
    {'name': 'Roadmap', 'path': os.path.join(BASE_DIR, 'estudos', 'Roadmap_Estudos.md'), 'subtitle': 'Elite Tech Roadmap'},
]

async def generate_pdf(file_info):
    md_file = file_info['path']
    name = file_info['name']
    subtitle = file_info['subtitle']
    output_pdf = os.path.join(OUTPUT_DIR, f"{name}_MASTER_EDITION.pdf")

    if not os.path.exists(md_file):
        print(f"[-] Arquivo não encontrado: {md_file}")
        return

    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Injetar TOC
    if "[TOC]" not in text:
        text = "[TOC]\n\n" + text

    html_content = markdown.markdown(text, extensions=['extra', 'codehilite', 'toc'])

    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400;600&display=swap');

            :root {{
                --bg-color: #0c0e14;
                --card-bg: #161a23;
                --primary: #bc13fe;
                --secondary: #00f3ff;
                --text-main: #e2e8f0;
                --text-dim: #94a3b8;
                --highlight: #f1f5f9;
            }}

            * {{ box-sizing: border-box; -webkit-print-color-adjust: exact; }}

            body {{
                margin: 0; padding: 0;
                background-color: var(--bg-color);
                color: var(--text-main);
                font-family: 'Inter', sans-serif;
                font-size: 11pt; line-height: 1.7;
            }}

            .watermark {{
                position: fixed; top: 50%; left: 50%;
                transform: translate(-50%, -50%) rotate(-45deg);
                font-size: 80pt; color: rgba(255, 255, 255, 0.03);
                white-space: nowrap; pointer-events: none; z-index: -1;
                font-weight: 800; text-transform: uppercase; letter-spacing: 15px;
            }}

            .cover {{
                height: 100vh; display: flex; flex-direction: column;
                justify-content: center; align-items: center;
                background: radial-gradient(circle at center, #1e1b4b 0%, #0c0e14 100%);
                text-align: center; position: relative; overflow: hidden;
            }}

            .cover h1 {{
                font-size: 50pt; font-weight: 800; margin: 0;
                background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                letter-spacing: -1px; line-height: 1.1;
                text-transform: uppercase;
            }}

            .cover .subtitle {{
                font-size: 18pt; color: var(--secondary);
                text-transform: uppercase; letter-spacing: 8px;
                margin-top: 15px; font-weight: 300;
            }}

            .cover .brand {{
                margin-top: 100px; font-size: 14pt; font-weight: 600; color: var(--primary);
            }}

            .content-page {{ padding: 2cm; position: relative; min-height: 100vh; }}
            
            h1 {{ font-size: 28pt; font-weight: 800; color: var(--highlight); margin-top: 50px; page-break-before: always; }}
            h1::after {{ content: ""; display: block; width: 60px; height: 5px; background: linear-gradient(to right, var(--secondary), var(--primary)); margin-top: 8px; border-radius: 3px; }}
            
            h2 {{ font-size: 20pt; color: var(--secondary); margin-top: 40px; }}
            pre {{ background: var(--card-bg); border-left: 4px solid var(--secondary); padding: 15px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 9pt; margin: 20px 0; }}
            blockquote {{ background: rgba(188, 19, 254, 0.05); border-left: 4px solid var(--primary); padding: 15px; margin: 20px 0; font-style: italic; color: var(--text-dim); }}
            
            .footer {{ position: fixed; bottom: 30px; right: 30px; font-size: 8pt; color: var(--text-dim); opacity: 0.4; }}
        </style>
    </head>
    <body>
        <div class="watermark">MATHEUS TI - ELITE</div>
        <div class="cover">
            <h1>{subtitle}</h1>
            <div class="subtitle">Master Edition</div>
            <div class="brand">ACADEMIA MATHEUS TI</div>
        </div>
        <div class="content-page">
            {html_content}
            <div class="footer">Matheus TI Academy | {subtitle} Master Edition</div>
        </div>
    </body>
    </html>
    """

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_template)
        await asyncio.sleep(2)
        await page.pdf(path=output_pdf, format="A4", print_background=True)
        await browser.close()

    print(f"[+] Gerado: {output_pdf}")

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for file_info in FILES_TO_CONVERT:
        await generate_pdf(file_info)

if __name__ == "__main__":
    asyncio.run(main())
