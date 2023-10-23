<?php
$anos = 20;
$mes = 7;
$dist = 15;
echo "Amanda tem $anos anos!";
echo '<br />';
echo 'Amanda tem $anos anos!';
echo '<br />';
echo "No mês ", $mes, " Fabiana completara {$anos}anos!";
echo '<br />';
echo "no mês " . $mes, " Teremos ", $anos . " anos de casa.";
echo '<br />';
echo "Percorreu {$dist}km<br />";
echo "Vinicius percorreu " . $dist . 'Km';


$exem = 0;
$texto = <<<BLOCO_HEREDOC
    Texto com varia linhas.
    Podendo conter aspas ' ou " sem influenciar em nada.
    Assim como variaveis, $exem tudo em um so texto.
    BLOCO_HEREDOC;

echo "<pre>$texto</pre>";


$maxSal = 1000;
$str = <<<SQL
    SELECT FROM Funcionario
    WHERE salario > $maxSal and
    codDepart = 'Vendas'
    SQL;

echo $str . "<br><br><br>";


$alunos = array(
    "20233698" => "Raphael",
    "20233699" => "Caroline",
    "20233700" => "Vinicius"
);

echo $alunos['20233698'];
echo $alunos[2];
echo "<br><br><br>";

function saudacaoPersonalizada($nome = "Usuário")
{
    echo "Olá, $nome!";
}

saudacaoPersonalizada();
saudacaoPersonalizada("Raphael");
echo "<br><br><br>";
$quadrado = function ($x) {
    return $x * $x;
};

echo $quadrado(4);
echo "<br><br><br>";

$quadrado = fn ($x) => $x * $x;

echo $quadrado(4);
echo "<br><br><br>";

function maiorQue($x, $y)
{
    if ($x > $y)
        return $x;
    else
        return $y;
}
$maior = maiorQue(8, 7);
function maiorQue2(float $x, int $y)
{
    if ($x > $y)
        return $x;
    else
        return $y;
}
$maior = maiorQue2(8.5, 7);

class Pessoa {
    public $nome;
    public $idade;

    public function apresentar() {
        echo "Olá, meu nome é {$this->nome} e eu tenho {$this->idade} anos.";
    }
}

$pessoa01 = new Pessoa();
$pessoa01->nome = "Raphael";
$pessoa01->idade = 39;
$pessoa01->apresentar();