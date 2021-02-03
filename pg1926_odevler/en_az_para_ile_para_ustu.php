<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<title>en az para ile para ustu</title>
	</head>
	<body>
        <?php
        if(isset($_POST))
        {
            echo "<h1>Param:".$_POST["para"]."</h1><br>";
            para_ustu($_POST);
        }
        function para_ustu($paraustu){
            $dizi=array(1,5,10,25,50);
            for($sayi=0;$sayi<=6;$sayi++){
                $adet=$paraustu/$dizi[$sayi];
                if($adet!=0){
                    echo $adet.'adet:'.$dizi[$sayi].'TL';
                    $paraustu%=$dizi[$sayi];
                }
            }
        }
        ?>
        <form action="" method="post">
            <input type="text" name="para">
            <input type="submit" name="gonder" value="Hesapla">
        </form>
	</body>
</html>