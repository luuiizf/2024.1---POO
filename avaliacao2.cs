using System.Collections.Generic;

class Disciplina {
    private string nome;
    private string semestre;
    private double media;
    private int ch;
    private bool aprovado;

    public Disciplina (string nome, string semestre, double media, int ch, bool aprovado) {
      this.nome = nome;
      this.semestre = semestre;
      this.media = media;
      this.ch = ch;
      this.aprovado = aprovado;
      if (nome == "") throw new ArgumentOutOfRangeException("Nome não pode ser vazio");
      if (semestre == "") throw new ArgumentOutOfRangeException("Semestre não pode ser vazio");
      if (media < 0 || media > 100) throw new ArgumentOutOfRangeException("Media não pode ser menor que zero ou maior que 100");
      if (ch <= 0) throw new ArgumentOutOfRangeException("Carga horária não pode ser menor ou igual a zero");
    }
  
    public void SetNome(string nome) {
      this.nome = nome;
      if (nome == "") throw new ArgumentOutOfRangeException("Nome não pode ser vazio");
    }
    public void SetSemestre(string semestre) {
      this.semestre = semestre;
      if (semestre == "") throw new ArgumentOutOfRangeException("Semestre não pode ser vazio");
    }
    public void SetMedia(double media) {
      if (media < 0 || media > 100) throw new ArgumentOutOfRangeException("Media não pode ser menor que zero ou maior que 100");
    }
    public void SetCh(int ch) {
      if (ch <= 0) throw new ArgumentOutOfRangeException("Carga horária não pode ser menor ou igual a zero");
    }
    public void SetAprovado(bool aprovado) {
        if (this.media >= 60) {
          this.aprovado = true;
        } else {
          this.aprovado = false;
        }  
    }
    public string GetNome() {
      return this.nome;
    }
    public string GetSemestre() {
      return this.semestre;
    }
    public double GetMedia() {
      return this.media;
    }
    public int GetCh() {
      return this.ch;
    }
    public bool GetAprovado() {
      return this.aprovado;
    }
    public override string ToString() { 
      return $"Nome: {this.nome}, Semestre: {this.semestre}, Média:{this.media}, Carga Horária: {this.ch}, Situação: {this.aprovado}";
  }
}

class Historico {
  private string aluno;
  private List<Disciplina> disciplinas;
  public Historico(string aluno) {
    this.aluno = aluno;
    this.disciplinas = new List<Disciplina>();
  }

  public void Inserir(Disciplina disciplina) {
    disciplinas.Add(disciplina);
  }
  public List<Disciplina> Listar() {
    return disciplinas;
  }
  public List<Disciplina> ListarSemestre(string semestre) {
    return disciplinas.Where(d => d.GetSemestre() == semestre).ToList(); 
  }
  public List<Disciplina> MaiorMedia() {
      var maiorMedia = disciplinas.Max(d => d.Media);
      return disciplinas.Where(d => d.Media == maiorMedia).ToList();
  }
  public override string ToString() {
      return $"Aluno: {this.aluno}, Disciplinas no histórico: {this.disciplinas.Count}";
  }
}

class Program {
  static void Main() {
     Disciplina a = new Disciplina("POO", "2024.1", 80, 120, true);
     Disciplina b = new Disciplina("Algoritmos", "2024.1", 60, 60, true);
     Disciplina c = new Disciplina("IHC", "2024.1", 50, 60, false);

    Console.WriteLine(a);
    Console.WriteLine(b);
    Console.WriteLine(c);
     
      Historico historico = new Historico("Luiz");

       historico.Inserir(a);
       historico.Inserir(b);
       historico.Inserir(c);

    
  }
}
