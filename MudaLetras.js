function MudaLetras(str){
    let final1 = []
    let final2 = []
    const alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j <= alfabeto.length; j++){
            if (str[i] == alfabeto[j]){
                final1.push(alfabeto[j+1])
                }
        }
        if (final1[i] == 'a' || final1[i] == 'e' || final1[i] == 'i' || final1[i] == 'o' || final1[i] == 'u'){
            final2.push(final1[i].toUpperCase())
        }
        else{
            final2.push(final1[i])
        }
    }
    console.log ("O novo vetor é: " + final2)
}
MudaLetras("flamengo")