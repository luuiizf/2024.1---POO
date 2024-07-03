Circulo circulo = new Circulo();
Console.WriteLine("Informe o valor do raio do circulo: ");
circulo.raio = double.Parse(Console.ReadLine());
Console.WriteLine("Essa é a área do círculo: ");
Console.WriteLine(circulo.CalcArea());
Console.WriteLine("Essa é a circunferência do círculo: ");
Console.WriteLine(circulo.CalcCirc());