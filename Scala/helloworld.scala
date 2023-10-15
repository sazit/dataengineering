// scalac helloword.scala first then scala helloworld, like javac

// scala 2
//object helloworld {
//  def main(args: Array[String]) = {
//    println("Hello, world!")
//  }
//}


// scala 3
import scala.io.StdIn.readLine

@main def helloworld() =
  println("Hello, World!")
  println("Now, please enter your name:")
  val your_name = readLine()

  println("Hello, " + your_name + "!")