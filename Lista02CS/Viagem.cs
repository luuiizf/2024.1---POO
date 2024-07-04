class Viagem {
    private double distancia = 0;
    private double tempo = 0;
    public void set_distancia(double d) {
        if (d >= 0) distancia = d;
        else throw new ArgumentOutOfRangeException();
    }
    public void set_tempo(double t) {
        if (t >= 0) tempo = t;
        else throw new ArgumentOutOfRangeException();
    }
    public double get_distancia() {
        return distancia;
    }
    public double get_tempo(){
        return tempo;
    }
    public double velocidade_media(){
        return distancia / tempo;
    }
}