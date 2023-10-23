<?php

$php_array = [
    [
        "nome" => "Raphael",
        "idade" => 38,
        "profissao" => "Desenvolvedor"
    ],
    [
        "nome" => "Maria",
        "idade" => 30,
        "profissao" => "Médica"
    ],
    [
        "nome" => "João",
        "idade" => 25,
        "profissao" => "Engenheiro"
    ],
    [
        "nome" => "Ana",
        "idade" => 22,
        "profissao" => "Estudante"
    ],
    [
        "nome" => "Pedro",
        "idade" => 45,
        "profissao" => "Advogado"
    ],
    [
        "nome" => "Sofia",
        "idade" => 28,
        "profissao" => "Designer"
    ],
    [
        "nome" => "Carlos",
        "idade" => 50,
        "profissao" => "Professor"
    ],
    [
        "nome" => "Luisa",
        "idade" => 35,
        "profissao" => "Empresária"
    ],
    [
        "nome" => "Mariana",
        "idade" => 29,
        "profissao" => "Arquiteta"
    ],
    [
        "nome" => "André",
        "idade" => 33,
        "profissao" => "Contador"
    ]
];

echo json_encode($php_array);
echo"<br><br><br>";
for ($i = 0; $i < count($php_array); $i++) {
    echo "Nome: ".$php_array[$i]["nome"].", Idade: ".$php_array[$i]["idade"].", Profissão: ".$php_array[$i]["profissao"]."<br>";
}
echo"<br><br><br>";
foreach ($php_array as $pessoa) {
    echo "Nome: ".$pessoa["nome"].", Idade: ".$pessoa["idade"].", Profissão: ".$pessoa["profissao"]."<br>";
}
echo"<br><br><br>";
$i = 0;
while ($i < count($php_array)) {
    echo "Nome: ".$php_array[$i]["nome"].", Idade: ".$php_array[$i]["idade"].", Profissão: ".$php_array[$i]["profissao"]."<br>";
    $i++;
}
