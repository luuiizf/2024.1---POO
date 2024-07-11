namespace Lista04CS;

class Program
{
    static void Main(string[] args)
    {
        Playlist x = new Playlist();
        Console.WriteLine("Digite o nome da sua playlist: ");
        x.SetNome (string.Parse(Console.ReadLine()));
        Console.WriteLine("Digite alguma descrição para sua playlist: ")
        x.SetDescricao (string.Parse(ConsoleReadLine()));
        Console.WriteLine("Qual música você deseja inserir na playlist? ")
        string musica = Console.ReadLine();
        x.Inserir(musica);

        Musica y = new Musica();


}
