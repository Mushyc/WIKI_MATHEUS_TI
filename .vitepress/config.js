export default {
  title: "Matheus TI",
  description: "Knowledge Base & Technical Study Center",
  ignoreDeadLinks: true,
  markdown: {
    mermaid: true
  },
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: '🎓 Roadmap', link: '/estudos/Roadmap_Estudos' },
      {
        text: 'Fundamentos',
        items: [
          { text: '📊 Algoritmos & Estruturas', link: '/guias/Curso_Algoritmos_Estruturas_Dados' },
          { text: '🎨 POO', link: '/guias/Curso_POO_Pratica' },
          { text: '🐧 Linux', link: '/guias/Curso_Dominio_Linux' },
          { text: '🌐 Redes', link: '/guias/Curso_Redes_Computadores' }
        ]
      },
      {
        text: 'Desenvolvimento',
        items: [
          { text: '🐍 Python', link: '/guias/Curso_Python_Automacao' },
          { text: '💻 Web Dev', link: '/guias/Guia_Desenvolvimento_Web' },
          { text: '🔀 Git & GitHub', link: '/guias/Curso_Git_GitHub' },
          { text: '🗄️ Banco de Dados', link: '/guias/Curso_Banco_Dados_Avancado' }
        ]
      },
      {
        text: 'Infraestrutura',
        items: [
          { text: '🖥️ Montagem PC', link: '/guias/Curso_Montagem_Manutencao_PC' },
          { text: '🏢 Windows Server', link: '/guias/Curso_Windows_Server_AD' },
          { text: '☁️ Cloud Computing', link: '/guias/Curso_Cloud_Computing' }
        ]
      },
      {
        text: 'Especialização',
        items: [
          { text: '💀 Kali Linux', link: '/guias/Curso_Pratico_Kali_Expert' },
          { text: '🛠️ Ferramentas Pen-drive', link: '/guias/Curso_Ferramentas_Pendrive' },
          { text: '🧮 Fundamentos CS', link: '/guias/Curso_Fundamentos_CS' }
        ]
      },
      { text: 'Referências', link: '/referencias/Galeria_Imagens' }
    ],
    sidebar: {
      '/guias/': [
        {
          text: '🎯 Essenciais (Comece Aqui)',
          collapsed: false,
          items: [
            { text: '📊 Algoritmos & Estruturas de Dados', link: '/guias/Curso_Algoritmos_Estruturas_Dados' },
            { text: '🎨 Programação Orientada a Objetos', link: '/guias/Curso_POO_Pratica' },
            { text: '🔀 Git e GitHub Profissional', link: '/guias/Curso_Git_GitHub' },
            { text: '🧮 Fundamentos de Ciência da Computação', link: '/guias/Curso_Fundamentos_CS' }
          ]
        },
        {
          text: '💻 Infraestrutura e Sistemas',
          collapsed: false,
          items: [
            { text: '🐧 Domínio do Linux', link: '/guias/Curso_Dominio_Linux' },
            { text: '🌐 Redes de Computadores', link: '/guias/Curso_Redes_Computadores' },
            { text: '🖥️ Montagem e Manutenção de PCs', link: '/guias/Curso_Montagem_Manutencao_PC' },
            { text: '🏢 Windows Server & AD', link: '/guias/Curso_Windows_Server_AD' }
          ]
        },
        {
          text: '🚀 Desenvolvimento',
          items: [
            { text: '🐍 Python para Automação', link: '/guias/Curso_Python_Automacao' },
            { text: '💻 Desenvolvimento Web', link: '/guias/Guia_Desenvolvimento_Web' },
            { text: '🗄️ Banco de Dados Avançado', link: '/guias/Curso_Banco_Dados_Avancado' }
          ]
        },
        {
          text: '🔐 Segurança e Cloud',
          items: [
            { text: '💀 Kali Linux Expert', link: '/guias/Curso_Pratico_Kali_Expert' },
            { text: '🛡️ Kali Linux Master', link: '/guias/Guia_Tecnico_Kali' },
            { text: '☁️ Cloud Computing Essentials', link: '/guias/Curso_Cloud_Computing' },
            { text: '🛠️ Ferramentas do Pen-drive', link: '/guias/Curso_Ferramentas_Pendrive' }
          ]
        },
        {
          text: '📋 Carreira e Profissionalização',
          items: [
            { text: '🔍 Troubleshooting Profissional', link: '/guias/Guia_Troubleshooting_Profissional' },
            { text: '📜 Roadmap de Certificações', link: '/guias/Guia_Roadmap_Certificacoes' },
            { text: '💬 Atendimento Técnico de Elite', link: '/guias/Guia_Atendimento_Elite' }
          ]
        }
      ],
      '/estudos/': [
        {
          text: '🎓 Planejamento',
          items: [
            { text: '📅 Roadmap de Estudos', link: '/estudos/Roadmap_Estudos' }
          ]
        },
        {
          text: '🔬 Laboratório',
          items: [
            { text: 'Workbook Kali Linux', link: '/estudos/Workbook_Estudo_Kali' }
          ]
        }
      ],
      '/referencias/': [
        {
          text: '🖼️ Biblioteca Visual',
          items: [
            { text: 'Galeria de Imagens', link: '/referencias/Galeria_Imagens' }
          ]
        }
      ]
    },
    footer: {
      message: 'Matheus TI | Knowledge Base',
      copyright: 'Copyright © 2025'
    },
    search: {
      provider: 'local'
    }
  }
}
