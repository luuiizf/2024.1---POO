class Playlist {

  private string nome;
  private string descricao;

  private List<Musica> musicas = new List<Musica>(); 

  public void SetNome(string nome) {
    this.nome = nome;
  public void SetDescricao(string descricao) {
    this.descricao = descricao;
  }
  public string GetNome() {
    return this.nome;
  }
  public string GetDescricao() {
    return this.descricao;
  }
  public void Inserir(Musica musica) {
        this.musicas.Add(musica);
  }
  public List<Musica> Listar() {
        return this.musicas;
  }
  public override string ToString() {
        return $"Essa playlist contém um total de {this.musicas.Count} músicas";