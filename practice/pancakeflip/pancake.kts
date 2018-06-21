
val PLUS = '+'
val MINUS = '-'


fun String.flip() = this.map {
    if (it == PLUS) MINUS else PLUS
}.joinToString(separator = "")

tailrec fun flippie(s: String, k: Int, cnt: Int = 0): String {
    val i = s.indexOf(MINUS)
    if (i == -1) return cnt.toString()
    val lastChunk = s.length - k
    return when {
        i <= lastChunk -> flippie(s.substring(0, i) + s.substring(i, i + k).flip() + s.substring(i + k), k, cnt + 1)
        s.substring(lastChunk) == PLUS.toString().repeat(k) -> cnt.toString()
        else -> "IMPOSSIBLE"
    }
}

// IO
val T = readLine()?.toInt() ?: 0
for (t in 1..T) {
    val (s, k) = readLine()!!.split(" ")
    println("Case #$t: ${flippie(s, k.toInt())}")
}
