<?php 
date_default_timezone_set('Europe/Istanbul'); 

$saat = date("H:i",strtotime("now"));
if( $saat >"06:00"and $saat<="10:00" ){
    echo "Gunaydin ";
} 
elseif($saat>"10:00" and $saat<="17:00"){
    echo "iyi gunler";
}
elseif($saat>"17:00" and $saat<="20:00"){
    echo "iyi aksamlar ";
}
elseif($saat>"20:00" and $saat<="00:00"){
    echo "iyi geceler ";
}
elseif($saat>"00:00" and $saat<="06:00"){
    echo "esenlikler dilerim ";
}

?> 