#IMporta o arquivo que contem a classe bancaria
from poo03 import ContaBancaria

conta_um = ContaBancaria("Marcos Flamengo",1000)
conta_um.consulta_saldo()

conta_um.depositar(200)
conta_um.consulta_saldo()
