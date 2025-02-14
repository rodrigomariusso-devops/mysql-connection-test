# MySQL Connection Tester

## Descrição
Este projeto é um script Python para testar a conexão com um banco de dados MySQL, permitindo executar consultas e visualizar os resultados de forma rápida.

## Como usar

### 1. Clone o repositório:
```bash
git clone https://github.com/rodrigomariusso-devops/mysql-connection-test.git
cd mysql-connection-test
```

### 2. Instale as dependências
```bash
pip install mysql-connector-python
```

### 3. Configure as credenciais do banco de dados
Edite o arquivo `app.py` e altere as credenciais de conexão conforme necessário:
```python
config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'seu_host',
    'database': 'seu_banco',
}
```

### 4. Execute o script
```bash
python app.py
```

O script se conectará ao banco de dados MySQL e executará a query `SELECT * FROM ras_pre_evento`, exibindo os resultados no terminal.

## Estrutura do Projeto
```
MySQL-Connection-Tester/
│── app.py               # Script Python que testa a conexão com o MySQL e executa uma query
```

## Requisitos
- Python 3
- Biblioteca `mysql-connector-python` instalada (`pip install mysql-connector-python`)

## Possíveis Melhorias Futuras
- Adicionar suporte para entrada dinâmica de queries
- Implementar logs estruturados
- Criar suporte para múltiplos bancos de dados

---
Esse script facilita a validação de conexões com MySQL sem precisar configurar uma aplicação completa! 🚀

