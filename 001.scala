object Problem1 {
  def kMax = 1000

  def IsMultipleOf3Or5(number: Int): Boolean = {
    return number % 3 == 0 || number % 5 == 0
  }

  def main(args: Array[String]) {
    val numbers = List.range(1, kMax)
    println((numbers filter IsMultipleOf3Or5).sum)
  }
}
