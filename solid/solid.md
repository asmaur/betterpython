# Os Principios de S.O.L.I.D

Principio criar e explicitado por Robert C. Martins no livro.
    - Versão inglês: [Clean Code](https://amzn.to/421yEht) (Link da Amazon)
    - Versão Português: [Código Limpo](https://amzn.to/4b06ZBC) (Link Amazon)

O **SOLID** são os 5 principios da programação orientado a objetos que signiicam.

- ***S***: Princípio da Responsabilidade única (Single Responsibility)
    : O principio da responsabilidade única explicita que uma class deve ser especializada em uma única tarefa. Seja deve possuir apenas uma responsabilidade dentro do software ou ter uma ação para executar.

- ***O***:  Princípio Aberto/Fechado (Open/Closed)
    : Este princípio explicita que as classes devem estar aberto para extensão mas fechada para modificação. Quando precisamos adicionar novas funcionalidades ou features, é boa pratica segundo este princípio extender a class ao invés de modificar o código original.

- ***L***: Princípio da Substituição de Liskov (Liskov Substituição)
    : Uma classe derivada deve ser substituível por sua classe base ou seja, a permutação de duas subclasses da mesma classe base não deve alterar o comportamento do sistema.

- ***I***: Princípio da Segragação de Interfaces (Interface Segregation)
    : A Segragation de interfaces estipula que uma classe não deve ser forçada implementar interfaces ou métodos que ela não irá usar. Assim sendo, é melhor criar interfaces mais especificas ao invés de interfaces mais genéricas.

- ***D***: Princípio da Inversão de Dependência (Dependency Inversion)
    : O princípio explicita a necessidade de depender de abstrações e não de implementações. Uma classe de alto nível não deve depender de módulos de baixo nível. E tanto os módulos de baixo e alto níveis devem depender de abstrações. As abstrações não pode se preocupar nem depender de detalhes mas as implementações dos detalhes dependem das abstrações.

## Pratica

    - Esse Repositorio contêm código pratica explicando os 5 principios solid.
    - Se preferir em Video veja no canal: [SOLID Descomplicado c/ Python]()
  