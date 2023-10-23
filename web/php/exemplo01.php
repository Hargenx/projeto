<?php
// AND
var_dump(  7 == 7  AND 9 > 7  );  // TRUE, ambas as expressões são verdadeiras
echo "<br>";
var_dump(  7 == 7  AND 9 < 7  );  // FALSE, apenas a primeira expressão é verdadeira
echo "<br>";
// OR
var_dump(  7 == 7  OR 9 > 7  );   // TRUE, ambas as expressões são verdadeiras
echo "<br>";
var_dump(  7 != 7  OR 9 > 7  );   // TRUE, a segunda expressão é verdadeira
echo "<br>";
var_dump(  7 != 7  OR 9 < 7  );   // FALSE, ambas as expressões são falsas
echo "<br>";
// XOR
var_dump(  7 == 7  XOR 9 > 7  );  // FALSE, ambas as expressões são verdadeiras
echo "<br>";
var_dump(  7 == 7  XOR 9 < 7  );  // TRUE, a primeira expressão é verdadeira
echo "<br>";
var_dump(  7 < 7  XOR 9 > 7  );   // TRUE, a segunda expressão é verdadeira
// !
echo "<br>";
var_dump(  ! 9 < 7  );   // TRUE, 9 NÃO é menor que 7
echo "<br>";
var_dump(  ! 9 > 7  );   // FALSE, 9 é maior que 7
// &&
echo "<br>";
var_dump(  7 == 7  && 9 > 7  );   // TRUE, ambas as expressões são verdadeiras
echo "<br>";
var_dump(  7 == 7  && 9 < 7  );   // FALSE, apenas a primeira expressão é verdadeira
// ||
echo "<br>";
var_dump(  7 == 7  || 9 > 7  );   // TRUE, ambas as expressões são verdadeiras
echo "<br>";
var_dump(  7 != 7  || 9 > 7  );   // TRUE, a segunda expressão é verdadeira
echo "<br>";
var_dump(  7 != 7  || 9 < 7  );   // FALSE, ambas as expressões são falsas
