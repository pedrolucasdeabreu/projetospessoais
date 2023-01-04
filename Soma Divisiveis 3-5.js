function Multiplo3_5(max){
    resultado = 0
    for (i=0;i<max;i++){
        if (i%3==0 || i%5==0){
            resultado = resultado + i
        }
    }
    console.log ("A soma de todos os números divisiveis por 3 ou 5 é: " + resultado);
}
Multiplo3_5(10)