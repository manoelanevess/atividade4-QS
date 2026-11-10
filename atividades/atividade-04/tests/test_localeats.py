import re

from playwright.sync_api import Page, expect


# Responsável: Manoela das Neves
def test_abre_formulario_de_cadastro(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/", wait_until="domcontentloaded")
    expect(page).to_have_url(re.compile(r"/login\.html$"))

    page.get_by_role("button", name="Criar Conta", exact=True).click()

    expect(page.get_by_placeholder("Seu nome", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Registrar", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("Sua senha secreta", exact=True)).to_be_hidden()
