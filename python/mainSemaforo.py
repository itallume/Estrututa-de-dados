from semaforoTemporizado import estado, semaforoTemporizado

semaforo = semaforoTemporizado()
print(semaforo.getEstadoAtual())
print(semaforo.__dict__)
s1 = semaforoTemporizado(estado.vermelho)
s2 = semaforoTemporizado()

print(s1)
print(s2)