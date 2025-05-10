# UniAgenda - Agenda de Atividades Acadêmicas

Aplicação para organização de atividades acadêmicas como aulas, prazos de trabalhos e eventos universitários.

---

## Tecnologias Utilizadas

- **Backend**: Django REST Framework  
- **Frontend**: HTML, CSS (Bulma), JavaScript  
- **Banco de dados**: SQLite (padrão do Django)

---

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd uniagenda
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   # No Linux/macOS:
   source venv/bin/activate
   # No Windows:
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Acesse no navegador:**
   ```
   http://localhost:8000
   ```

---

## Uso

- **Adicionar atividade**: Preencha o formulário e clique em "Adicionar Atividade"  
- **Visualizar atividades**: A lista é carregada automaticamente  
- **Excluir atividade**: Clique no botão "Excluir" da atividade desejada

---

## Estrutura do Projeto

```
/uniagenda
│
├── /rest(UniAgenda)
│   ├── manage.py
│   ├── /UniAgenda
│   │   └── settings.py, urls.py
│   └── /agenda
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
│
├── /frontend
│   ├── index.html
│
└── README.md
```

---

## 🔌 Rotas da API

| Método | Rota                | Descrição                       |
|--------|---------------------|----------------------------------|
| GET    | `/atividades/`      | Lista todas as atividades       |
| POST   | `/atividades/`      | Cria uma nova atividade         |
| GET    | `/atividades/<id>/` | Mostra uma atividade específica |
| DELETE | `/atividades/<id>/` | Remove uma atividade específica |

---

## 🧾 Modelo de Dados

```json
{
  "id": 1,
  "titulo": "Entrega do trabalho de Redes",
  "descricao": "Finalizar e enviar o trabalho sobre protocolos TCP/IP",
  "data": "2025-05-10",
  "hora": "23:59",
  "status": "pendente"
}
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Siga os passos abaixo:

1. Faça um fork do projeto  
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nomeDaFeature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -am 'Add nova feature'
   ```
4. Faça push para a branch:
   ```bash
   git push origin feature/nomeDaFeature
   ```
5. Crie um novo Pull Request

---

**Licença:** [Especifique aqui, ex: MIT, GPL, etc.]