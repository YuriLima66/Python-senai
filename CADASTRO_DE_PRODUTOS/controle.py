# Importando os módulos necessários do PyQt5
from PyQt5 import uic, QtWidgets

# Função a ser executada quando um botão de rádio é clicado
def funcao_principal():
    # Obtendo o texto dos campos de linha no formulário
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    # Verificando qual botão de rádio está marcado e imprimindo a mensagem correspondente
    if formulario.radioButton.isChecked():
        print("Categoria Informática foi selecionada")
    elif formulario.radioButton_2.isChecked():
        print("Categoria Eletrônicos foi selecionada")
    elif formulario.radioButton_3.isChecked():
        print("Categoria Alimentos foi selecionada")

    # Imprimindo os valores dos campos de linha
    print("Código:", linha1)
    print("Descrição:", linha2)
    print("Preço:", linha3)

# Criando uma instância de QApplication
app = QtWidgets.QApplication([])

# Carregando o formulário de interface do usuário a partir do arquivo .ui
formulario = uic.loadUi("formulario.ui")

# Conectando o sinal de clique dos botões de rádio à função funcao_principal
formulario.pushButton.clicked.connect(funcao_principal)

# Exibindo o formulário
formulario.show()

# Executando a aplicação
app.exec()
