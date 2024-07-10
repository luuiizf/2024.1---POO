using System;

class Frete {
  private double distancia;
  private double peso;

public Frete(double distancia, double peso) {
  if (distancia < 0 || peso < 0) {
    throw new ArgumentOutOfRangeException("distancia e peso devem ser maiores que zero");
  }
  this.distancia = distancia;
  this.peso = peso;
}

  public double get_distancia() {
    return distancia;
  }
  public double get_peso() {
    return peso;
  }
  public void set_distancia(double distancia) {
    if (distancia < 0) {
      throw new ArgumentOutOfRangeException("distancia deve ser maior que zero");
    }
    this.distancia = distancia;
  }
  public void set_peso(double peso) {
    if (peso < 0) {
      throw new ArgumentException("Peso deve ser maior que zero");
    }
    this.peso = peso;
  }
  public double calc_frete() {
    return distancia * peso * 0.01;
  }
  public override string ToString() {
    return $"Distancia: {distancia} km's - Peso: {peso} kg";
  }
}

