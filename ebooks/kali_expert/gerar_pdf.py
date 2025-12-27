import markdown
import asyncio
from playwright.async_api import async_playwright
import os

# Caminhos
md_file = r'c:\SISTEMA_ORIGEM\WIKI_MATHEUS_TI\ebooks\kali_expert\KALI_LINUX_EXPERT_COMPLETO.md'
output_pdf = r'c:\SISTEMA_ORIGEM\WIKI_MATHEUS_TI\ebooks\kali_expert\KALI_LINUX_EXPERT_MASTER_EDITION.pdf'

async def generate_premium_pdf():
    # 1. Ler o Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Converter Markdown para HTML (com suporte a TOC)
    # Adicionamos [TOC] no início para forçar a geração do sumário
    if "[TOC]" not in text:
        text = "[TOC]\n\n" + text
        
    html_content = markdown.markdown(text, extensions=['extra', 'codehilite', 'toc'])

    # 3. HTML & CSS Ultra-Premium (Modern Glassmorphism & Cyberpunk)
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

            * {{
                box-sizing: border-box;
                -webkit-print-color-adjust: exact;
            }}

            body {{
                margin: 0;
                padding: 0;
                background-color: var(--bg-color);
                color: var(--text-main);
                font-family: 'Inter', sans-serif;
                font-size: 11pt;
                line-height: 1.7;
            }}

            /* WATERMARK */
            .watermark {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%) rotate(-45deg);
                font-size: 80pt;
                color: rgba(255, 255, 255, 0.03);
                white-space: nowrap;
                pointer-events: none;
                z-index: -1;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 15px;
            }}

            /* CAPA ULTRA PREMIUM */
            .cover {{
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background: radial-gradient(circle at center, #1e1b4b 0%, #0c0e14 100%);
                text-align: center;
                position: relative;
                overflow: hidden;
            }}

            .cover::before {{
                content: "";
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                background-image: url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
                opacity: 0.1;
            }}

            .cover h1 {{
                font-size: 60pt;
                font-weight: 800;
                margin: 0;
                background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -2px;
                line-height: 1;
            }}

            .cover .subtitle {{
                font-size: 20pt;
                color: var(--secondary);
                text-transform: uppercase;
                letter-spacing: 12px;
                margin-top: 10px;
                font-weight: 300;
            }}

            .cover .author {{
                margin-top: 150px;
                font-size: 16pt;
                font-weight: 600;
                color: var(--primary);
            }}

            /* SUMÁRIO (TOC) */
            .toc {{
                padding: 1cm 2cm;
                page-break-after: always;
            }}
            .toc h2 {{ color: var(--secondary); border-bottom: 1px solid var(--primary); padding-bottom: 10px; }}
            .toc ul {{ list-style: none; padding-left: 0; }}
            .toc li {{ margin-bottom: 8px; border-bottom: 1px dotted var(--text-dim); display: flex; justify-content: space-between; align-items: baseline; }}
            .toc a {{ color: var(--text-main); text-decoration: none; font-weight: 600; font-size: 11pt; }}
            .toc a:hover {{ color: var(--primary); }}

            /* CONTEÚDO */
            .content-page {{
                padding: 2cm;
                position: relative;
                min-height: 100vh;
            }}

            h1 {{
                font-size: 32pt;
                font-weight: 800;
                color: var(--highlight);
                margin-top: 60px;
                margin-bottom: 30px;
                position: relative;
                page-break-before: always;
            }}

            h1::after {{
                content: "";
                display: block;
                width: 80px;
                height: 6px;
                background: linear-gradient(to right, var(--secondary), var(--primary));
                margin-top: 10px;
                border-radius: 3px;
            }}

            h2 {{
                font-size: 22pt;
                color: var(--secondary);
                margin-top: 45px;
                font-weight: 600;
            }}

            h3 {{
                color: var(--primary);
                font-size: 16pt;
                margin-top: 30px;
            }}

            p {{
                margin-bottom: 20px;
                color: var(--text-main);
            }}

            /* BLOCOS DE CÓDIGO (GLASSMOPHISM) */
            pre {{
                background: var(--card-bg);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-left: 4px solid var(--secondary);
                padding: 20px;
                border-radius: 12px;
                font-family: 'JetBrains Mono', monospace;
                font-size: 10pt;
                overflow-x: hidden;
                margin: 25px 0;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}

            code {{
                font-family: 'JetBrains Mono', monospace;
                color: var(--secondary);
                background: rgba(0, 243, 255, 0.1);
                padding: 2px 6px;
                border-radius: 4px;
            }}

            /* TABELAS MODERNAS */
            table {{
                width: 100%;
                border-collapse: separate;
                border-spacing: 0;
                margin: 30px 0;
                border-radius: 12px;
                overflow: hidden;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            th {{
                background-color: var(--primary);
                color: white;
                padding: 15px;
                text-align: left;
                font-weight: 600;
                text-transform: uppercase;
                font-size: 10pt;
            }}

            td {{
                background-color: var(--card-bg);
                padding: 12px 15px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }}

            tr:last-child td {{
                border-bottom: none;
            }}

            /* BLOCKQUOTES (ALERTS) */
            blockquote {{
                background: rgba(188, 19, 254, 0.05);
                border-left: 4px solid var(--primary);
                margin: 30px 0;
                padding: 20px 25px;
                border-radius: 0 12px 12px 0;
                color: var(--text-dim);
                font-style: italic;
            }}

            /* RODAPÉ E PÁGINA */
            @page {{
                margin: 0;
            }}

            .footer {{
                position: fixed;
                bottom: 30px;
                right: 30px;
                font-size: 8pt;
                color: var(--text-dim);
                opacity: 0.5;
            }}

        </style>
    </head>
    <body>
        <div class="watermark">MATHEUS TI - ELITE EDITION</div>
        
        <div class="cover">
            <h1>KALI LINUX<br>EXPERT</h1>
            <div class="subtitle">Master Edition</div>
            <div class="author">POR MATHEUS TI</div>
        </div>

        <div class="content-page">
            {html_content}
            <div class="footer">Kali Linux Expert: Master Edition | Matheus TI</div>
        </div>
    </body>
    </html>
    """

    # 4. Gerar o PDF com Playwright (Chromium)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Definir o conteúdo HTML
        await page.set_content(html_template)
        
        # Esperar fontes carregarem (opcional mas bom)
        await asyncio.sleep(2) 

        # Salvar como PDF
        await page.pdf(
            path=output_pdf,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        
        await browser.close()

    print(f"PDF ULTRA-PREMIUM gerado com sucesso em: {output_pdf}")

if __name__ == "__main__":
    asyncio.run(generate_premium_pdf())
