from urllib import request
from bs4 import BeautifulSoup

urls = [
    "http://www.tvi.iol.pt/vocenatv/extras/brownie-marmorizado/5704ddba0cf279af1523f32f",
    "http://www.tvi.iol.pt/vocenatv/extras/empadao-de-vitela-com-espinafres/570e19710cf248fe7e37045a",
    "http://www.tvi.iol.pt/vocenatv/extras/quindins-e-pavlova/57175de40cf273cab45f8afd",
    "http://www.tvi.iol.pt/vocenatv/extras/massa-chinesa-com-frango-e-legumes/572093ed0cf209b36b77b9c3",
    "http://www.tvi.iol.pt/vocenatv/extras/bolo-salgado-com-sobras-de-frango/5720952d0cf209b36b77b9c6",
    "http://www.tvi.iol.pt/vocenatv/extras/bolo-de-laranja-sem-ovos/5729e22a0cf2d018a523df27",
    "http://www.tvi.iol.pt/vocenatv/extras/trifle-de-morangos/5729e3fa0cf2cfe9f10d5f57",
    "http://www.tvi.iol.pt/vocenatv/extras/polvo-com-ervas-e-esmagada-de-favas/573308630cf220340222048a",
    "http://www.tvi.iol.pt/vocenatv/extras/salada-de-polvo-com-espargos-e-abacate/573309c60cf209b36b78a746",
    "http://www.tvi.iol.pt/vocenatv/extras/tiramisu/573c3e2e0cf209b36b79129d",
    "http://www.tvi.iol.pt/vocenatv/extras/tiramisu-com-queijo-quark/573c3f8f0cf273cab4614a85",
    "http://www.tvi.iol.pt/vocenatv/extras/bacalhau-tostado/5745b8440cf2aba6b0a56b21",
    "http://www.tvi.iol.pt/vocenatv/extras/pao-de-bacalhau/5745b96f0cf2e1c448ae4f91",
    "http://www.tvi.iol.pt/vocenatv/extras/pudim-de-gemas-com-vinho-do-porto/574d5f160cf22f3ce42ea452",
    "http://www.tvi.iol.pt/vocenatv/extras/molotof-sem-forno/574d60110cf22f3ce42ea455",
    "http://www.tvi.iol.pt/vocenatv/extras/tarte-de-feijao-branco/5757f6440cf2b4e23cc4b8e9",
    "http://www.tvi.iol.pt/vocenatv/extras/feijao-branco-com-ovos-escalfados/5757fd080cf22c4188c40626",
    "http://www.tvi.iol.pt/vocenatv/extras/pannacotta-com-cerejas/576166400cf22c4188c42208",
    "http://www.tvi.iol.pt/vocenatv/extras/triffle-de-cerejas-tipo-floresta-negra/57616d0b0cf22f3ce42ee471",
    "http://www.tvi.iol.pt/vocenatv/extras/cerejas-em-vinagre/5762738f0cf22c4188c425b9",
    "http://www.tvi.iol.pt/vocenatv/extras/almondegas-de-frango-com-tomate/57697b900cf22f3ce42efd15",
    "http://www.tvi.iol.pt/vocenatv/extras/espetadas-de-frango-com-coentros/57697c8d0cf29c0e4d981793",
    "http://www.tvi.iol.pt/vocenatv/extras/bolo-de-polenta/57739a6f0cf22f3ce42f1b38",
    "http://www.tvi.iol.pt/vocenatv/extras/polenta-recheada-com-carne/577398d20cf2b4e23cc50def",
    "http://www.tvi.iol.pt/vocenatv/extras/delicia-de-tomate-e-maca/577cc7750cf22c4188c4768f",
    "http://www.tvi.iol.pt/vocenatv/extras/sopa-fria-de-tomate/577cc7db0cf29c0e4d9851ec",
    "http://www.tvi.iol.pt/vocenatv/extras/sopa-de-beldroegas-com-queijo/57863c0a0cf2b4e23cc5473c",
    "http://www.tvi.iol.pt/vocenatv/extras/alhos-assados-no-forno/57863c7d0cf2b4e23cc5473f",
    "http://www.tvi.iol.pt/vocenatv/extras/alhos-em-conserva/578641270cf2edf5f6b59bca",
    "http://www.tvi.iol.pt/vocenatv/extras/figos-recheados-com-carnes-e-ervas-aromaticas/578f87a10cf2d6e7c123beb1",
    "http://www.tvi.iol.pt/vocenatv/extras/tarte-de-figos-com-amendoa/578f88010cf2d6e7c123beb4",
    "http://www.tvi.iol.pt/vocenatv/extras/gelado-de-agua-com-frutos-vermelhos/5798892a0cf22c4188c4c47e",
    "http://www.tvi.iol.pt/vocenatv/extras/granizado-de-melancia/57988c140cf2b4e23cc5776e",
    "http://www.tvi.iol.pt/vocenatv/extras/panna-cotta-de-lucia-lima-com-calda-de-morangos/57988d290cf2edf5f6b5ccd3",
    "http://www.tvi.iol.pt/vocenatv/extras/cassata-de-baunilha-e-frutos-vermelhos/579893fe0cf2edf5f6b5cd0f",
    "http://www.tvi.iol.pt/vocenatv/extras/tarte-cremosa-de-maca/57a1bdb90cf2d6e7c123f0b8",
    "http://www.tvi.iol.pt/vocenatv/extras/filet-mignon-com-maca/57a1be0f0cf2d6e7c123f0bd",
    "http://www.tvi.iol.pt/vocenatv/extras/mousse-de-meloa/57ab0a1a0cf224ef98310978",
    "http://www.tvi.iol.pt/vocenatv/extras/meloa-grelhada-com-pesto-de-rucula/57ab087f0cf2570e796704af",
    "http://www.tvi.iol.pt/vocenatv/extras/pizza-de-ricota-e-presunto/57b343530cf2c4de0f5ecee2",
    "http://www.tvi.iol.pt/vocenatv/extras/flan-de-ricotta/57b344a50cf2c4de0f5ecefc",
    "http://www.tvi.iol.pt/vocenatv/extras/perna-de-pato-confitada-com-ameixas-frescas/57bd85fd0cf2b1af9832f71b",
    "http://www.tvi.iol.pt/vocenatv/extras/cheesecake-de-ameixas-frescas/57bda7870cf2b1af9832f7ba",
    "http://www.tvi.iol.pt/vocenatv/extras/bolo-de-mousse-de-chocolate/57c6b9330cf2d382b7e9615d",
    "http://www.tvi.iol.pt/vocenatv/extras/tacas-de-brownie-com-gelado-de-maracuja/57c6ba630cf2e4335317bb51",
]

_k = 0

for _p in urls:
    _pc = request.urlopen(request.Request(_p, headers={'User-Agent': 'Mozilla'})).read()
    _s = BeautifulSoup(_pc, "html.parser")
    _f = _s.find_all("div", class_="artigo-text", recursive=True)
    _t = _s.find_all("h1")
    with open("output/" + "tvi_" + str(_k) + "_" + _t[0].text.replace(' ', '_') + ".txt", "w") as f:
        f.write(_t[0].text + "\n\n")
        f.write(_f[0].text)
        print("Wrote {}.".format(_t[0].text))
    _k += 1
