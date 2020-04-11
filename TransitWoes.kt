fun main(){
    val (s, t, n) = readLine()!!.split(' ').map { it.toInt() }
    val d: List<Int> = readLine()!!.split(' ').map { it.toInt() }
    val b: List<Int> = readLine()!!.split(' ').map { it.toInt() }
    val c: List<Int> = readLine()!!.split(' ').map { it.toInt() }

    var state = s
    var boolhls = true
    var bus = 0
    for(i in 0..n-1){
        var busArrived = c[i]
        bus += busArrived
        while (d[i] + state  > bus) {
            busArrived += busArrived
            bus += busArrived
        }
        state = busArrived
        state += b[i] + d[i+1]
        if (state > t){
            boolhls = false
            break
        }
    }
    print(if (boolhls) "yes" else "no")
}
