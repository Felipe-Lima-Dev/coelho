from django.shortcuts import render, redirect, get_object_or_404
from .models import Viagem, Passageiro

# 1. Tela de Login (index.html) - Rota Raiz
def login_view(request):
    if request.method == 'POST':
        # Futuramente podes adicionar autenticação real aqui.
        # Por enquanto, redireciona para a lista de viagens após submeter.
        return redirect('listar_viagens')
    return render(request, 'gestao/index.html')


# 2. Listagem de Viagens (relacaoviagens.html)
def listar_viagens(request):
    viagens = Viagem.objects.all()
    context = {'viagens': viagens}
    return render(request, 'gestao/relacaoviagens.html', context)


# 3. Cadastrar Nova Viagem (novaviagem.html)
def nova_viagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        cidade_inicio = request.POST.get('cidade_inicio')
        cidade_termino = request.POST.get('cidade_termino')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        horario_saida = request.POST.get('horario_saida')
        horario_chegada = request.POST.get('horario_chegada')
        
        # Cria a viagem na base de dados
        Viagem.objects.create(
            nome = nome,
            descricao = descricao,
            cidade_inicio = cidade_inicio,
            cidade_termino = cidade_termino,
            data_inicio = data_inicio,
            data_termino = data_termino,
            horario_saida = horario_saida,
            horario_chegada = horario_chegada
        )
        return redirect('listar_viagens')
        
    return render(request, 'gestao/novaviagem.html')


# 4. Detalhes da Viagem / Tabela de Passageiros (viagem.html ou detalhesviagem.html)
def detalhes_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    passageiros = Passageiro.objects.filter(viagem=viagem)
    
    context = {
        'viagem': viagem,
        'passageiros': passageiros
    }
    # Podes usar 'gestao/viagem.html' (versão em tabela) ou 'gestao/detalhesviagem.html' (cards)
    return render(request, 'gestao/viagem.html', context)


# 5. Cadastrar Novo Passageiro numa Viagem (novopassageiro.html)
def novo_passageiro(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        documento = request.POST.get('documento')
        nacionalidade = request.POST.get('nacionalidade')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        nome_emergencia = request.POST.get('nome_emergencia')
        telefone_emergencia = request.POST.get('telefone_emergencia')
        
        Passageiro.objects.create(
            viagem = viagem,
            nome = nome,
            documento = documento,
            nacionalidade = nacionalidade,
            telefone = telefone,
            data_nascimento = data_nascimento,
            nome_emergencia = nome_emergencia,
            telefone_emergencia = telefone_emergencia
        )
        return redirect('detalhes_viagem', viagem_id=viagem.id)
        
    context = {'viagem': viagem}
    return render(request, 'gestao/novopassageiro.html', context)


# 6. Ficha de Detalhes do Passageiro (detalhespassageiro.html)
def detalhes_passageiro(request, passageiro_id):
    passageiro = get_object_or_404(Passageiro, id=passageiro_id)
    context = {'passageiro': passageiro}
    return render(request, 'gestao/detalhespassageiro.html', context)