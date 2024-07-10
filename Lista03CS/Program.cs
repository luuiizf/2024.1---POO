class Program {
    public static void Main() {
    Frete x = new Frete(0, 0);
    Console.WriteLine("Escreva a distância do frete a ser entregue: ");   
    x.set_distancia (double.Parse(Console.ReadLine()));
    Console.WriteLine("Escreva o peso do frete a ser entregue: ");
    x.set_peso (double.Parse(Console.ReadLine()));

    Console.WriteLine($"O valor do frete é de {x.calc_frete} cuja distância é {x.get_distancia()} e o peso {x.get_peso()}");
    }
}

