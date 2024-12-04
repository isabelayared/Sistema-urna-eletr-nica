# Urna Eletrônica Simulada com Segurança Criptográfica 🚀

Este projeto implementa um sistema de **urna eletrônica simulada**, desenvolvido em Python, com foco na **transmissão segura de votos**. O sistema utiliza **criptografia com XOR**, **Base64** e **Hash** para garantir a integridade e autenticidade dos dados. Ele oferece um ambiente seguro para registrar, criptografar e apurar votos, rejeitando arquivos não autenticados.

---

## 🛠️ Funcionalidades

1. **Registro de Votos:**
   - Os usuários podem registrar votos usando o código do candidato.
   - Todos os votos são criptografados antes do armazenamento.

2. **Criptografia e Hash:**
   - **XOR** e **Base64** são usados para criptografar os votos.
   - Um **hash autenticado** é gerado para verificar a integridade dos dados.

3. **Validação de Dados:**
   - O programa valida a integridade dos votos ao descriptografar e comparar o hash armazenado.
   - Arquivos com hash inválido são rejeitados, protegendo contra manipulação de dados.

4. **Apuração de Resultados:**
   - Exibe o relatório final dos votos para cada candidato, juntamente com o total de votos.

---

## 📋 Como Usar

### 1️⃣ Registro de Votos
- Execute o programa e escolha a opção de votação.
- Insira o código do candidato para registrar seu voto.

### 2️⃣ Criptografia e Salvamento
- Após o registro, os votos são criptografados com uma chave fornecida pelo usuário.
- Os dados criptografados são salvos em um arquivo para apuração futura.

### 3️⃣ Apuração de Votos
- Selecione a opção de apuração.
- Insira a chave usada na criptografia para validar os dados.
- O programa exibirá os votos dos candidatos e o total, desde que o hash seja válido.

---

## 🧑‍💻 Tecnologias Utilizadas

- **Python:** Linguagem de programação para implementar o sistema.
- **Criptografia com XOR:** Para garantir a segurança dos dados.
- **Base64:** Para codificação dos dados criptografados.
- **Hash:** Para validar a integridade dos votos.

---

## 📁 Estrutura do Projeto

- `criptografia_votos`: Arquivo onde os votos criptografados, o hash e o total são armazenados.
- **Funções principais:**
  - `registrar_votos`: Registra e exibe os candidatos disponíveis.
  - `xor` / `xor_decrypt`: Criptografa e descriptografa os votos.
  - `texto_para_base64` / `base64_para_texto`: Codifica e decodifica os dados em Base64.
  - `hash_dados`: Gera o hash para autenticação dos votos.
  - `ver_dados`: Valida e exibe os resultados de votação.

---

## 🛡️ Segurança

- **Integridade:** O uso de hash impede adulterações nos dados.
- **Autenticidade:** Arquivos sem o hash correto são rejeitados durante a apuração.
- **Confidencialidade:** Apenas quem possui a chave consegue descriptografar os votos.

---

## 📌 Pré-requisitos

- Python 3.8 ou superior instalado na máquina.

---

## 📝 Notas

- A chave de criptografia deve ser **guardada com segurança**, pois é essencial para validar e descriptografar os votos.
- Modificações nos arquivos podem invalidar o hash, tornando os dados inutilizáveis.

---


## 🌟 Contribua

Sinta-se à vontade para abrir **issues** ou enviar **pull requests**. Vamos melhorar juntos!  

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT.  

> **Dica:** Não se esqueça de dar ⭐ no repositório se gostou!
