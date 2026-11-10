# Atividade 4 — Testes automatizados do LocalEats

**Unidade curricular** — Qualidade de Software  
**Modalidade** — Individual  
**Estudante** — Manoela das Neves

## 1. TDD de Manoela das Neves

**Regra escolhida** — O pedido atinge o valor mínimo a partir de R$ 30,00. Valores menores retornam `False` e valores negativos geram `ValueError`.

**Primeiro teste escrito** — O TU01 usa exatamente R$ 30,00 e espera `True`.

**Por que falhou inicialmente** — A primeira versão da função lançava `NotImplementedError`. A execução terminou com `1 failed`.

**Implementação mínima** — A função passou a retornar `True`. A execução seguinte mostrou `1 passed`.

**Segundo teste escrito** — O TU02 usa R$ 29,99 e espera `False`. Ele falhou porque a função ainda retornava `True` para qualquer valor. Com a comparação `valor_pedido >= 30`, os dois testes passaram.

**Melhoria realizada** — O TU03 verificou que um valor negativo precisa gerar `ValueError`. O teste falhou porque a comparação retornava `False` para esse valor. A validação de negativos foi colocada antes da comparação com o mínimo.

## 2. Teste funcional

O TF01 abre o site em uma sessão nova. O teste confirma o redirecionamento para a tela de login e clica em **Criar Conta**. Em seguida, verifica se o campo **Seu nome** e o botão **Registrar** ficam visíveis e se o campo de senha do login fica oculto. O cenário termina na abertura do formulário. [LocalEats](https://local-eats-unisenac.vercel.app/)

## 3. Responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| --- | --- | --- | --- | --- |
| TU01 | Manoela das Neves | Unitário | Pedido de R$ 30,00 atinge o mínimo | `tests/test_regras_localeats.py::test_pedido_de_trinta_reais_atinge_o_minimo` |
| TU02 | Manoela das Neves | Unitário | Pedido de R$ 29,99 fica abaixo do mínimo | `tests/test_regras_localeats.py::test_pedido_um_centavo_abaixo_do_minimo` |
| TU03 | Manoela das Neves | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_erro` |
| TF01 | Manoela das Neves | Funcional | A opção **Criar Conta** troca o formulário de login pelo de cadastro | `tests/test_localeats.py::test_abre_formulario_de_cadastro` |

## 4. Explicação do TU01

O valor de R$ 30,00 é o primeiro que atende à regra. O teste chama a função com esse valor e usa `is True` para conferir o retorno booleano. Se alguém trocar `>=` por `>`, o pedido de R$ 30,00 será recusado e esse teste vai falhar.

## 5. Como executar no PowerShell

Na pasta `atividades/atividade-04`, com o ambiente virtual ativo, instale as dependências e o Chromium. O teste funcional precisa de acesso ao site.

```powershell
python -m pip install -r requirements.txt
python -m playwright install --only-shell chromium
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Os três testes unitários e o teste funcional passaram. O pytest também registrou um aviso de depreciação na fixture `base_url` do plugin de testes. [Relatório da execução](relatorio-pytest.txt)

## 6. Uso de inteligência artificial

**Ferramenta utilizada** — ChatGPT (Codex).

**Como foi utilizada** — Usei o ChatGPT como auxílio para escrever a função, os testes em Python e este relatório.

**Sugestão alterada** — A primeira ideia era testar a busca de restaurantes. O site redireciona visitantes sem sessão para o login. O cenário foi ajustado para verificar a troca do formulário de login para o de cadastro.

**Como o código foi verificado** — Os testes unitários foram executados antes e depois dos ajustes na função. O cenário funcional foi executado com Playwright no Chromium, usando o site publicado. A saída completa da suíte está no arquivo `relatorio-pytest.txt`.
