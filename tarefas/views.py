from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"nome": "Courtois", "idade": "32", 
         "posicao": "Goleiro", 
         "nascimento": "Bree, Bélgica", 
         "foto": "img/courtois.webp"},
        {"nome": "Carvajal", "idade": "32", 
         "posicao": "Lateral", 
         "nascimento": "Leganés, Espanha", 
         "foto": "img/carvajal.webp"},
        {"nome": "E. Militão", "idade": "26", 
         "posicao": "Zagueiro", 
         "nascimento": "Sertãozinho, São Paulo", 
         "foto": "img/militao.webp"},
        {"nome": "Rudiger", "idade": "31", 
         "posicao": "Zagueiro", 
         "nascimento": "Berlim, Alemanha", 
         "foto": "img/rudiger.webp"},
        {"nome": "F. Mendy", "idade": "29", 
         "posicao": "Lateral", 
         "nascimento": "Meulan-en-Yvelines, França", 
         "foto": "img/mendy.webp"},
        {"nome": "Valverde", "idade": "26", 
         "posicao": "Meio-campista", 
         "nascimento": "Montevidéu, Uruguai", 
         "foto": "img/valverde.webp"},
        {"nome": "Modric", "idade": "38", 
         "posicao": "Meio-campista", 
         "nascimento": "Zadar, Croácia", 
         "foto": "img/modric.webp"},
        {"nome": "Bellingham", "idade": "21", 
         "posicao": "Meio-campista", 
         "nascimento": "Stourbridge, Reino Unido", 
         "foto": "img/bellingham.webp"},
        {"nome": "Rodrygo", "idade": "23", 
         "posicao": "Atacante", 
         "nascimento": "Osasco, São Paulo", 
         "foto": "img/rodrygo.webp"},
        {"nome": "Mbappé", "idade": "25", 
         "posicao": "Atacante", 
         "nascimento": "Paris, França", 
         "foto": "img/mbappe.webp"},
        {"nome": "Vini Jr.", "idade": "23", 
         "posicao": "Atacante", 
         "nascimento": "São Gonçalo, Rio de Janeiro", 
         "foto": "img/vini.webp"},
        {"nome": "Carlo Ancelotti", "idade": "65", 
         "posicao": "Técnico", 
         "nascimento": "Reggiolo, Itália", 
         "foto": "img/ancelotti.webp"},

    ]

    context = {
        "jogadores": jogadores,
    }
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")