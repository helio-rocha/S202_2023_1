from database import Database

db = Database("bolt://3.83.151.183:7687", "neo4j", "ribs-folder-tongue")

# Questão 1

query = 'MATCH(t:Teacher {name : "Renzo"}) return t.ano_nasc as ano_nasc, t.cpf as cpf'
results = db.execute_query(query)
teacher = [(result["ano_nasc"], result['cpf']) for result in results]
print('1.a)')
print("Ano de Nascimento: " + str(teacher[0][0]))
print("CPF: " + teacher[0][1])
print()


query = 'MATCH(t:Teacher) WHERE LEFT(t.name,1) = \'M\' return t.name as name, t.cpf as cpf'
results = db.execute_query(query)
teacher = [(result["name"], result['cpf']) for result in results]
print('1.b)')
for t in teacher:
    print("Nome: " + t[0])
    print("CPF: " + t[1])
    print()

query = 'MATCH(c:City) return c.name AS name'
results = db.execute_query(query)
city = [(result["name"]) for result in results]
print('1.c)')
for c in city:
    print("Nome: " + c[0])
    print()

query = 'MATCH(s:School) WHERE s.number >= 150 and s.number <= 550 return s.name as name, s.address as address, s.number as number'
results = db.execute_query(query)
school = [(result["name"], result['address'], result['number']) for result in results]
print('1.d)')
for s in school:
    print("Nome: " + s[0])
    print("Endereço: " + s[1])
    print("Número: " + str(s[2]))
    print() 

# Questão 2

query = 'MATCH(t:Teacher) return MIN(t.ano_nasc) as ano_nasc_mais_vel, MAX(t.ano_nasc) as ano_nasc_mais_nov'
results = db.execute_query(query)
teacher = [(result["ano_nasc_mais_vel"], result['ano_nasc_mais_nov']) for result in results]
print('2.a)')
print("Ano de nascimento do professor mais velho: " + str(teacher[0][0]))
print("Ano de nascimento do professor mais novo: " + str(teacher[0][1]))
print()

query = 'MATCH(c:City) return AVG(c.population) as population'
results = db.execute_query(query)
city = [(result["population"]) for result in results]
print('2.b)')
print("População média: " + str(city[0]))
print()

query = 'MATCH(c:City {cep: "37540-000"}) return REPLACE(c.name,\'a\',\'A\') as name'
results = db.execute_query(query)
city = [(result["name"]) for result in results]
print('2.c)')
print("Nome: " + city[0])
print()


query = 'MATCH(t:Teacher) return SUBSTRING(t.name,2,1) as name'
results = db.execute_query(query)
teacher = [(result["name"]) for result in results]
print('2.d)')
for t in teacher:
    print("Nome: " + t)
print()

