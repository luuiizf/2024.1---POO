namespace Lista02CS;

class Program
{
    static void Main(string[] args)
    {
        Viagem x = new Viagem();
        Console.WriteLine("Digite a distância em km: ");
        x.set_distancia(double.Parse(Console.ReadLine()));
        Console.WriteLine("Digite o tempo em horas: ");
        x.set_tempo(double.Parse(Console.ReadLine()));
        Console.WriteLine($"Uma viagem cuja distância é de {x.get_distancia()} kms e o tempo {x.get_tempo()} horas");
        Console.WriteLine($"Tem a velocidade média = {x.velocidade_media()}");
    }
}
