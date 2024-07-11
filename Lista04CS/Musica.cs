 class Musica {
    private string nome;
    private string artista;
    private string album;

    public void SetNome(string nome) {
        this nome = nome;
    }
    public void SetArtista(string artista) {
        this artista = artista;
    }
    public void SetAlbum(string album) {
        this album = album;
    }
    public string GetNome() {
        return this.nome;
    }
    public string GetArtista() {
        return this.artista;
    }
    public string GetAlbum() {
        return this.album;
    }
    public override string ToString() {
        return $"A música na posição desejada na playlist é {this.musicas.IndexOf}";
         
    }
  }